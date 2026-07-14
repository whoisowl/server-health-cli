# 🖥️ Server Health CLI

```{=html}

```
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS-blue?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

```{=html}

```

------------------------------------------------------------------------

# 🇺🇸 English

## Overview

**Server Health CLI** is a lightweight Python-based command-line tool
for monitoring system health.

### Features

-   CPU usage monitoring
-   Memory usage monitoring
-   Disk usage monitoring
-   Hostname & current user
-   System uptime
-   Top CPU and memory consuming processes
-   JSON output
-   Watch mode
-   Configurable alert thresholds
-   Colored terminal output
-   Proper exit codes for automation

## Installation

``` bash
git clone https://github.com/whoisowl/server-health-cli.git
cd server-health-cli
pip install -r requirements.txt
```

## Usage

Run normally:

``` bash
python health_check.py
```

JSON output:

``` bash
python health_check.py --json
```

Watch mode:

``` bash
python health_check.py --watch 5
```

Custom thresholds:

``` bash
python health_check.py --cpu-threshold 85 --memory-threshold 80 --disk-threshold 90
```

## Built With

-   Python
-   psutil
-   argparse

## License

MIT License

------------------------------------------------------------------------

# 🇮🇷 فارسی

## معرفی

**Server Health CLI** یک ابزار خط فرمان (CLI) است که با زبان **Python**
برای بررسی وضعیت سیستم توسعه داده شده است.

### امکانات

-   نمایش میزان استفاده از CPU
-   نمایش میزان استفاده از حافظه (RAM)
-   نمایش میزان استفاده از دیسک
-   نمایش نام سیستم (Hostname)
-   نمایش کاربر فعلی
-   نمایش مدت زمان روشن بودن سیستم (Uptime)
-   نمایش پردازش‌های با بیشترین مصرف CPU و حافظه
-   خروجی JSON
-   حالت Watch
-   امکان تعیین آستانه هشدار
-   خروجی رنگی در ترمینال
-   Exit Code مناسب برای اتوماسیون

## نصب

``` bash
git clone https://github.com/whoisowl/server-health-cli.git
cd server-health-cli
pip install -r requirements.txt
```

## اجرا

``` bash
python health_check.py
```

خروجی JSON:

``` bash
python health_check.py --json
```

حالت بروزرسانی خودکار:

``` bash
python health_check.py --watch 5
```

آستانه دلخواه:

``` bash
python health_check.py --cpu-threshold 85 --memory-threshold 80 --disk-threshold 90
```

## تکنولوژی‌های استفاده شده

-   Python
-   psutil
-   argparse

## مجوز

این پروژه تحت مجوز MIT منتشر شده است.

------------------------------------------------------------------------

## 👨‍💻 Author \| توسعه‌دهنده

**Arian Salarian**

GitHub: https://github.com/whoisowl

⭐ If you found this project useful, consider giving it a star!

⭐ اگر این پروژه برایتان مفید بود، خوشحال می‌شوم به آن ستاره بدهید.
