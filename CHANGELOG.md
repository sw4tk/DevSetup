
# Changelog

All notable changes to DevSetup are documented here.

---

# v1.0.0

## Added

### Rich Terminal UI

- Complete UI redesign using Rich
- Semantic color system
- Minimal tables
- Panels
- Dynamic loaders
- Installation summaries
- Environment dashboards

### Project Workflow

- Added `devsetup init`
- Added `devsetup sync`
- Local `.devsetup.json` support

### Profile Management

- Frozen profile exports
- Version pinning
- Profile inspection
- Profile metadata

### Installation Engine

- Cross-platform installers
- Dependency-aware installation
- Installation planning
- Better subprocess handling

### User Experience

- Rich confirmation prompts
- Consistent headers
- Cleaner error rendering
- Improved progress indicators

---

## Changed

- Packaged as a global executable CLI
- Refactored architecture into service-based modules
- Unified command rendering
- Improved profile handling
- Standardized version headers

---

## Fixed

- Silent hanging during long scans
- Theme rendering inconsistencies
- Winget subprocess parsing
- Installation verification edge cases
- PATH detection issues

---

# v0.8.0

## Added

- Profile installation
- Individual tool installation
- Tool scanning
- Built-in profiles
- Profile import/export
- Dependency-aware installation
- Cross-platform package mappings
- Installation summaries

## Improved

- Installer architecture
- Version detection
- Tool detection
- Profile workflow

## Fixed

- Windows package manager integration
- Version command compatibility
- Dependency handling

## Removed

- Doctor command

---

# v0.7.0

## Added

- Profile import
- Profile export
- Built-in profiles
- Validation system
- Metadata support

## Improved

- Argparse routing
- CLI organization
- Error handling

## Removed

- Doctor command
- Legacy routing

---

# v0.6.0

## Added

- Profile scanning
- Environment health calculation
- Command handlers

## Changed

- Migrated to argparse
- Refactored architecture
- Improved maintainability

## Fixed

- Invalid profile handling

---

# v0.5.0

## Added

- Custom profiles
- Profile editing
- Profile deletion
- Profile listing

---

# v0.4.0

## Added

- Doctor command
- Development profiles
- Health scoring

---

# v0.3.0

## Added

- Scan command
- Report command
- Version command

---

# v0.2.0

## Added

- JSON export
- Environment reports

---

# v0.1.0

## Initial Release

### Added

- Tool detection
- Version scanning
```
