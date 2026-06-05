# DevSetup

DevSetup is an open-source Python CLI that scans developer environments, manages development profiles, exports configurations, and helps recreate developer setups across machines.

The long-term goal is simple:

**Move to a new machine and restore your development workflow with minimal effort.**

---

# Current Version

**v0.7.0**

---

# Features

## Environment Scanning

Scan installed development tools and generate reports.

Supported tools include:

* Python
* Git
* Pip
* Node.js
* npm
* Yarn
* pnpm
* Bun
* Docker
* Kubernetes
* Terraform
* AWS CLI
* Java
* Go
* Rust
* And many more

---

## Environment Reports

Generate a human-readable report showing:

* Total tools scanned
* Installed tools
* Missing tools

Example:

```text
DevSetup v0.7.0 Scan Report

Installed:
✔ python
✔ git
✔ node

Missing:
✘ docker
✘ kubectl
```

---

## Profile-Based Scanning

Compare your machine against a development profile.

Example:

```bash
python main.py scan webdev
```

Output:

```text
DevSetup v0.7.0 Profile Comparison

Environment Health : 75.00%
Installed : 6/8
```

---

## Built-In Profiles

DevSetup includes profiles for:

* Web Development
* Python Development
* AI Engineering
* Data Science
* DevOps
* Cloud Engineering
* Backend Development
* Frontend Development
* Mobile Development
* Cybersecurity
* Game Development
* And many more

---

## Custom Profiles

Create your own development profiles.

Example:

```bash
python main.py profile create myprofile
```

List profiles:

```bash
python main.py profile list
```

Show profile:

```bash
python main.py profile show myprofile
```

Edit profile:

```bash
python main.py profile edit myprofile
```

Delete profile:

```bash
python main.py profile delete myprofile
```

---

## Profile Export

Export profiles and share them with other developers.

Example:

```bash
python main.py profile export webdev
```

Generated:

```text
webdev_export.json
```

---

## Profile Import

Import profiles from exported JSON files.

Example:

```bash
python main.py profile import webdev_export.json
```

---

## Profile Validation

Imported profiles are automatically validated.

Validation checks:

* Required fields exist
* Tools field is a list
* Tool names are strings
* At least one tool exists

---

## JSON Environment Snapshot

Environment scans are stored as:

```text
data.json
```

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

# Commands

## Scan Environment

```bash
python main.py scan
```

---

## Scan Against Profile

```bash
python main.py scan webdev
```

---

## Report

```bash
python main.py report
```

---

## Version

```bash
python main.py version
```

---

## Profile Commands

Create:

```bash
python main.py profile create <name>
```

List:

```bash
python main.py profile list
```

Show:

```bash
python main.py profile show <name>
```

Edit:

```bash
python main.py profile edit <name>
```

Delete:

```bash
python main.py profile delete <name>
```

Export:

```bash
python main.py profile export <name>
```

Import:

```bash
python main.py profile import <file>
```

---

# Project Structure

```text
devsetup/

├── main.py
├── functions.py
├── data_manager.py
├── storage.py
├── profile_storage.py
├── profile_manager.py
├── validators.py
├── printer.py
├── default_tools.py
├── profiles/
├── VERSION
├── CHANGELOG.md
├── README.md
└── .gitignore
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/sw4tk/DevSetup.git
```

Move into the project:

```bash
cd DevSetup
```

Run:

```bash
python main.py scan
```

---

# Roadmap

## v0.8

* Environment Export
* Portable environment snapshot format
* Machine metadata support

## v0.9

* Apply Engine Foundation
* Installation planner
* Dependency resolution

## v1.0

* One-command environment recreation

Example:

```bash
devsetup export
devsetup apply
```

---

# Long-Term Vision

Infrastructure as Code manages servers.

DevSetup aims to manage developer machines.

A developer should be able to move to a completely new machine and restore their development workflow using a single command.

---

# Contributing

Suggestions, bug reports, and pull requests are welcome.

---

# Author

Swastik

---

# License

MIT License
