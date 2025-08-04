#!/usr/bin/env python3
"""Simple installation script for Google Play Reviews Scraper."""

import subprocess
import sys
import os

def main():
    """Install dependencies and run the application."""
    print("🚀 Installing Google Play Reviews Scraper...")
    
    # Check Python version
    if sys.version_info < (3, 7):
        print("❌ Python 3.7+ required. Current version:", sys.version)
        sys.exit(1)
    
    # Install requirements
    print("📦 Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully!")
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        sys.exit(1)
    
    # Launch appropriate GUI based on platform
    print("🎬 Launching GUI...")
    try:
        import platform
        system = platform.system()
        
        if system == "Darwin":  # macOS
            print("🍎 Detected macOS - launching native interface...")
            subprocess.run([sys.executable, "src/app_gui_mac.py"])
        elif system == "Windows":  # Windows
            print("🪟 Detected Windows - launching Windows interface...")
            subprocess.run([sys.executable, "src/app_gui.py"])
        else:  # Linux and others
            print("🐧 Detected Linux/Unix - launching cross-platform interface...")
            subprocess.run([sys.executable, "src/app_gui.py"])
            
    except KeyboardInterrupt:
        print("\n👋 Thanks for using Google Play Reviews Scraper!")
    except Exception as e:
        print(f"❌ Error launching GUI: {e}")
        print("💡 Try running manually:")
        if platform.system() == "Darwin":
            print("   python src/app_gui_mac.py")
        else:
            print("   python src/app_gui.py")

if __name__ == "__main__":
    main()