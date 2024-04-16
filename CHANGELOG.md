## 2024-02-12

### Changed
- Added --build-windows and --build-check flags to build scripts to allow optional skipping of Windows build and unit tests/mypy checks.

### Fixed
- Resolved issues with paho-mqtt upgrade breaking cloudadapter's mqtt connections.
- Improved error messaging for failed URL fetches.
- Addressed missing GUID when not provided by manifest for fwupdate tool.
- Fixed SOTA snapshot conditions to prevent double reboots on EXT4 systems.

### Security
- Updated cryptography to address CVE-2023-5678 and CVE-2023-6129 vulnerabilities.