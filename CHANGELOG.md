# Changelog

## v0.8.0

### Added

* Profile installation system
* Individual tool installation
* Individual tool scanning
* Built-in developer profiles
* Profile import
* Profile export
* Profile validation
* Dependency-aware installation
* Cross-platform command mappings
* Expanded tool database
* Installation summary reporting
* Environment rescan after installation

### Improved

* Installer architecture
* Profile management workflow
* Tool detection accuracy
* Version detection system
* CLI user experience

### Fixed

* Windows package manager integration issues
* Version command compatibility issues
* Dependency handling edge cases
* PATH-related installation verification issues

### Removed

* Doctor command (replaced by profile comparison workflow)

### Notes

DevSetup is now capable of both auditing and setting up developer environments.

This release lays the foundation for automated environment recreation in future releases.


# Changelog

## v0.7.0

### Added

* Profile import functionality
* Profile export functionality
* Built-in developer profiles
* Profile validation system
* Profile metadata support
* Health calculation helper

### Improved

* Migrated command routing to argparse
* Simplified profile comparison workflow
* Improved command structure
* Improved code organization
* Improved error handling

### Removed

* Doctor command
* Duplicate comparison logic
* Legacy command routing code

### Refactored

* Moved command logic into dedicated functions
* Simplified CLI architecture
* Reduced code duplication

### Fixed

* Invalid profile imports
* Missing profile edge cases
* Empty tool list validation


## v0.6.0 - Argparse CLI & Architecture Refactor

### Added

* Profile-based environment scanning
* Environment health calculation
* Dedicated command handler functions
* Improved profile comparison workflow
* Better error handling for missing profiles

### Changed

* Migrated CLI from `sys.argv` to `argparse`
* Refactored command routing
* Simplified project structure
* Improved code organization and maintainability
* Moved default tool definitions into a dedicated module
* Updated README and project documentation

### Removed

* Legacy doctor command workflow
* Unnecessary command-routing complexity
* Redundant architecture components

### Fixed

* Safer profile loading
* More reliable handling of invalid profile names
* Reduced duplicate logic across commands

### Commands

```bash
python main.py scan
python main.py scan <profile>

python main.py report

python main.py profile list
python main.py profile create <name>
python main.py profile show <name>
python main.py profile edit <name>
python main.py profile delete <name>

python main.py version
```

---

## v0.5.0 - Custom Profiles

### Added

* Profile creation
* Profile editing
* Profile deletion
* Profile listing
* JSON-based profile storage

---

## v0.4.0 - Environment Diagnostics

### Added

* Doctor command
* Development profiles
* Environment health scoring
* Profile-aware diagnostics

---

## v0.3.0 - CLI Commands

### Added

* Scan command
* Report command
* Version command
* JSON loading support

---

## v0.2.0 - Reporting

### Added

* JSON export
* Environment reports

---

## v0.1.0 - Initial Release

### Added

* Tool detection
* Version scanning
