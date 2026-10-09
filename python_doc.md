# Python Learning Notes — Day 1

## 1. Why Python

Python has a huge ecosystem of packages and libraries, which reduces time to market and helps automate work.

- **Reference sites:** [python.org](https://www.python.org) and the [Python docs](https://docs.python.org) (using Python 3.14)
- **Setup:** install Python and VS Code

**Topics planned:**

- Variables, constants, conditions, loops, functions
- Libraries, data types, and data structures
- How APIs work
- Creating an AI agent
- Packaging and deploying it
- Using an AI assistant for code

---

## 2. Data Types and Data Structures

Data structures are ways of storing and organizing collections of data.

| Type | Key Point |
|---|---|
| **List** | Holds many different values |
| **Dict** | Holds key-value pairs |
| **Set** | Holds only unique values |
| **Tuple** | Immutable — values can't be changed after creation |

> **Note:** Tuple vs. list — tuple elements can still be accessed by index, but the tuple itself can't be modified after creation.

---

## 3. Conditionals

Python uses `if`, `elif`, and `else`.

**Example scenario:** As an engineer, you check whether CPU usage is above 80%. Using the `psutil` library, you take the threshold as user input and send an alert if the CPU is above it.

---

## 4. Virtual Environments

**Why:** Each project gets its own dedicated space on your system, isolated from other projects.

| Step | Command |
|---|---|
| Create | `python3.14 -m venv env` |
| Activate | `env\Scripts\activate` |
| Install packages | `pip install psutil` |

Creating the environment makes an `env` folder with its own Python inside — like a sandbox.

---

## 5. Use Case: CPU Health Check

Check CPU usage against a user-provided threshold, sampled over about 5 seconds, and report whether the CPU is healthy.

---

## 6. APIs and Requests

The `requests` library lets you interact with APIs.

Two things to look at in a response:

| Part | Description |
|---|---|
| Response | The HTTP response object itself (status code, headers, etc.) |
| Content | The actual body/data returned by the API |

---

## 7. FastAPI

**Install:**

```bash
pip install fastapi
# or
pip install "fastapi[standard]"
```

**Import:**

```python
from fastapi import FastAPI
```

`FastAPI` is a class.

---

## 8. Boto3

Boto3 is the official AWS SDK (Software Development Kit) for Python, used for AWS automation.
