# 🏏 CRICKET24_Utility
**Cricket 24 Auto Updater v1.3 **  
Made by **XLR8**

A powerful, user-friendly GUI tool to automatically update your Cricket 24 installation to the latest version. Forget manual patching — this app handles detection, downloading, backup, installation, and launching in one smooth flow.

---

## 🚀 Features
- ✅ **Automatic Version Detection** – Reads your current version from `version.txt`
- ✅ **Smart Update Chain** – Downloads only the updates you need
- ✅ **Supports ZIP / RAR / 7Z** – Local and automatic installs from archive formats
- ✅ **Built-in Archive Support** – No need to install external tools like 7-Zip or NanaZip
- ✅ **Fast Retry System** – Auto-retry downloads (up to 5 attempts with exponential backoff)
- ✅ **Progress Tracking** – Real-time progress bar, status updates, and download speed
- ✅ **Dark/Light Theme Toggle** – Choose your preferred viewing mode
- ✅ **Game Backup System** – Auto-backups saved games before patching
- ✅ **Manual Update Option** – Install updates from local ZIP/RAR/7Z files
- ✅ **SHA256 Checksum Toggle** – Optional file integrity verification
- ✅ **Launch Game Post-Update** – One-click Cricket 24 launch from the app
- ✅ **Logging System** – Error logging, debug info, exportable logs

---

## 📁 Key Directories
- 🗂️ **Game Folder**: Where `cricket24.exe` is located
- 💾 **Saved Games**: Usually `~/Saved Games/Cricket 24`
- 🛡️ **Backups**: `~/Saved Games/Cricket 24 Backups`

---

## 🔧 Manual Update Support
Install `.zip`, `.rar`, or `.7z` update packages manually via the GUI.

---

## 🧪 Checksum Verification (Optional)
- Enabled by default (recommended)
- Can be toggled off from the interface
- Ensures file integrity using SHA256 hashes before installation

---

## 🎨 GUI Overview
### Main Tab
- Select Game Directory
- View Current & Target Versions
- List of Required Updates
- Check for Updates, Start Update, Cancel
- Progress Bar, Status Labels, Launch Game

### Logs Tab
- View operation logs
- Export logs
- Clear log history
- Debug failed updates

---

## 💡 How It Works
1. **Detects version.txt** in your game folder.
2. **Checks update path** between your version and the latest.
3. **Downloads only needed patches** from Pixeldrain.
4. **Backs up saved games** (optional).
5. **Verifies file hash** if enabled.
6. **Extracts and installs** automatically using built-in archive support.
7. **Updates version.txt** and allows you to launch the game.

---

## ❗ Troubleshooting
**"version.txt not found"**
- Check if the selected folder contains `cricket24.exe`.

**"Download failed after 5 attempts"**
- Try again later or check your connection.
- Join our Discord for mirror links.

**"Archive extraction failed"**
- Ensure the downloaded file is not corrupted.
- Try downloading the update again.

**Game won't launch**
- Check game directory
- Ensure `cricket24.exe` exists
- Try running as administrator

---

## 📞 Get Help or Join the Community
💬 [Join our Discord](https://discord.gg/fqWvraDg)

We help with:
- Installation issues
- Update failures
- Feature suggestions
- Community patches

---

© 2024 XLR8 | Cricket24 Auto Updater Project
