# DevSetup

DevSetup is a lightweight open-source CLI tool that scans a developer's machine and compares it against predefined development profiles.

It helps developers quickly understand:

* What tools are installed
* What tools are missing
* How their environment matches a development role

---

# Current Version

**v0.7.0**

---

# Core Idea

Instead of manually checking tools one by one, DevSetup lets you define or use a **development profile** and instantly compare your system against it.

Example:

```bash
devsetup scan webdev
```

---

# Features

## Environment Scanning

DevSetup scans your system and detects installed development tools.

Supported tools include:

* Python
* Git
* Node.js
* npm
* Docker
* Java
* Go
* Rust
* Kubernetes tools
* Cloud CLIs

---

## Profile-Based Environment Comparison

Compare your system with a predefined profile.

Example:

```bash
devsetup scan webdev
```

Output:

* Installed tools
* Missing tools
* Environment health score

---

## Built-in Profiles

DevSetup ships with ready-to-use profiles:

* webdev
* python
* ai
* data-science
* devops
* backend
* frontend
* mobile
* cloud
* cybersecurity

---

## Custom Profiles

Create your own environment profiles.

### Create Profile

```bash
devsetup profile create myprofile
```

### List Profiles

```bash
devsetup profile list
```

### Show Profile

```bash
devsetup profile show myprofile
```

### Edit Profile

```bash
devsetup profile edit myprofile
```

### Delete Profile

```bash
devsetup profile delete myprofile
```

---

## Profile Import / Export

Share profiles between machines or developers.

### Export Profile

```bash
devsetup profile export webdev
```

Output:

```text
webdev_export.json
```

### Import Profile

```bash
devsetup profile import webdev_export.json
```

Imported profiles are automatically validated before saving.

---

## Profile Validation

All imported profiles are validated:

* Required fields exist (name, description, tools)
* Tools must be a list
* Tools must contain strings
* Must have at least one tool

---

## Environment Report

Generate a system report from stored scan data:

```bash
devsetup report
```

---

## Version

```bash
devsetup version
```

---

# Command Structure

## Scan system

```bash
devsetup scan
```

## Scan with profile comparison

```bash
devsetup scan webdev
```

## Profile management

```bash
devsetup profile <action>
```

Actions:

* list
* create
* show
* edit
* delete
* import
* export

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
└── README.md
```

---

# Roadmap

## v0.7.0 (Current)

* Profile scanning system
* Profile import/export
* Built-in profiles
* Clean argparse CLI
* Removed unnecessary features

## v0.8.0

* UI/UX improvements in CLI output
* Better formatting and readability
* Faster scanning engine

## v0.9.0

* Apply engine (environment installer foundation)
* Dependency resolution system
* Safe installation planning

## v1.0.0

* Full environment recreation system
* One-command setup:

  ```bash
  devsetup apply webdev
  ```
* Cross-machine reproducibility

---

# Long-Term Vision

DevSetup aims to become:

> “Infrastructure as Code, but for developer machines”

A developer should be able to:

* Move to a new machine
* Run one command
* Get full working environment instantly

---

# Contributing

Contributions, ideas, and improvements are welcome.

---

# Author

Swastik

---

# License

MIT
