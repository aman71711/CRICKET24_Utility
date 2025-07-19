# 🖼️ Visual User Guide

This visual guide describes the interface and what you should expect to see when using Cricket 24 Auto Updater v5.0.

## 📥 Getting Started

### Step 1: Download and Launch
**What you'll see:**
- GitHub Releases page with download links
- File name: `Cricket24_Auto_Updater_v5.0.exe` (approximately 17 MB)
- Windows may show a blue "Windows protected your PC" warning
- Click "More info" → "Run anyway" to proceed

### Step 2: First Launch
**Application Window:**
- **Title**: "Cricket 24 Auto Updater v5.0"
- **Theme**: Dark professional theme with blue accents
- **Size**: Opens at 1200x900 pixels (resizable)
- **Icon**: Cricket-themed icon in taskbar and title bar

### Step 3: Select Game Directory
**Interface Elements:**
- **Game Directory Field**: Shows "No directory selected" initially
- **📁 Browse Button**: Click to open folder selection dialog
- **Target Folder**: Look for folder containing `cricket24.exe`
- **Validation**: Green checkmark appears when valid directory is selected

---

## 🔄 Auto Updater Tab

### Main Interface Layout
**Tab Structure:**
```
[🔄 Auto Updater] [🛡️ Verifier] [🔧 Utilities] [🩺 Diagnostics]
```

**Main Controls:**
- **🔍 Check for Updates** (blue button) - Primary action button
- **⬇️ Download & Install** (appears when updates found)
- **⏸️ Pause / ▶️ Resume** (during downloads)
- **❌ Cancel** (stops current operation)

### Checking for Updates
**Status Messages You'll See:**
- "🔍 Checking for updates..."
- "📡 Connecting to update servers..."
- "✅ Found X updates available"
- "ℹ️ Your game is up to date"

### Download Progress
**Progress Display:**
- **Progress Bar**: Blue bar showing percentage (0-100%)
- **Speed**: "Download Speed: 15.2 MB/s"
- **ETA**: "Time Remaining: 2m 15s"
- **File**: "Downloading: C24_Update_5362_to_5385.zip"
- **Overall**: "Downloading Update 1 of 2"

### Installation Complete
**Success Screen:**
- ✅ Green checkmark icon
- "🎉 Update completed successfully!"
- "Your Cricket 24 is now updated to version X"
- Option to launch the game immediately

---

## 🛡️ File Verifier Tab

### Verification Interface
**Layout Description:**
- **🔍 Start Verification** (large blue button)
- **Progress Area**: Shows file currently being checked
- **Statistics Panel**: Counts of good/bad/missing files
- **Results Area**: Scrollable list of file issues

### Verification in Progress
**What You'll See:**
- **Current File**: "Checking: data/graphics/stadium_01.pak"
- **Progress**: "Processed 1,250 of 8,543 files (14.6%)"
- **Live Counters**:
  - ✅ Good: 1,200 files
  - ❌ Corrupted: 3 files
  - ⚠️ Missing: 1 file

### Verification Results
**Results Display:**
```
📊 Verification Complete:
✅ Good Files: 8,539 (99.95%)
❌ Corrupted Files: 3 (0.04%)
⚠️ Missing Files: 1 (0.01%)
📁 Extra Files: 0

Issues Found:
❌ data/audio/crowd_cheer.wav - Checksum mismatch
⚠️ data/config/settings.ini - File missing
```

---

## 🔧 Utilities Tab

### Utilities Overview
**Section Layout:**
```
┌─ Game Management ────────────────┐
│ 🎮 Launch Cricket 24             │
│ 💾 Backup Saves                  │
│ ⬆️ Restore Backup               │
└─────────────────────────────────┘

┌─ Quick Access ──────────────────┐
│ 📁 Open Save Location           │
│ 📂 Open Backup Folder           │
│ 🔗 Create Cricket 24 Shortcut   │
└─────────────────────────────────┘

┌─ Network Tools ─────────────────┐
│ 🌐 Flush DNS Cache              │
│ 📋 Copy Network Info            │
└─────────────────────────────────┘

┌─ Cache Management ──────────────┐
│ 🧹 Clear Download Cache         │
└─────────────────────────────────┘
```

### Save Backup Process
**Backup Dialog:**
- Shows save location: `C:\Users\[Name]\Saved Games\Cricket 24`
- Backup destination: `C:\Users\[Name]\Saved Games\Cricket 24 Backups`
- Progress: "Creating backup... Cricket24_Save_2025-01-19_14-30-25.zip"
- Success: "✅ Backup created successfully: 2.4 MB"

### Network Tools
**DNS Flush Result:**
- "🌐 Flushing DNS cache..."
- "✅ DNS cache cleared successfully"
- "ℹ️ This may help resolve connection issues"

---

## 🩺 Diagnostics Tab

### System Diagnostics
**Information Display:**
```
🖥️ System Information:
   OS: Windows 11 Pro (Build 26100)
   CPU: Intel Core i7-12700K @ 3.60GHz
   RAM: 32.0 GB
   GPU: NVIDIA GeForce RTX 4070 (Driver: 551.23)

💾 Disk Space:
   C: Drive: 245 GB free of 500 GB
   Game Drive: 1.2 TB free of 2.0 TB

🎮 Game Information:
   Version: 5.385
   Install Size: 45.2 GB
   Last Updated: 2025-01-15
```

### Crash Log Analysis
**Event Log Results:**
```
🔍 Scanning Windows Event Logs...

📅 Recent Cricket 24 Events:
   2025-01-19 14:25:32 - Application Error (ID: 1000)
   2025-01-18 09:15:41 - Application Hang (ID: 1002)
   2025-01-17 16:45:12 - Application Error (ID: 1000)

📋 Analysis:
   Total crashes in last 7 days: 3
   Most common error: Application Error (1000)
   Recommendation: Update graphics drivers
```

---

## ⚠️ Common Scenarios

### Windows Security Warning
**SmartScreen Dialog:**
```
🛡️ Windows protected your PC
   Microsoft Defender SmartScreen prevented 
   an unrecognized app from starting.

   App: Cricket24_Auto_Updater_v5.0.exe
   Publisher: Unknown Publisher

   [Run anyway] [Don't run]
```
**Action**: Click "More info" then "Run anyway"

### Administrator Prompt (UAC)
**User Account Control:**
```
🔑 Do you want to allow this app to make 
    changes to your device?

    Cricket24_Auto_Updater_v5.0.exe
    Unknown Publisher

    [Yes] [No]
```
**Action**: Click "Yes" for full functionality

### Error Messages
**Common Errors You Might See:**

**Connection Error:**
```
❌ Connection Failed
Unable to connect to update servers.
Please check your internet connection.
[Retry] [Cancel]
```

**Permission Error:**
```
⚠️ Permission Denied
Cannot access game directory. Please run 
as Administrator or check folder permissions.
[OK]
```

**Invalid Directory:**
```
🚫 Invalid Game Directory
Selected folder does not contain cricket24.exe
Please select the correct Cricket 24 installation folder.
[OK]
```

---

## 🎨 Interface Design

### Color Scheme
- **Background**: Dark gray (#1a1a1a)
- **Text**: White and light gray
- **Accent**: Microsoft Blue (#0078d4)
- **Success**: Green (#16a085)
- **Warning**: Orange (#f39c12)
- **Error**: Red (#e74c3c)

### Typography
- **Titles**: Segoe UI, 20pt, Bold
- **Body Text**: Segoe UI, 10pt, Regular
- **Buttons**: Segoe UI, 10pt, Bold
- **Code/Logs**: Consolas, 9pt, Regular

### Icons and Emojis
The interface uses Unicode emojis for cross-platform compatibility:
- 🔍 Search/Check for updates
- ⬇️ Download
- ✅ Success/Verified
- ❌ Error/Failed
- ⚠️ Warning
- 🔧 Tools/Utilities
- 🛡️ Security/Verification

---

**Note**: This text-based visual guide describes exactly what you'll see in the application. The interface follows modern Windows design principles with dark theming and intuitive controls.
