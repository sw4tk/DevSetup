# DevSetup

DevSetup is an open-source Python CLI utility that scans a developer machine, detects installed development tools, analyzes environment readiness, and exports environment information into a structured JSON format.

The long-term goal of DevSetup is to make developer environments portable, reproducible, and easy to restore on new machines.

---

## Current Version

**v0.4.0**

---

## Features

### Environment Scanning

Detect installed development tools and retrieve version information.

Currently supported:

* Python
* Git
* Pip

---

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

---

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

---

### Command-Based Interface

#### Scan Environment

```bash
python main.py scan
```

Scans the environment and saves results to `data.json`.

#### Generate Report

```bash
python main.py report
```

Loads previously exported data and generates a report.

#### Show Version

```bash
python main.py version
```

Displays the current DevSetup version.

---

## Doctor Command

Analyze development environment readiness based on predefined developer profiles.

Supported Profiles:

* Web Development
* Python Development
* AI Development

Example:

```bash
python main.py doctor webdev
```

Example Output:

```text
DevSetup v0.4 Doctor
====================

Profile : Web Development
Description : Frontend and Backend Development

Environment Health : 75%
Installed : 3/4

Issues :
    vscode missing
```

---

## Project Structure

```text
devsetup/

├── main.py
├── scanner.py
├── saver.py
├── loader.py
├── categorizer.py
├── printer.py
├── doctor.py
├── profiles.py
├── tools.py
├── VERSION
├── CHANGELOG.md
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/sw4tk/DevSetup.git
```

Move into the project directory:

```bash
cd DevSetup
```

Run a scan:

```bash
python main.py scan
```

Generate a report:

```bash
python main.py report
```

Check version:

```bash
python main.py version
```

Run doctor:

```bash
python main.py doctor webdev
```

---

## Roadmap

### v0.1

* Tool detection
* Version scanning

### v0.2

* JSON export
* Environment reports

### v0.3

* Command routing
* Scan command
* Report command
* Version command
* JSON loading support

### v0.4

* Doctor command
* Environment diagnostics
* Environment health scoring
* Development profiles
* Profile-aware diagnostics

### v0.5

* Custom profile creation
* Profile saving
* Profile loading
* Profile listing

### v0.6

* Environment comparison
* Environment diff reports

### v0.7

* Export profiles
* Import profiles

### v1.0

* Environment recreation
* Apply engine
* One-command machine setup

---

## Long-Term Vision

Infrastructure as Code manages servers.

DevSetup aims to manage developer machines.

A developer should be able to move to a completely new machine and restore their workflow with minimal effort.

Future workflow:

```bash
devsetup scan

devsetup export work

devsetup apply work
```

---

## Why DevSetup?

Setting up a new development machine often requires:

* Installing runtimes
* Installing package managers
* Configuring tools
* Remembering versions
* Rebuilding workflows

DevSetup aims to automate and standardize that process.

---

## Contributing

DevSetup is currently under active development.

Suggestions, bug reports, and contributions are welcome.

---

## Author

Swastik

---

## License

MIT License
