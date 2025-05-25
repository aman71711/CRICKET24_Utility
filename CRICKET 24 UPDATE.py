import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import subprocess
import shutil
import zipfile
import tempfile
import threading
from pathlib import Path
import time
import requests

class Cricket24Updater:
    def __init__(self, root):
        self.root = root
        self.root.title("Cricket 24 Auto Updater v2.1")
        self.root.geometry("700x600")
        self.root.resizable(True, True)
        
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Variables
        self.game_dir = tk.StringVar()
        self.current_version = ""
        self.selected_file = ""
        self.downloading = False
        self.cancel_download = False
        
        # Update data
        self.versions = ["3451", "3891", "4784", "4818", "4847", "4910", "4949", "5008", "5047", "5183", "5214"]
        self.latest_version = "5214"
        
        # Download links
        self.pixeldrain_links = {
            "3451_3891": "https://pixeldrain.com/u/wdvkRfUa",
            "3891_4784": "https://pixeldrain.com/u/LyNTkxck",
            "4784_4818": "https://pixeldrain.com/u/LyNTkxck",
            "4818_4847": "https://pixeldrain.com/u/JyFpA3Q8",
            "4847_4910": "https://pixeldrain.com/u/RXukPLnB",
            "4910_4949": "https://pixeldrain.com/u/bRVganvC",
            "4949_5008": "https://pixeldrain.com/u/tXs5d5Px",
            "5008_5047": "https://pixeldrain.com/u/vfnY8JNb",
            "5047_5183": "https://pixeldrain.com/u/XwpN5hfe",
            "5183_5214": "https://pixeldrain.com/u/TJXex7Cb"
        }
        
        self.update_sizes = {
            "3451_3891": "Standard",
            "3891_4784": "21.8 GB",
            "4784_4818": "254 MB",
            "4818_4847": "Standard",
            "4847_4910": "Standard",
            "4910_4949": "Standard",
            "4949_5008": "Standard",
            "5008_5047": "Standard",
            "5047_5183": "Standard",
            "5183_5214": "Standard"
        }
        
        self.create_widgets()
    
    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="15")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text="Cricket 24 Auto Updater v2.1", 
                              font=('Arial', 18, 'bold'))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Game directory selection
        dir_frame = ttk.LabelFrame(main_frame, text="Game Directory", padding="10")
        dir_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 15))
        
        ttk.Entry(dir_frame, textvariable=self.game_dir, width=60).grid(row=0, column=0, padx=(0, 10))
        ttk.Button(dir_frame, text="Browse", command=self.select_game_dir).grid(row=0, column=1)
        
        # Version display
        version_frame = ttk.LabelFrame(main_frame, text="Version Status", padding="10")
        version_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 15))
        
        self.version_label = ttk.Label(version_frame, text="Current Version: Not detected", 
                                     font=('Arial', 11, 'bold'))
        self.version_label.grid(row=0, column=0, sticky=tk.W)
        
        # Updates needed display
        updates_frame = ttk.LabelFrame(main_frame, text="Updates Required", padding="10")
        updates_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 15))
        
        self.updates_text = tk.Text(updates_frame, height=8, width=70, wrap=tk.WORD)
        scrollbar = ttk.Scrollbar(updates_frame, orient="vertical", command=self.updates_text.yview)
        self.updates_text.configure(yscrollcommand=scrollbar.set)
        self.updates_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.updates_text.insert(tk.END, "Click 'Check for Updates' to see required updates...")
        self.updates_text.config(state='disabled')
        
        # Progress
        progress_frame = ttk.LabelFrame(main_frame, text="Progress", padding="10")
        progress_frame.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 15))
        
        self.progress = ttk.Progressbar(progress_frame, mode='determinate')
        self.progress.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        self.status_label = ttk.Label(progress_frame, text="Select game directory to begin")
        self.status_label.grid(row=1, column=0, sticky=tk.W)
        
        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=5, column=0, columnspan=3, pady=(15, 0))
        
        self.check_button = ttk.Button(button_frame, text="Check for Updates", 
                                     command=self.check_updates)
        self.check_button.pack(side=tk.LEFT, padx=(0, 10))
        
        self.update_button = ttk.Button(button_frame, text="Start Update", 
                                      command=self.start_update, state='disabled')
        self.update_button.pack(side=tk.LEFT, padx=(0, 10))
        
        self.cancel_button = ttk.Button(button_frame, text="Cancel", 
                                      command=self.cancel_update, state='disabled')
        self.cancel_button.pack(side=tk.LEFT, padx=(0, 10))
        
        ttk.Button(button_frame, text="Exit", command=self.root.quit).pack(side=tk.LEFT)
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(3, weight=1)
        updates_frame.columnconfigure(0, weight=1)
        updates_frame.rowconfigure(0, weight=1)

    def select_game_dir(self):
        """Handle directory selection"""
        directory = filedialog.askdirectory(title="Select Cricket 24 Game Directory")
        if directory:
            self.game_dir.set(directory)
            self.check_version()

    def check_version(self):
        """Check current game version"""
        game_path = self.game_dir.get()
        if not game_path:
            return
        
        version_file = os.path.join(game_path, "version.txt")
        if not os.path.exists(version_file):
            self.version_label.config(text="Current Version: version.txt not found!")
            self.status_label.config(text="Error: version.txt not found in selected directory")
            return
        
        try:
            with open(version_file, 'r') as f:
                version_line = f.read().strip()
            
            parts = version_line.split('.')
            if len(parts) >= 3:
                self.current_version = parts[2].split()[0]  # Get version number
                self.version_label.config(text=f"Current Version: v{self.current_version}")
                self.status_label.config(text="Version detected successfully")
            else:
                self.version_label.config(text="Current Version: Invalid format")
                self.status_label.config(text="Error: Invalid version format in version.txt")
        except Exception as e:
            self.version_label.config(text="Current Version: Read error")
            self.status_label.config(text=f"Error reading version.txt: {str(e)}")

    def robust_pixeldrain_download(self, link, filename=None):
        """Enhanced downloader with 5 retry attempts"""
        file_id = link.rstrip('/').split('/')[-1]
        temp_dir = tempfile.mkdtemp()
        
        for attempt in range(1, 6):  # 5 attempts
            if self.cancel_download:
                self.root.after(0, self.update_status, "Download cancelled")
                shutil.rmtree(temp_dir, ignore_errors=True)
                return None
            
            try:
                # Configure session
                session = requests.Session()
                session.headers.update({
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
                    "Accept": "application/octet-stream",
                    "Connection": "keep-alive"
                })
                
                # Get file info to preserve original filename
                info_url = f"https://pixeldrain.com/api/file/{file_id}/info"
                info_response = session.get(info_url, timeout=15)
                info_response.raise_for_status()
                file_info = info_response.json()
                
                # Determine output path with original extension
                original_name = file_info.get('name', f"update_{file_id}")
                output_path = os.path.join(temp_dir, filename or original_name)
                
                # Download file
                self.root.after(0, self.update_status, 
                              f"Downloading (Attempt {attempt}/5)...")
                
                download_url = f"https://pixeldrain.com/api/file/{file_id}"
                total_size = file_info['size']
                downloaded = 0
                start_time = time.time()
                
                with session.get(download_url, stream=True, timeout=30) as response:
                    response.raise_for_status()
                    
                    with open(output_path, 'wb') as f:
                        for chunk in response.iter_content(chunk_size=8192):
                            if self.cancel_download:
                                raise Exception("Download cancelled by user")
                            if chunk:
                                f.write(chunk)
                                downloaded += len(chunk)
                                
                                # Update progress
                                progress = (downloaded / total_size) * 100
                                self.root.after(0, self.update_progress, progress)
                                speed = downloaded / (time.time() - start_time) / 1024
                                status = (f"Downloading: {progress:.1f}% | "
                                         f"Speed: {speed:.1f} KB/s")
                                self.root.after(0, self.update_status, status)
                
                self.root.after(0, self.update_status, "Download complete")
                return output_path
                
            except Exception as e:
                self.root.after(0, self.update_status, 
                               f"Attempt {attempt} failed: {str(e)}")
                if attempt < 5:
                    wait_time = min(2 ** attempt, 15)  # Exponential backoff max 15s
                    self.root.after(0, self.update_status,
                                  f"Retrying in {wait_time} seconds...")
                    time.sleep(wait_time)
                session.close()
        
        shutil.rmtree(temp_dir, ignore_errors=True)
        self.root.after(0, self.update_status, "All download attempts failed")
        return None

    def do_extract_and_install(self, file_path, version, prev_version):
        """Improved extraction supporting ZIP, RAR, and 7z formats"""
        try:
            game_dir = self.game_dir.get()
            temp_dir = tempfile.mkdtemp()
            
            # Check file extension
            file_ext = os.path.splitext(file_path)[1].lower()
            
            # Extract based on file type
            if file_ext == '.zip':
                with zipfile.ZipFile(file_path, 'r') as zip_ref:
                    zip_ref.extractall(temp_dir)
            elif file_ext in ('.rar', '.7z'):
                try:
                    # Try using 7-zip if available
                    subprocess.run(['7z', 'x', file_path, f'-o{temp_dir}', '-y'], 
                                  check=True, capture_output=True)
                except (subprocess.CalledProcessError, FileNotFoundError):
                    self.root.after(0, messagebox.showerror, "Error", 
                                  "Please install 7-Zip to extract RAR/7z files")
                    return
            else:
                self.root.after(0, messagebox.showerror, "Error",
                              f"Unsupported file format: {file_ext}")
                return

            # Find cricket24.exe and copy contents
            cricket_exe_folder = None
            for root, dirs, files in os.walk(temp_dir):
                if 'cricket24.exe' in files:
                    cricket_exe_folder = root
                    break
            
            if cricket_exe_folder:
                for item in os.listdir(cricket_exe_folder):
                    source_path = os.path.join(cricket_exe_folder, item)
                    dest_path = os.path.join(game_dir, item)
                    
                    try:
                        if os.path.isdir(source_path):
                            shutil.copytree(source_path, dest_path, dirs_exist_ok=True)
                        else:
                            shutil.copy2(source_path, dest_path)
                    except Exception as e:
                        print(f"Warning: Could not copy {item}: {str(e)}")
            else:
                # Fallback: Copy common folders
                common_folders = ['Data', 'Binaries', 'Content', 'Engine', 'Cricket24']
                for folder_name in common_folders:
                    for root, dirs, files in os.walk(temp_dir):
                        if folder_name in dirs:
                            source_folder = os.path.join(root, folder_name)
                            dest_folder = os.path.join(game_dir, folder_name)
                            try:
                                shutil.copytree(source_folder, dest_folder, dirs_exist_ok=True)
                            except Exception as e:
                                print(f"Warning: Could not copy {folder_name}: {str(e)}")
                
                # Copy remaining files
                for item in os.listdir(temp_dir):
                    source_path = os.path.join(temp_dir, item)
                    dest_path = os.path.join(game_dir, item)
                    try:
                        if os.path.isdir(source_path):
                            shutil.copytree(source_path, dest_path, dirs_exist_ok=True)
                        else:
                            shutil.copy2(source_path, dest_path)
                    except Exception as e:
                        print(f"Warning: Could not copy {item}: {str(e)}")
            
            shutil.rmtree(temp_dir)
            
        except Exception as e:
            self.root.after(0, messagebox.showerror, "Error", f"Installation failed: {str(e)}")
            self.root.after(0, self.enable_buttons)

    def check_updates(self):
        """Check which updates are needed"""
        if not self.current_version:
            messagebox.showerror("Error", "Please select a valid game directory first")
            return
        
        if self.current_version == self.latest_version:
            messagebox.showinfo("Up to Date", f"Your game is already up to date! (v{self.latest_version})")
            return
        
        # Find updates needed
        updates_needed = []
        start_updating = False
        
        for version in self.versions:
            if version == self.current_version:
                start_updating = True
                continue
            if start_updating:
                updates_needed.append(version)
        
        if not updates_needed:
            messagebox.showerror("Error", f"Current version {self.current_version} not recognized")
            return
        
        # Display updates needed
        self.updates_text.config(state='normal')
        self.updates_text.delete(1.0, tk.END)
        self.updates_text.insert(tk.END, "Updates needed:\n\n")
        
        prev_ver = self.current_version
        for version in updates_needed:
            size_key = f"{prev_ver}_{version}"
            size = self.update_sizes.get(size_key, "Standard")
            self.updates_text.insert(tk.END, f"v{prev_ver} → v{version} - Size: {size}\n")
            prev_ver = version
        
        self.updates_text.config(state='disabled')
        self.updates_needed = updates_needed
        self.update_button.config(state='normal')
        self.status_label.config(text=f"Ready to update from v{self.current_version} to v{self.latest_version}")

    def start_update(self):
        """Begin the update process"""
        if not hasattr(self, 'updates_needed'):
            messagebox.showerror("Error", "Please check for updates first")
            return
        
        total_updates = len(self.updates_needed)
        
        if not messagebox.askyesno("Confirm Update", 
                                 f"This will download and install {total_updates} updates.\n"
                                 f"From v{self.current_version} to v{self.latest_version}\n\n"
                                 "Continue?"):
            return
        
        self.update_button.config(state='disabled')
        self.check_button.config(state='disabled')
        self.cancel_button.config(state='normal')
        
        self.current_update_index = 0
        self.start_next_update()
    
    def start_next_update(self):
        """Process the next update in queue"""
        if self.current_update_index >= len(self.updates_needed) or self.cancel_download:
            self.update_complete()
            return
        
        if self.current_update_index == 0:
            prev_version = self.current_version
        else:
            prev_version = self.updates_needed[self.current_update_index - 1]
        
        current_version = self.updates_needed[self.current_update_index]
        link_key = f"{prev_version}_{current_version}"
        download_url = self.pixeldrain_links.get(link_key)
        
        if not download_url:
            messagebox.showerror("Error", f"No download link found for v{prev_version} → v{current_version}")
            self.enable_buttons()
            return
        
        self.downloading = True
        self.status_label.config(text=f"Downloading: v{prev_version} → v{current_version}")
        
        download_thread = threading.Thread(
            target=self.process_update,
            args=(download_url, current_version, prev_version)
        )
        download_thread.daemon = True
        download_thread.start()
    
    def process_update(self, url, version, prev_version):
        """Handle download and installation for one update"""
        try:
            # Download update
            downloaded_file = self.robust_pixeldrain_download(url)
            if not downloaded_file:
                raise Exception("Download failed after 5 attempts")
            
            # Install update
            self.root.after(0, self.update_status, f"Installing v{version}...")
            self.do_extract_and_install(downloaded_file, version, prev_version)
            
            # Clean up
            try:
                os.remove(downloaded_file)
            except:
                pass
            
            # Next update
            self.current_update_index += 1
            self.root.after(0, self.continue_updates)
            
        except Exception as e:
            self.root.after(0, messagebox.showerror, "Error", f"Update failed: {str(e)}")
            self.root.after(0, self.enable_buttons)

    def continue_updates(self):
        """Continue with next update or complete"""
        if self.current_update_index < len(self.updates_needed) and not self.cancel_download:
            remaining = len(self.updates_needed) - self.current_update_index
            self.status_label.config(text=f"Update installed! {remaining} more updates remaining...")
            self.root.after(2000, self.start_next_update)
        else:
            self.update_complete()

    def update_complete(self):
        """Finalize update process"""
        self.downloading = False
        self.cancel_download = False
        self.progress['value'] = 0
        
        if not self.cancel_download:
            self.status_label.config(text="All updates completed successfully!")
            messagebox.showinfo("Update Complete", 
                              f"Cricket 24 has been successfully updated from v{self.current_version} to v{self.latest_version}!")
        
        self.check_version()
        self.enable_buttons()

    def update_status(self, message):
        """Update status label"""
        self.status_label.config(text=message)

    def update_progress(self, value):
        """Update progress bar"""
        self.progress['value'] = value

    def enable_buttons(self):
        """Re-enable control buttons"""
        self.update_button.config(state='normal')
        self.check_button.config(state='normal')
        self.cancel_button.config(state='disabled')
        self.progress['value'] = 0

    def cancel_update(self):
        """Handle update cancellation"""
        if self.downloading:
            self.cancel_download = True
            self.status_label.config(text="Cancelling update...")
            self.cancel_button.config(state='disabled')

def main():
    root = tk.Tk()
    app = Cricket24Updater(root)
    root.mainloop()

if __name__ == "__main__":
    main()