#!/usr/bin/env python3
"""
Server Health Check CLI
------------------------
A command-line tool that checks CPU, memory, disk, and process health
on a Linux/Mac server, and warns you when something crosses a threshold.

Usage examples:
    python3 health_check.py                     # run once, human-readable output
    python3 health_check.py --json              # run once, JSON output (for scripting)
    python3 health_check.py --watch 5            # re-check every 5 seconds until Ctrl+C
    python3 health_check.py --cpu-threshold 90   # customize alert threshold
"""

import argparse
import json
import sys
import time
from datetime import datetime

import psutil  # third-party library: pip install psutil


# ---------------------------------------------------------------------------
# STEP 1: Functions that collect raw system data
# Each function has ONE job. This makes the code easy to test and reuse.
# ---------------------------------------------------------------------------

def get_cpu_usage():
    """Returns CPU usage as a percentage (0-100)."""
    # interval=1 means: measure over 1 second for an accurate reading
    return psutil.cpu_percent(interval=1)


def get_memory_usage():
    """Returns a dict with memory stats in percent and GB."""
    mem = psutil.virtual_memory()
    return {
        "percent": mem.percent,
        "used_gb": round(mem.used / (1024 ** 3), 2),
        "total_gb": round(mem.total / (1024 ** 3), 2),
    }


def get_disk_usage(path="/"):
    """Returns disk usage stats for the given path (default: root)."""
    disk = psutil.disk_usage(path)
    return {
        "percent": disk.percent,
        "used_gb": round(disk.used / (1024 ** 3), 2),
        "total_gb": round(disk.total / (1024 ** 3), 2),
    }


def get_top_processes(limit=5):
    """Returns the top N processes sorted by CPU usage."""
    processes = []
    for proc in psutil.process_iter(["pid", "name", "cpu_percent", "memory_percent"]):
        try:
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            # Processes can disappear between listing and reading them — just skip those.
            continue

    processes.sort(key=lambda p: p["cpu_percent"] or 0, reverse=True)
    return processes[:limit]


# ---------------------------------------------------------------------------
# STEP 2: Compare results against thresholds and build alerts
# ---------------------------------------------------------------------------

def evaluate_health(cpu, memory, disk, thresholds):
    """
    Takes the raw metrics + threshold settings and returns a list of
    human-readable warning strings. Empty list = everything is healthy.
    """
    alerts = []

    if cpu >= thresholds["cpu"]:
        alerts.append(f"HIGH CPU USAGE: {cpu}% (threshold: {thresholds['cpu']}%)")

    if memory["percent"] >= thresholds["memory"]:
        alerts.append(
            f"HIGH MEMORY USAGE: {memory['percent']}% "
            f"({memory['used_gb']}GB / {memory['total_gb']}GB) "
            f"(threshold: {thresholds['memory']}%)"
        )

    if disk["percent"] >= thresholds["disk"]:
        alerts.append(
            f"LOW DISK SPACE: {disk['percent']}% used "
            f"({disk['used_gb']}GB / {disk['total_gb']}GB) "
            f"(threshold: {thresholds['disk']}%)"
        )

    return alerts


# ---------------------------------------------------------------------------
# STEP 3: Build the full report (this is what ties everything together)
# ---------------------------------------------------------------------------

def build_report(thresholds):
    cpu = get_cpu_usage()
    memory = get_memory_usage()
    disk = get_disk_usage()
    top_processes = get_top_processes()
    alerts = evaluate_health(cpu, memory, disk, thresholds)

    return {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "cpu_percent": cpu,
        "memory": memory,
        "disk": disk,
        "top_processes": top_processes,
        "alerts": alerts,
        "status": "WARNING" if alerts else "OK",
    }


# ---------------------------------------------------------------------------
# STEP 4: Output formatting — human-readable or JSON
# ---------------------------------------------------------------------------

# ANSI color codes so the terminal output looks nice (no extra library needed)
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"
BOLD = "\033[1m"


def print_human_report(report):
    status_color = RED if report["status"] == "WARNING" else GREEN
    print(f"\n{BOLD}=== Server Health Check — {report['timestamp']} ==={RESET}")
    print(f"Status: {status_color}{report['status']}{RESET}")
    print(f"CPU Usage:    {report['cpu_percent']}%")
    print(f"Memory Usage: {report['memory']['percent']}% "
          f"({report['memory']['used_gb']}GB / {report['memory']['total_gb']}GB)")
    print(f"Disk Usage:   {report['disk']['percent']}% "
          f"({report['disk']['used_gb']}GB / {report['disk']['total_gb']}GB)")

    print(f"\n{BOLD}Top 5 processes by CPU:{RESET}")
    for proc in report["top_processes"]:
        print(f"  PID {proc['pid']:<7} {proc['name']:<25} "
              f"CPU: {proc['cpu_percent']}%  MEM: {round(proc['memory_percent'] or 0, 1)}%")

    if report["alerts"]:
        print(f"\n{BOLD}{YELLOW}⚠ Alerts:{RESET}")
        for alert in report["alerts"]:
            print(f"  {RED}- {alert}{RESET}")
    else:
        print(f"\n{GREEN}✓ All systems normal.{RESET}")


def print_json_report(report):
    print(json.dumps(report, indent=2))


# ---------------------------------------------------------------------------
# STEP 5: Command-line interface (argparse)
# ---------------------------------------------------------------------------

def parse_args():
    parser = argparse.ArgumentParser(
        description="Check server CPU, memory, disk, and process health."
    )
    parser.add_argument("--json", action="store_true",
                         help="Output the report as JSON instead of plain text.")
    parser.add_argument("--watch", type=int, metavar="SECONDS",
                         help="Re-run the check every N seconds until you press Ctrl+C.")
    parser.add_argument("--cpu-threshold", type=float, default=85.0,
                         help="CPU usage percent that triggers an alert (default: 85)")
    parser.add_argument("--memory-threshold", type=float, default=85.0,
                         help="Memory usage percent that triggers an alert (default: 85)")
    parser.add_argument("--disk-threshold", type=float, default=90.0,
                         help="Disk usage percent that triggers an alert (default: 90)")
    return parser.parse_args()


def main():
    args = parse_args()
    thresholds = {
        "cpu": args.cpu_threshold,
        "memory": args.memory_threshold,
        "disk": args.disk_threshold,
    }

    def run_once():
        report = build_report(thresholds)
        if args.json:
            print_json_report(report)
        else:
            print_human_report(report)
        return report

    if args.watch:
        try:
            while True:
                report = run_once()
                # Exit code convention: 0 = healthy, 1 = alerts fired.
                # Useful later if you wire this into a monitoring pipeline.
                time.sleep(args.watch)
        except KeyboardInterrupt:
            print("\nStopped watching.")
            sys.exit(0)
    else:
        report = run_once()
        sys.exit(1 if report["alerts"] else 0)


if __name__ == "__main__":
    main()
