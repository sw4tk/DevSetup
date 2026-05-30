# DevSetup

DevSetup is a Python CLI utility that scans a developer machine, detects installed development tools, and exports environment information into a structured JSON format.

The long-term goal is to allow developers to recreate their development environments on new machines with minimal setup effort.

## Version

Current Version: v0.2.0

## Features

### Environment Scanning

Detect installed developer tools and retrieve version information.

Currently supported:

* Python
* Git
* Pip

### JSON Export

Generate a machine-readable environment snapshot.

Example:

```json
{
    "python": {
        "installed": true,
        "version": "Python 3.14.0"
    },
    "git": {
        "installed": true,
        "version": "git version 2.50.1"
    }
}
```

### Environment Reports

Generate a human-readable report showing:

* Total tools scanned
* Installed tools
* Missing tools

Example:

```text
DevSetup Report
====================

Total Scanned: 3

Installed:
✔ python : Python 3.14.0
✔ git : git version 2.50.1

Missing:
✘ node
```

## Project Structure

```text
devsetup/

├── main.py
├── scanner.py
├── saver.py
├── filter.py
├── tools.py
├── data.json
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/sw4tk/DevSetup
```

Move into the project directory:

```bash
cd devsetup
```

Run:

```bash
python main.py
```

## Roadmap

### v0.1

* Tool detection
* Version scanning

### v0.2

* JSON export
* Environment reports

### v0.3

* CLI commands
* Scan command
* Report command
* Version command

### v0.4

* Environment profiles

### v0.5

* Environment comparison

### v1.0

* Environment recreation
* One-command machine setup

## Long-Term Vision

Infrastructure as Code manages servers.

DevSetup aims to manage developer machines.

A developer should be able to move to a completely new machine and restore their workflow with minimal effort.

## Author

Swastik
