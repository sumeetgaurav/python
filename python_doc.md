# Python Files Documentation — Day 1

Reference documentation for all Python files in this directory.

## File Summary

| File | Description |
|---|---|
| `hello.py` | Beginner walkthrough of Python basics: variables, primitive types, and core data structures (list, dict, tuple, set). |
| `cpu_check.py` | Takes a user-entered CPU usage value and classifies it as high, moderate, or normal. |
| `real_cpu.py` | Monitors real-time CPU usage with `psutil` and flags it as healthy or unhealthy against a user-defined threshold. |
| `system_utils.py` | Reusable utility module that collects live CPU, memory, and disk usage stats into a dictionary. |
| `show_system_info.py` | CLI script that fetches and prints current system stats using `system_utils.get_system_info()`. |
| `get_data.py` | Minimal example of fetching JSON data from a REST API using the `requests` library. |
| `s3_utils.py` | Uploads a local file to an AWS S3 bucket using `boto3`. |
| `api.py` | FastAPI web service exposing endpoints for a health check, live system metrics, and AWS S3 bucket listing. |

---

## File Details

### `hello.py`

| Field | Detail |
|---|---|
| Purpose | Demonstrates core Python syntax and data types |
| Covers | `print()`, primitives (`str`, `float`, `int`, `bool`), `type()`, `list`, `dict`, `tuple`, `set` |
| Input required | None |
| Run | `python hello.py` |

### `cpu_check.py`

| Field | Detail |
|---|---|
| Purpose | Classifies a manually entered CPU usage value |
| Input required | A numeric CPU percentage |
| Run | `python cpu_check.py` |

**Classification logic:**

| Condition | Output |
|---|---|
| `cpu > 50` | CPU usage is high |
| `20 < cpu < 50` | CPU usage is moderate |
| otherwise | CPU usage is normal |

### `real_cpu.py`

| Field | Detail |
|---|---|
| Purpose | Live CPU monitoring against a user-defined threshold |
| Library | `psutil` |
| Input required | A CPU usage threshold (%) |
| Behavior | Samples CPU usage 5 times (1-second interval each) |
| Run | `python real_cpu.py` |

| Condition | Output |
|---|---|
| Sampled usage > threshold | CPU usage is Unhealthy |
| Sampled usage ≤ threshold | CPU usage is Healthy |

### `system_utils.py`

| Field | Detail |
|---|---|
| Purpose | Reusable module — not run directly |
| Function | `get_system_info()` |
| Returns | Dictionary with `CPU Usage`, `Memory Usage`, `Disk Usage` (all %) |
| Used by | `show_system_info.py`, `api.py` |

### `show_system_info.py`

| Field | Detail |
|---|---|
| Purpose | CLI wrapper around `system_utils.get_system_info()` |
| Dependency | `system_utils.py` |
| Run | `python show_system_info.py` |

### `get_data.py`

| Field | Detail |
|---|---|
| Purpose | Example of consuming a REST API |
| Library | `requests` |
| Target API | `https://fake-json-api.mock.beeceptor.com/users` |
| Run | `python get_data.py` |

### `s3_utils.py`

| Field | Detail |
|---|---|
| Purpose | Uploads a local file to AWS S3 |
| Library | `boto3` |
| Bucket | `devops-fde` (hardcoded) |
| Requires | Valid AWS credentials |
| Run | `python s3_utils.py` |

### `api.py`

| Field | Detail |
|---|---|
| Purpose | FastAPI service exposing system + AWS metrics over HTTP |
| Libraries | `fastapi`, `uvicorn`, `boto3` |
| Run | `uvicorn api:app --reload` |

**Endpoints:**

| Method | Path | Description |
|---|---|---|
| GET | `/hello` | Returns a simple greeting JSON message |
| GET | `/metrics` | Returns live system metrics via `get_system_info()` |
| GET | `/aws/s3/buckets` | Lists all S3 bucket names in the connected AWS account |

---

## Dependency Map

| File | Depends on |
|---|---|
| `api.py` | `system_utils.py` (`get_system_info`) |
| `show_system_info.py` | `system_utils.py` (`get_system_info`) |
| `cpu_check.py`, `real_cpu.py`, `hello.py`, `get_data.py`, `s3_utils.py` | Standalone — no internal dependencies |

---

## Required Packages by File

| Package | Required by |
|---|---|
| `psutil` | `real_cpu.py`, `system_utils.py`, `show_system_info.py`, `api.py` (`/metrics`) |
| `requests` | `get_data.py` |
| `boto3` | `s3_utils.py`, `api.py` (`/aws/s3/buckets`) |
| `fastapi`, `uvicorn` | `api.py` |

`hello.py` and `cpu_check.py` use only the Python standard library.
