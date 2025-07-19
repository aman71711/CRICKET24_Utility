# Cricket 24 Auto Updater v5.0

A comprehensive utility for managing Cricket 24 game updates with enhanced visual design and modern user interface.

## Features

### 🔄 Auto Updater
- **Automatic Update Detection**: Checks for the latest Cricket 24 patches
- **Multi-threaded Downloads**: Fast concurrent downloading with pause/resume support
- **Checksum Verification**: Ensures file integrity with SHA-256 verification
- **Smart Installation**: Automatic extraction and installation of updates
- **Host Failover**: Multiple download sources for reliability

### 🛡️ File Verifier
- **Complete Game Verification**: Validates all game files against checksums
- **Detailed Reports**: Identifies missing, corrupted, and extra files
- **Export Capabilities**: Save verification reports for troubleshooting
- **Real-time Progress**: Live updates during verification process

### 🔧 Utilities
- **Game Management**: Launch Cricket 24, backup/restore saves
- **Network Tools**: DNS management for connection issues
- **Quick Access**: Direct shortcuts to save locations and backups
- **Shortcut Creation**: Create Cricket 24 Start Menu shortcuts
- **Cache Management**: Clear download cache to free disk space

### 🩺 System Diagnostics
- **Hardware Analysis**: CPU, GPU, RAM, and disk space information
- **Crash Log Scanning**: Windows Event Log analysis for game crashes
- **DirectX Reporting**: Generate comprehensive DxDiag reports
- **Export Results**: Save diagnostic information for support

### 📄 Enhanced Logging
- **Comprehensive Logs**: Detailed application and system event logging
- **Color-coded Output**: Easy-to-read categorized log entries
- **Export & Archive**: Save logs for troubleshooting and support

## Installation

### Recommended Method (Pre-compiled Binary)
1. Download the latest `cricket24_utility_5.0.exe` from the [Releases](https://github.com/yourusername/cricket24-utility/releases) page
2. Run the executable as Administrator (recommended for full functionality)
3. No additional installation required - it's a standalone executable

### Advanced Users (Source Code)
1. Ensure you have Python 3.13+ installed
2. Install required dependencies: `pip install psutil sv-ttk py-cpuinfo WMI pywin32`
3. Run: `python cricket24_utility_5.0.py`

**Note**: The pre-compiled executable is recommended for most users as it includes all dependencies and provides the best performance.

## Requirements

- Windows 10/11
- .NET Framework 4.7.2 or higher
- Administrator privileges (recommended for full functionality)
- Internet connection for updates

## Usage

1. **Select Game Directory**: Choose your Cricket 24 installation folder
2. **Check for Updates**: Click "Check for Updates" to scan for new patches
3. **Install Updates**: Follow the on-screen prompts to download and install
4. **Verify Files**: Use the Verifier tab to check game file integrity
5. **Use Utilities**: Access various game management tools

## Technology Stack

- **Python 3.13+**: Core application logic
- **Tkinter + sv-ttk**: Modern dark-themed user interface
- **Threading**: Concurrent operations and background tasks
- **PowerShell**: Windows integration and system operations
- **7-Zip**: Archive extraction and compression
- **WMI**: System information gathering

## Development Team

- **👑 XLR8** (@xlr8_boi) - Creator
- **⭐ ADITYA** (@adityaberchha) - Developer
- **🤝 Begula** (@belugaaaaaaaaaaaaa) - Contributor

## Version History

### v5.0 (Phoenix Enhanced)
- Complete visual overhaul with modern theming system
- Enhanced icon consistency and visual hierarchy
- Improved layout with better spacing and alignment
- Modular theme management with multiple color schemes
- Optimized button styling and visual feedback
- Enhanced clear cache functionality with better UX

### Previous Versions
- v4.x: Enhanced network tools and diagnostics
- v3.x: Multi-threaded downloads and verification
- v2.x: Basic update functionality
- v1.x: Initial release

## Contributing

We welcome contributions! Please feel free to:
- Report bugs and issues
- Suggest new features
- Submit pull requests
- Improve documentation

## Support

- **Discord Community**: [Join our Discord](https://discord.gg/5gWWv3ar)
- **Issues**: Report bugs on our [GitHub Issues](https://github.com/yourusername/cricket24-utility/issues) page
- **Documentation**: Check our [Wiki](https://github.com/yourusername/cricket24-utility/wiki) for detailed guides

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is not affiliated with or endorsed by the official Cricket 24 developers. Use at your own risk. Always backup your save files before making changes.

---

Made with ❤️ by the Cricket 24 Community
