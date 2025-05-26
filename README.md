# CRICKET24_Utility

Cricket 24 Auto Updater v2.4
Made by XLR8
A powerful, user-friendly GUI application for automatically updating Cricket 24 to the latest version. No more manual downloads or complex installations - just select your game directory and let the updater do the rest!
🚀 Features

Automatic Version Detection - Instantly detects your current Cricket 24 version
Smart Update Chain - Only downloads updates you actually need
Multiple File Format Support - Handles ZIP, RAR, and 7z archives
Robust Download System - 5-attempt retry system with exponential backoff
Progress Tracking - Real-time download progress and speed monitoring
Dark/Light Mode - Toggle between themes for comfortable usage
Comprehensive Logging - Detailed logs for troubleshooting
Backup System - Backup your saved games before updating
Manual Install Option - Install updates from local files
Game Launcher - Launch Cricket 24 directly from the updater

📋 Supported Versions
The updater supports updates between these Cricket 24 versions:

v3451 → v3891 (4.4 GB)
v3891 → v4784 (21.8 GB)
v4784 → v4818 (254 MB)
v4818 → v4847 (247 MB)
v4847 → v4910 (139 MB)
v4910 → v4949 (98.4 MB)
v4949 → v5008 (39.6 MB)
v5008 → v5047 (39 MB)
v5047 → v5183 (181 MB)
v5183 → v5214 (38.9 MB)

Latest Version: v5214

Key Directories

Game Directory: Your Cricket 24 installation folder (contains cricket24.exe)
Saved Games: Usually located at ~/Saved Games/Cricket 24
Backups: Created at ~/Saved Games/Cricket 24 Backups

🎮 How It Works

Version Detection: Reads version.txt from your game directory
Update Planning: Calculates which updates are needed to reach the latest version
Smart Downloads: Only downloads the updates between your version and the latest
Automatic Installation: Extracts and installs updates to your game directory
Verification: Updates version information after successful installation

📱 Interface Overview
Main Tab

Game Directory Selection: Choose your Cricket 24 folder
Version Status: Shows current and target versions
Updates Required: Lists all needed updates with sizes
Progress Tracking: Real-time download/install progress
Control Buttons: Check, Update, Cancel, and Launch

Logs Tab

Application Logs: Detailed operation history
Log Management: Refresh, clear, or save logs
Troubleshooting: Error tracking and debugging info

🔧 Advanced Features
Backup System

Automatically timestamps backups
Creates ZIP archives of saved games
Stores in dedicated backup folder
One-click restore capability

Manual Installation

Install updates from local ZIP/RAR/7z files
Useful for offline updates or custom patches
Same extraction logic as automatic updates

Logging System

Comprehensive operation logging
Error tracking and debugging
Exportable log files
Performance monitoring

🎨 Customization
Dark Mode

Toggle between light and dark themes
Comfortable viewing in any lighting
Saves preference during session

Theme Settings

Modern, clean interface
Responsive design
Progress indicators and status updates

🚨 Troubleshooting
Common Issues
"version.txt not found"

Ensure you've selected the correct Cricket 24 directory
The directory should contain cricket24.exe

"Download failed after 5 attempts"

Check your internet connection
Try again later (server might be busy)
Join our Discord for alternative download links

"7-Zip required for RAR/7z extraction"

Install 7-Zip from the official website
Restart the updater after installation

Game won't launch

Verify game directory is correct
Check if cricket24.exe exists
Run as administrator if needed

Getting Help
If you encounter any issues:
🔗 Join our Discord for support: https://discord.gg/fqWvraDg
Our community is ready to help with:

Installation problems
Update failures
General questions
Feature requests
