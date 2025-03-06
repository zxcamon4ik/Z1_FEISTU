# Z1_FEISTU Tester Documentation ♿→👨‍🔬

Welcome, cutie! Welcome to **Z1_FEISTU**! This guide will help you get started with the project, understand its usage, and make your life simpler. Let's dive in—every step is a step toward mastery! UwU

---

## Table of Contents

- [Installation & Setup](#installation--setup)
- [Docker 🐋](#docker-)

---

## Installation & Setup

Hey there! Ready to get started? Follow these steps to install and run the project on your local machine:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/zxcamon4ik/Z1_FEISTU.git
   cd Z1_FEISTU
   ```

2. **Install Dependencies:**
   Make sure you have [Python 3.12+](https://www.python.org/) and [GCC](https://gcc.gnu.org/) installed.

3. **Prepare Your C File:**
   - Place your `.c` file named **z1.c** in the root of the project.
   - Alternatively, you can specify a different file using the `SRC` argument:
     ```bash
     make run SRC=/path/to/file
     ```

4. **Run the Project:**
   ```bash
   make run
   ```
   > To run with a custom source file, use:
   > ```bash
   > make run SRC=/path/to/file
   > ```

---

## Docker 🐋

A few Docker commands for fun and convenience!

### Run in Docker 🏃
To execute the tester inside a Docker container:
```bash
make d-run
```
> You can also specify a custom source file:
> ```bash
> make d-run SRC=/path/to/file
> ```

### Purge Docker Content ♻️
To clean up Docker-related artifacts:
```bash
make d-purge
```

---
