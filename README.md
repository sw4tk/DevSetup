# DevSetup

DevSetup is an open-source Python CLI that helps developers scan their machines, compare them against development profiles, and install missing tools automatically.

The goal is simple:

**Set up a development environment in minutes instead of hours.**

---

# Current Version

**v0.8.0**

---

# Features

## Environment Scanning

Scan installed development tools and generate a report.

Example:

```bash
python main.py scan
```

Supported tools include:

* Python
* Git
* Node.js
* Java
* Go
* Rust
* Docker
* Kubernetes
* Terraform
* AWS CLI
* Azure CLI
* GCP CLI
* MongoDB
* PostgreSQL
* Redis
* Yarn
* pnpm
* Bun
* And many more

---

## Profile-Based Scanning

Compare your machine against a development profile.

Example:

```bash
python main.py scan webdev
```

Output:

```text
Environment Health : 80.00%
Installed : 8/10
```

---

## Built-In Profiles

DevSetup ships with developer profiles including:

* Web Development
* Frontend Development
* Backend Development
* Full Stack Development
* Python Development
* AI Engineering
* Data Science
* Machine Learning
* DevOps
* SRE
* Cloud Engineering
* Cybersecurity
* Docker
* Kubernetes
* Java
* Go
* Rust
* PHP
* Ruby
* PostgreSQL
* MongoDB
* Automation
* Database Engineering

and more.

---

## Custom Profiles

Create your own profiles.

Create:

```bash
python main.py profile create myprofile
```

List:

```bash
python main.py profile list
```

Show:

```bash
python main.py profile show myprofile
```

Edit:

```bash
python main.py profile edit myprofile
```

Delete:

```bash
python main.py profile delete myprofile
```

---

## Profile Export

Export profiles for sharing.

Example:

```bash
python main.py profile export webdev
```

Output:

```text
webdev_export.json
```

---

## Profile Import

Import profiles from JSON files.

Example:

```bash
python main.py profile import webdev_export.json
```

Imported profiles are automatically validated before being stored.

---

## Profile Validation

DevSetup validates imported profiles.

Checks include:

* Required fields exist
* Valid profile structure
* Tool list validation
* Invalid data rejection

---

## Tool Installation

Install missing tools from a profile automatically.

Example:

```bash
python main.py install webdev
```

DevSetup will:

1. Scan the current machine
2. Detect missing tools
3. Ask for confirmation
4. Install supported tools
5. Rescan the environment

Example:

```text
Missing:
- git
- node

Install missing tools? (y/n)
```

---

## Individual Tool Installation

Install a specific tool directly.

Example:

```bash
python main.py install-tool git
```

Supported package managers:

### Windows

* Winget

### Linux

* Apt
* DNF
* Pacman (planned)

### macOS

* Homebrew

---

# Commands

## Scan Environment

```bash
python main.py scan
```

---

## Scan Profile

```bash
python main.py scan webdev
```

---

## Install Profile

```bash
python main.py install webdev
```

---

## Install Single Tool

```bash
python main.py install-tool git
```

---

## Generate Report

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

```bash
python main.py profile create <name>
python main.py profile list
python main.py profile show <name>
python main.py profile edit <name>
python main.py profile delete <name>
python main.py profile export <name>
python main.py profile import <file>
```

---

# Project Structure

```text
devsetup/

├── main.py
├── functions.py
├── data_manager.py
├── installer.py
├── printer.py
├── validators.py
├── profile_manager.py
├── profile_storage.py
├── storage.py
├── default_tools.py
├── version_commands.py
├── tool_metadata.py
├── profiles/
├── VERSION
├── CHANGELOG.md
└── README.md
```

---

# Roadmap

## v0.8.0 (Current)

* Profile import/export
* Built-in profiles
* Environment scanning
* Profile comparison
* Automated tool installation
* Individual tool installation

## v0.9.0

* Installation reliability improvements
* Dependency handling
* Better package manager support
* Collision detection
* Installation rollback system
* Improved CLI UX

## v1.0.0

* Fully automated environment setup
* One-command profile installation
* Cross-platform installation engine
* Production-ready release
* Packaged executable

Example:

```bash
devsetup install webdev
```

---

# Long-Term Vision

DevSetup aims to become:

> Infrastructure as Code for Developer Machines

A developer should be able to:

* Move to a new machine
* Install DevSetup
* Run one command
* Get a fully configured development environment

---

# Contributing

Pull requests, bug reports, and ideas are welcome.

---

# Author

Swastik

---

# License

MIT
