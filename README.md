

# Z1_FEISTU Tester Documentation ♿->👨‍🔬

Welcome, cutie! Welcome to **Z1_FEISTU**! This guide will help you get started with the project, understand its usage and make your live simpler . Let's dive in, and remember, every step is a step toward mastery! UwU

---

## Table of Contents

- [Installation & Setup](#installation--setup)
- [Docker 🐋](#docker-)


## Installation & Setup

Hey there! Ready to get started? Follow these steps to install and run the project on your local machine:

1. **Clone the Repo:**
   ```bash
   git clone https://github.com/zxcamon4ik/Z1_FEISTU.git
   cd Z1_FEISTU
   ```
2. **Install Dependencies:**
   Make sure you have [python3.12+](https://www.python.org/) and [gcc](https://gcc.gnu.org/) installed.
3. **Attach test file.c**
   Put .c file named z1.c in root of project, or specify it using SRC argument in make, SRC=/path/to/file
   
4. **Run the Project:**
   ```bash
   make run
   ```
   >```bash
   >make run SRC=/path/to/file
   >```
---

## Docker 🐋
Few dockers things that I have done for fun!

Run Docker 🏃

```bash
make d-run
```
>Also you can specify path to file as been said before:
>```bash
>make d-run SRC=/path/to/file
>```
Purge Docker Content
```bash
make d-purge
```
