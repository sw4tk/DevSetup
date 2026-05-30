# DevSetup

DevSetup is a Python CLI tool that scans a developer machine and detects installed development tools and their versions.

The project is being built to eventually help developers export and recreate their development environments across different machines.

## Features

### Current Features (v0.1)

* Detect installed development tools
* Check tool availability
* Retrieve tool version information
* Modular project structure
* Error handling for missing tools

### Supported Tools

* Python
* Git
* Pip

## Project Structure

```text
devsetup/

├── main.py
├── scanner.py
├── tools.py
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/devsetup.git
```

Move into the project directory:

```bash
cd devsetup
```

## Usage

Run:

```bash
python main.py
```

Example Output:

```text
python : Python 3.14.0
git : git version 2.50.1.windows.1
pip : pip 25.1
```

If a tool is not installed:

```text
node : Not found
```

## How It Works

DevSetup uses Python's `subprocess` module to execute version commands and determine whether developer tools are installed.

Example:

```python
subprocess.run(
    ["python", "--version"],
    capture_output=True,
    text=True
)
```

## Learning Goals

This project is helping me learn:

* Python automation
* System programming
* CLI application development
* Subprocess management
* Project architecture
* Environment configuration tools

## Roadmap

### v0.1

* Tool detection
* Version scanning
* Modular architecture

### v0.2

* JSON export
* Environment reports

### v0.3

* CLI commands
* Configuration management

### v0.4

* Profile support

### v1.0

* Environment export and recreation

## Long-Term Vision

DevSetup aims to become a tool that allows developers to move to a new machine and restore their development environment with minimal setup effort.

## Author

Swastik
