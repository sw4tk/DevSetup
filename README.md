
# DevSetup

> **Infrastructure as Code for Developer Machines**

DevSetup is an open-source Python CLI that scans developer environments, compares them against reusable development profiles, and installs missing tools automatically.

Instead of manually installing Git, Python, Node.js, Docker, databases, cloud CLIs, and other developer tools every time you switch machines, DevSetup lets you recreate your entire development environment with a single command.

---

## Current Version

**v1.0.0**

---

## Features

### Project Environment Workflow

Create project-specific environment files similar to `package.json`, but for your machine.

```bash
devsetup init
````

Creates:

```
.devsetup.json
```

Synchronize your local environment:

```bash
devsetup sync
```

---

### Environment Scan

Audit your current machine.

```bash
devsetup scan
```

Shows:

* Installed tools
* Missing tools
* Versions
* Categories
* Environment health

---

### Profile Scan

Compare your environment against a development profile.

```bash
devsetup scan webdev
```

Displays:

* Match percentage
* Missing tools
* Missing categories
* Environment compatibility

---

### Install Development Profiles

Automatically install everything required for a profile.

```bash
devsetup install webdev
```

Supports:

* Version-aware installations
* Dependency handling
* Installation planning
* Installation summaries

---

### Install Individual Tools

```bash
devsetup install-tool git
```

Uses the native package manager:

* Windows → Winget
* macOS → Homebrew
* Linux → Apt

---

### Profile Management

```bash
devsetup profile list

devsetup profile show webdev

devsetup profile export webdev

devsetup profile export webdev --freeze

devsetup profile import profile.json
```

Frozen profiles pin every tool to an exact version, making environments fully reproducible.

---

## Built-in Profiles

DevSetup includes ready-to-use profiles for:

* Web Development
* Python Development
* AI Engineering
* Data Science
* DevOps
* Cloud Engineering
* Docker & Kubernetes
* Database Engineering

and more.

---

## Roadmap

### v1.0.0

* Rich terminal UI
* Project initialization
* Environment synchronization
* Frozen profile exports
* Cross-platform installation
* Health dashboard

### v1.1.0

* Installation rollback
* DNF support
* Pacman support
* Custom registries
* Plugin system

### Long-Term Vision

DevSetup aims to become the **Infrastructure as Code** solution for developer workstations.

A developer should be able to:

1. Buy a new computer.
2. Install DevSetup.
3. Run a single command.

Their entire development environment should be restored automatically.

---

## Author

Swastik Mandal

---

## License

MIT License

```
```
