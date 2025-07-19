# 📖 How to Use Cricket 24 Auto Updater v5.0

This comprehensive guide will walk you through every feature of the Cricket 24 Auto Updater to help you keep your game updated and running smoothly.

## 🚀 Quick Start Guide

### Step 1: Download and Launch
1. **Download**: Get the latest `Cricket24_Auto_Updater_v5.0.exe` from the [Releases](https://github.com/aman71711/CRICKET24_Utility/releases) page
2. **Security**: Windows may show a security warning - this is normal for new software. Click "More info" → "Run anyway"
3. **Launch**: Right-click the executable and select "Run as administrator" (recommended for full functionality)

### Step 2: First Time Setup
1. **Select Game Directory**: Click the 📁 folder icon next to "Game Directory"
2. **Navigate**: Find your Cricket 24 installation folder (usually `C:\Program Files\Steam\steamapps\common\Cricket 24\`)
3. **Confirm**: Click "Select Folder" - the tool will verify it contains `cricket24.exe`

### Step 3: Check for Updates
1. **Click "Check for Updates"** in the main tab
2. **Wait**: The tool will connect to update servers and scan for new patches
3. **Review**: Any available updates will be displayed with version information

---

## 📑 Detailed Feature Guide

### 🔄 Auto Updater Tab

#### Checking for Updates
- **Purpose**: Scans for the latest Cricket 24 patches and updates
- **How to Use**:
  1. Ensure you have selected your Cricket 24 game directory
  2. Click **"🔍 Check for Updates"**
  3. Wait for the scan to complete (usually 10-30 seconds)
  4. Review any found updates in the status area

#### Installing Updates
- **When Updates Found**:
  1. Click **"⬇️ Download & Install Updates"**
  2. **Monitor Progress**: Watch the progress bar and download speed
  3. **Pause/Resume**: Use the "⏸️ Pause" button if needed
  4. **Wait for Completion**: Installation happens automatically after download

#### Download Management
- **Pause/Resume**: Click the pause button during downloads to pause, click again to resume
- **Cancel**: Use the "❌ Cancel" button to stop downloads (partial files are saved for later resume)
- **Speed Info**: Monitor download speed and ETA in real-time
- **Multiple Sources**: The tool automatically switches between download mirrors for best speed

---

### 🛡️ File Verifier Tab

#### Basic File Verification
- **Purpose**: Checks if your game files are corrupted or missing
- **How to Use**:
  1. Go to the **"Verifier"** tab
  2. Click **"🔍 Start Verification"**
  3. **Wait**: Verification can take 10-30 minutes depending on your system
  4. **Review Results**: See detailed report of file status

#### Understanding Verification Results
- **✅ Good Files**: Files that passed verification
- **❌ Corrupted Files**: Files that failed checksum verification
- **⚠️ Missing Files**: Files that should exist but don't
- **📁 Extra Files**: Files that shouldn't be there
- **🔒 Unreadable Files**: Files that couldn't be accessed

#### Verification Reports
- **Export Report**: Click **"📤 Export Report"** to save results to a text file
- **Save Location**: Reports are saved to your Desktop with timestamp
- **Use for Support**: Share these reports when asking for help on Discord

---

### 🔧 Utilities Tab

#### Game Management
- **🎮 Launch Cricket 24**: 
  - Starts the game directly from the updater
  - Automatically uses the correct game directory
  - Shows error if game files are missing

- **💾 Backup Saves**:
  - Creates a zip backup of your save files
  - Saves to `Documents\Cricket 24 Backups\`
  - Files are named with current date/time

- **⬆️ Restore Backup**:
  - Select a backup zip file to restore
  - **WARNING**: This overwrites your current saves
  - Always backup current saves before restoring

#### Quick Access Tools
- **📁 Open Save Location**: Opens your Cricket 24 save folder in Windows Explorer
- **📂 Open Backup Folder**: Opens the folder containing your save backups
- **🔗 Create Cricket 24 Shortcut**: Adds Cricket 24 to your Start Menu for easy access

#### Network Tools
- **🌐 Flush DNS Cache**: 
  - Clears Windows DNS cache
  - Useful if you have connection issues
  - Requires administrator privileges

- **📋 Copy Network Info**: Copies your network configuration to clipboard for support

#### Cache Management
- **🧹 Clear Download Cache**: 
  - Removes all downloaded update files
  - Frees up disk space (can be several GB)
  - **Safe to use**: Downloads can be resumed later if needed

---

### 🩺 Diagnostics Tab

#### System Information
- **📊 Basic Scan**: Quick overview of CPU, RAM, disk space
- **🔍 Full Scan**: Comprehensive system analysis (takes 2-3 minutes)
- **Export Results**: Save diagnostic info for troubleshooting

#### Crash Log Analysis
- **📋 Scan Event Logs**: 
  - Searches Windows Event Log for Cricket 24 crashes
  - Requires administrator privileges for full access
  - Results show crash times and error codes

#### DirectX Diagnostics
- **🎮 Generate DxDiag**: 
  - Creates comprehensive DirectX report
  - Useful for graphics-related issues
  - Takes 1-2 minutes to complete

---

## ⚠️ Troubleshooting Guide

### Common Issues and Solutions

#### "Game Directory Not Found"
- **Problem**: Selected folder doesn't contain `cricket24.exe`
- **Solution**: 
  1. Navigate to your actual Cricket 24 installation
  2. Look for the folder containing `cricket24.exe`
  3. Common locations:
     - `C:\Program Files\Steam\steamapps\common\Cricket 24\`
     - `C:\Program Files (x86)\Steam\steamapps\common\Cricket 24\`
     - Custom Steam library locations

#### "No Updates Available"
- **Problem**: Tool says no updates but you think there should be
- **Solutions**:
  1. Check your internet connection
  2. Try **"🔄 Refresh"** button
  3. Clear DNS cache using the Network Tools
  4. Check Discord for server status

#### "Download Failed"
- **Problem**: Downloads keep failing or stopping
- **Solutions**:
  1. Check your internet connection stability
  2. Try pausing and resuming the download
  3. Clear download cache and try again
  4. Check if antivirus is blocking the download

#### "Verification Finds Many Corrupted Files"
- **Problem**: Verification reports many corrupted files
- **Solutions**:
  1. **If recently updated**: This is normal, files are being replaced
  2. **If game won't start**: Run Steam's "Verify Integrity of Game Files"
  3. **If problems persist**: Consider a clean reinstall of Cricket 24

#### "Permission Denied" Errors
- **Problem**: Tool can't access files or perform operations
- **Solutions**:
  1. **Always run as Administrator**: Right-click → "Run as administrator"
  2. Check that Cricket 24 is not running
  3. Ensure antivirus isn't blocking the tool
  4. Check file permissions on game directory

---

## 🛠️ Advanced Features

### Background Operations
- **Multi-threading**: Downloads use multiple connections for speed
- **Automatic Retry**: Failed downloads retry automatically
- **Resume Support**: Interrupted downloads can be resumed
- **Checksum Verification**: All files verified for integrity

### Logging and Debugging
- **📄 View Logs**: Check `cricket24_updater.log` for detailed operation logs
- **Log Levels**: Different types of messages (INFO, WARNING, ERROR)
- **Export Logs**: Save logs for support requests

### Command Line Usage
The tool can be started with specific directories:
```cmd
Cricket24_Auto_Updater_v5.0.exe "C:\Path\To\Cricket24"
```

---

## 🔒 Security Information

### Windows Security Warnings
- **SmartScreen Warning**: Windows may warn about "unrecognized app"
- **Why This Happens**: New executables aren't immediately trusted by Windows
- **Safe to Run**: The tool is clean and safe - click "More info" → "Run anyway"

### Administrator Privileges
- **When Required**: For DNS cache clearing, event log scanning, and some file operations
- **Why Required**: Windows restricts these operations to prevent malware
- **Always Safe**: The tool only modifies Cricket 24 related files and Windows cache

### Antivirus Compatibility
- **False Positives**: Some antivirus software may flag the tool
- **Add Exception**: Add the executable to your antivirus whitelist
- **Safe Downloads**: All game files are verified with checksums before installation

---

## 📞 Getting Help

### Before Asking for Help
1. **Check this guide** for your specific issue
2. **Check the logs** in `cricket24_updater.log`
3. **Try basic troubleshooting** (restart, run as admin, check internet)

### Where to Get Support
- **💬 Discord Community**: [Join our Discord](https://discord.gg/5gWWv3ar)
  - Fastest response time
  - Community help available
  - Share screenshots and logs easily

- **🐛 GitHub Issues**: [Report bugs here](https://github.com/aman71711/CRICKET24_Utility/issues)
  - For technical bugs and feature requests
  - Include logs and system information
  - Check existing issues first

### Information to Include When Asking for Help
1. **What you were trying to do**
2. **What went wrong (exact error message)**
3. **Your system info** (Windows version, game location)
4. **Log file contents** (recent entries from `cricket24_updater.log`)
5. **Screenshots** if applicable

---

## 📊 Performance Tips

### For Faster Downloads
- **Close other internet applications** during downloads
- **Use wired connection** instead of WiFi when possible
- **Pause/resume** if speeds are slow - sometimes helps switch servers

### For Better Performance
- **Run as Administrator** for full functionality
- **Close Cricket 24** before updating
- **Free up disk space** if you have less than 5GB available
- **Update Windows** to ensure compatibility

### Disk Space Management
- **Clear cache regularly** using the Cache Management tool
- **Archive old backups** - you don't need to keep all save backups
- **Monitor space** - updates can be 1-3GB each

---

## ❓ Frequently Asked Questions

### Q: Do I need to keep the executable file?
**A:** Yes, keep it somewhere permanent. It's a portable application - no installation required.

### Q: Can I move my Cricket 24 installation?
**A:** Yes, just select the new directory in the tool. Your saves are stored separately.

### Q: Will this work with pirated copies?
**A:** This tool is designed for legitimate Steam copies only. We don't support pirated versions.

### Q: Can I use this with mods?
**A:** Yes, but verify your files before updating to ensure mods don't cause conflicts.

### Q: How often should I check for updates?
**A:** Check weekly, or whenever you experience game issues. Updates fix bugs and add features.

### Q: Is my save data safe?
**A:** Yes, updates don't affect save data. But it's always good to backup saves regularly.

---

**💡 Pro Tip**: Join our Discord community for the latest updates, tips, and help from other Cricket 24 players!

---

*Last Updated: January 2025 | Version 5.0*
