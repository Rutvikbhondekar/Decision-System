

# 🚀 Configurable Workflow Decision Platform

## 🧠 Overview

This project implements a **configurable workflow decision system** where workflows and business rules are defined using YAML.
It enables dynamic decision-making without modifying application code, making the system flexible, scalable, and easy to maintain.

---

## 🎯 Key Features

* 🔹 YAML-driven workflow configuration
* 🔹 Rule engine supporting validation and threshold checks
* 🔹 Modular workflow execution engine
* 🔹 State management for tracking request lifecycle
* 🔹 Audit logging for full traceability
* 🔹 REST API built using FastAPI
* 🔹 Support for failure handling and manual review flows

---

## 🏗️ System Architecture

<img width="1536" height="1024" alt="Copilot_20260327_140900" src="https://github.com/user-attachments/assets/78f64c29-6c35-4d7a-9ab2-b5371a661f2a" />

The system follows a modular pipeline:

```text
Request → Validation → Rule Engine → Workflow Execution → Decision → State → Audit
```

---

## 📁 Project Structure

```text
config/
  ├── rules/        # Rule definitions (YAML)
  └── workflows/    # Workflow definitions (YAML)

core/               # Core engine logic
tests/              # Test cases

main.py             # FastAPI application entry point
```

---

## 🚀 Getting Started

### 1️⃣ Install Dependencies

```bash
pip install fastapi uvicorn pyyaml pytest
```

---

### 2️⃣ Run the Application

```bash
python -m uvicorn main:app --reload
```

---

### 3️⃣ Access API Documentation

Open in browser:

```text
http://127.0.0.1:8000/docs
```

---

## 🧪 API Usage

### Endpoint

```text
POST /workflow/{workflow_name}/execute
```

---

## ✅ Successful Execution (Approved Case)

![Approved Output](./screenshots/approved.png)

✔ All validation and rules passed
✔ Workflow completed successfully

---

## ❌ Validation Failure (Rejected Case)

![Rejected Output](./screenshots/rejected.png)

✔ Missing required fields
✔ System correctly rejects invalid input

---

## 🔍 Audit Logs (Execution Trace)

![Audit Logs](./screenshots/audit.png)

✔ Captures step-by-step execution
✔ Enables debugging and traceability

---
🧠 How It Works
The request is received via API
Input validation rules are applied
Business rules are evaluated
Workflow stages are executed sequentially
Final decision is determined
State and audit logs are recorded

---

🔗 Repository

https://github.com/Rutvikbhondekar/Decision-System

---

👨‍💻 Author

Rutvik Bhondekar
