# Day 1 — Python Scripts

Overview of all Python files in this directory, what each one does, and how to run it.

## Prerequisites

### 1. Python

Python 3.9+ is required (this project was tested with Python 3.14). Verify it's installed:

```powershell
python --version
```

### 2. Virtual environment

A virtual environment folder (`env/`) already exists in this directory. Activate it before installing packages or running scripts, so dependencies stay isolated from your system Python:

```powershell
# PowerShell
.\env\Scripts\Activate.ps1
```
```bash
# Git Bash
source env/Scripts/activate
```

If `env/` didn't exist, you'd create it with `python -m venv env` first.

### 3. Required packages

Install everything needed by every script in one go:

```bash
pip install fastapi uvicorn boto3 requests psutil
```

Or install only what a specific script needs:

| Package | Needed by | Install |
|---|---|---|
| `psutil` | `real_cpu.py`, `system_utils.py`, `show_system_info.py`, `api.py` (`/metrics`) | `pip install psutil` |
| `requests` | `get_data.py` | `pip install requests` |
| `boto3` | `s3_utils.py`, `api.py` (`/aws/s3/buckets`) | `pip install boto3` |
| `fastapi` + `uvicorn` | `api.py` | `pip install fastapi uvicorn` |

`hello.py` and `cpu_check.py` use only the Python standard library — no extra packages needed.

### 4. AWS credentials (only for S3-related scripts)

`s3_utils.py` and the `/aws/s3/buckets` endpoint in `api.py` use `boto3`, which needs valid AWS credentials to talk to S3. Set these up with **one** of the following before running them:

```bash
aws configure
```
or set environment variables:
```bash
# Git Bash
export AWS_ACCESS_KEY_ID=your_key
export AWS_SECRET_ACCESS_KEY=your_secret
export AWS_DEFAULT_REGION=your_region
```
```powershell
# PowerShell
$env:AWS_ACCESS_KEY_ID="your_key"
$env:AWS_SECRET_ACCESS_KEY="your_secret"
$env:AWS_DEFAULT_REGION="your_region"
```

The AWS identity used must have permission to list buckets (`s3:ListAllMyBuckets`) and upload objects (`s3:PutObject`) to the target bucket (`devops-fde` in `s3_utils.py`).

### 5. Internet access

`get_data.py` and the S3-related scripts require outbound internet access to reach the mock API and AWS endpoints respectively.

---

## `hello.py`

**Purpose:** Beginner-level walkthrough of core Python syntax.

**What it covers:**
- `print()` output
- Primitive data types: `str`, `float`, `int`, `bool`, and inspecting them with `type()`
- Non-primitive data structures: `list`, `dict`, `tuple`, `set`
- Dictionary key access and set de-duplication behavior

**Usage:**
```bash
python hello.py
```
No input required — just prints demonstration output. Not a reusable module.

---

## `cpu_check.py`

**Purpose:** Simple script that classifies a CPU usage value entered by the user.

**Logic:** Prompts for a numeric CPU percentage and prints:
- `"CPU usage is high"` if > 50
- `"CPU usage is moderate"` if between 20 and 50
- `"CPU usage is normal"` otherwise

**Usage:**
```bash
python cpu_check.py
# Enter the CPU: 65
```

---

## `real_cpu.py`

**Purpose:** Live CPU monitoring using `psutil` instead of manual input.

**Logic:** Prompts for a CPU usage threshold, then samples the real CPU usage 5 times (1-second intervals via `psutil.cpu_percent`), printing `"CPU usage is Unhealthy"` or `"CPU usage is Healthy"` for each sample depending on whether it exceeds the threshold.

**Usage:**
```bash
python real_cpu.py
# Enter the threshold for CPU usage: 50
```

---

## `system_utils.py`

**Purpose:** Reusable utility module — not meant to be run directly.

**Contents:** Defines `get_system_info()`, which uses `psutil` to collect and return a dictionary of current system stats:
- `CPU Usage` (%)
- `Memory Usage` (%)
- `Disk Usage` (%)

**Usage:** Imported by other scripts (`show_system_info.py`, `api.py`):
```python
from system_utils import get_system_info
info = get_system_info()
```

---

## `show_system_info.py`

**Purpose:** Thin CLI wrapper that calls `get_system_info()` from `system_utils.py` and prints the result.

**Usage:**
```bash
python show_system_info.py
```

---

## `get_data.py`

**Purpose:** Minimal example of calling an external REST API with the `requests` library.

**Logic:** Sends a GET request to a mock JSON API (`fake-json-api.mock.beeceptor.com/users`) and prints the JSON response — useful as a template for API consumption.

**Usage:**
```bash
python get_data.py
```

---

## `s3_utils.py`

**Purpose:** One-off script to upload a local file to an AWS S3 bucket using `boto3`.

**Logic:** Uploads `api.py` (hardcoded path) to the S3 bucket `devops-fde` under the object name `api.py`, then prints `"Upload complete"`.

**Usage:**
```bash
python s3_utils.py
```
> Note: file path and bucket name are hardcoded — edit `file_name`, `object_name`, and `bucket_name` to reuse for other files/buckets.

---

## `api.py`

**Purpose:** FastAPI web service exposing system metrics and AWS S3 info over HTTP.

**Endpoints:**
| Method | Path | Description |
|---|---|---|
| GET | `/hello` | Returns a simple greeting JSON message |
| GET | `/metrics` | Returns live system metrics via `get_system_info()` from `system_utils.py` |
| GET | `/aws/s3/buckets` | Lists all S3 bucket names in the connected AWS account via `boto3` |

**Usage:**
```bash
uvicorn api:app --reload
```
Then visit `http://127.0.0.1:8000/docs` for interactive Swagger UI, or hit endpoints directly, e.g. `http://127.0.0.1:8000/metrics`.

---

## File Dependency Map

```
api.py ──────────────► system_utils.py (get_system_info)
show_system_info.py ─► system_utils.py (get_system_info)

cpu_check.py, real_cpu.py, hello.py, get_data.py, s3_utils.py — standalone scripts
```
