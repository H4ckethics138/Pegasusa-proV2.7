#!/usr/bin/env python3
import os
import sys
import subprocess
import platform
import shutil

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_banner():
    print("\033[96m" + "="*60)
    print("   PEGASUSA-PRO v2.8 ULTIMATE - DEPENDENCY INSTALLER")
    print("      Automated Setup for Linux, Termux, and Windows")
    print("="*60 + "\033[0m")

def install_python_packages():
    print("\033[93m[*] Installing Python packages...\033[0m")
    packages = ["colorama", "requests"]
    for pkg in packages:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])
            print(f"\033[92m[✓] {pkg} installed successfully.\033[0m")
        except:
            print(f"\033[91m[!] Failed to install {pkg}.\033[0m")

def setup_linux():
    print("\033[93m[*] Detected Linux system. Installing system dependencies...\033[0m")
    dependencies = ["adb", "scrcpy", "nmap", "qrencode", "metasploit-framework"]
    
    # Update package list
    os.system("sudo apt update -y")
    
    for dep in dependencies:
        if not shutil.which(dep):
            print(f"\033[94m[+] Installing {dep}...\033[0m")
            if dep == "metasploit-framework":
                os.system("curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall")
            else:
                os.system(f"sudo apt install -y {dep}")
        else:
            print(f"\033[92m[✓] {dep} is already installed.\033[0m")

def setup_termux():
    print("\033[93m[*] Detected Termux environment. Installing dependencies...\033[0m")
    dependencies = ["android-tools", "nmap", "qrencode", "metasploit"]
    
    os.system("pkg update -y && pkg upgrade -y")
    
    for dep in dependencies:
        print(f"\033[94m[+] Installing {dep}...\033[0m")
        os.system(f"pkg install {dep} -y")

def setup_windows():
    print("\033[93m[*] Detected Windows system.\033[0m")
    print("\033[91m[!] Please install the following manually on Windows:\033[0m")
    print("1. ADB (Android Platform Tools)")
    print("2. scrcpy (Screen Copy)")
    print("3. Nmap (Network Mapper)")
    print("4. Metasploit Framework")
    print("\n\033[93m[*] Attempting to install Python packages...\033[0m")
    install_python_packages()

def main():
    clear_screen()
    print_banner()
    
    current_os = platform.system().lower()
    is_termux = 'com.termux' in os.environ.get('PREFIX', '') or 'termux' in os.environ.get('SHELL', '')

    if is_termux:
        setup_termux()
    elif current_os == "linux":
        setup_linux()
    elif current_os == "windows":
        setup_windows()
    else:
        print(f"\033[91m[!] Unsupported OS: {current_os}\033[0m")
        sys.exit(1)
    
    install_python_packages()
    
    print("\n\033[92m" + "="*60)
    print("   SETUP COMPLETED SUCCESSFULLY!")
    print("   You can now run: python3 PEGASUSA_PRO_V2_8_ULTIMATE.py")
    print("="*60 + "\033[0m")

if __name__ == "__main__":
    main()
