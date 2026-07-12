# Server Health Check CLI

*[English](#english) | [فارسی](#فارسی)*

---

## English

A lightweight command-line tool that checks CPU, memory, and disk usage on a
Linux/Mac server, flags the top resource-consuming processes, and raises
alerts when usage crosses a configurable threshold.

### Why this exists

Real DevOps/SRE teams need quick visibility into server health without
spinning up a full monitoring stack (Prometheus/Grafana) for a single box or
a quick diagnostic check. This tool is a minimal, dependency-light version of
that idea — the same core logic that powers larger monitoring systems.

### Setup

```bash
# 1. Clone / copy this folder
cd server-health-cli

# 2. (Recommended) create a virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
```

### Usage

```bash
# Run once, human-readable output
python3 health_check.py

# Run once, JSON output (useful for piping into other tools/scripts)
python3 health_check.py --json

# Keep checking every 5 seconds until you press Ctrl+C
python3 health_check.py --watch 5

# Customize alert thresholds
python3 health_check.py --cpu-threshold 90 --memory-threshold 80 --disk-threshold 95
```

### Exit codes

- `0` — system healthy, no alerts
- `1` — one or more alerts fired

This makes it easy to plug into a cron job or CI pipeline step:
```bash
python3 health_check.py --json || echo "Server unhealthy, investigate!"
```

### Possible next steps (good "future work" talking points in an interview)

- Add a `--slack-webhook` flag to POST alerts to a Slack channel
- Add remote server checks over SSH (using `paramiko`) instead of just local
- Write results to a log file or push metrics to InfluxDB/Prometheus
- Package it with `setup.py`/`pyproject.toml` and publish to PyPI
- Add unit tests with `pytest` for the threshold-evaluation logic

### Resume bullet point (example)

> Built a Python CLI tool using `psutil` and `argparse` to monitor server
> CPU, memory, and disk usage with configurable alert thresholds and JSON
> output for pipeline integration.

---

## فارسی

یک ابزار خط‌فرمان سبک که مصرف CPU، حافظه و دیسک را روی سرور لینوکس یا مک بررسی می‌کند، پرمصرف‌ترین پردازش‌ها را نشان می‌دهد و در صورت عبور از حد آستانه‌ی تعیین‌شده، هشدار صادر می‌کند.

### چرا این ابزار ساخته شد

تیم‌های واقعی DevOps/SRE برای دید سریع نسبت به سلامت سرور، همیشه نیازی به راه‌اندازی یک استک کامل مانیتورینگ (مثل Prometheus/Grafana) ندارند؛ به‌خصوص برای یک سرور تکی یا یک بررسی سریع. این ابزار نسخه‌ای مینیمال و بدون وابستگی سنگین از همان منطق اصلی است که سیستم‌های مانیتورینگ بزرگ‌تر از آن استفاده می‌کنند.

### نصب و راه‌اندازی

```bash
# ۱. پوشه پروژه را کپی یا کلون کنید
cd server-health-cli

# ۲. (پیشنهادی) ساخت محیط مجازی
python3 -m venv venv
source venv/bin/activate

# ۳. نصب وابستگی‌ها
pip install -r requirements.txt
```

### نحوه استفاده

```bash
# اجرای یک‌باره با خروجی قابل خواندن برای انسان
python3 health_check.py

# اجرای یک‌باره با خروجی JSON (مناسب برای اتصال به ابزارهای دیگر)
python3 health_check.py --json

# بررسی مداوم هر ۵ ثانیه تا زمان فشردن Ctrl+C
python3 health_check.py --watch 5

# سفارشی‌سازی حد آستانه‌های هشدار
python3 health_check.py --cpu-threshold 90 --memory-threshold 80 --disk-threshold 95
```

### کدهای خروجی (Exit Codes)

- `۰` — سیستم سالم است، هیچ هشداری صادر نشده
- `۱` — حداقل یک هشدار صادر شده است

این ویژگی باعث می‌شود ابزار به‌راحتی در یک cron job یا مرحله‌ای از پایپ‌لاین CI قابل استفاده باشد:
```bash
python3 health_check.py --json || echo "سرور ناسالم است، بررسی کنید!"
```

### قابلیت‌های پیشنهادی برای توسعه بعدی (نکات خوب برای مصاحبه شغلی)

- افزودن فلگ `--slack-webhook` برای ارسال هشدارها به کانال Slack
- افزودن قابلیت بررسی سرورهای ریموت از طریق SSH (با استفاده از `paramiko`)
- ذخیره نتایج در فایل لاگ یا ارسال متریک‌ها به InfluxDB/Prometheus
- پکیج‌بندی پروژه با `setup.py`/`pyproject.toml` و انتشار در PyPI
- افزودن تست واحد (unit test) با `pytest` برای منطق بررسی حد آستانه‌ها

### نمونه جمله برای رزومه

> یک ابزار خط‌فرمان با پایتون و با استفاده از `psutil` و `argparse` ساختم که مصرف CPU، حافظه و دیسک سرور را با حد آستانه‌های قابل تنظیم مانیتور می‌کند و خروجی JSON برای یکپارچه‌سازی با پایپ‌لاین ارائه می‌دهد.
