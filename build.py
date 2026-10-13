"""Build a standalone app with PyInstaller (and the Windows installer).

    python build.py              # dist/GooglePlayReviewsScraper(.exe/.app)
    python build.py --installer  # Windows: also runs Inno Setup -> installer/

Needs: pip install -r requirements-dev.txt
Installer needs Inno Setup 6 (https://jrsoftware.org/isinfo.php).
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NAME = "GooglePlayReviewsScraper"


def run(cmd: list[str]) -> None:
    print("$", " ".join(cmd))
    subprocess.run(cmd, check=True, cwd=ROOT)


def build_app() -> Path:
    for folder in ("build", "dist"):
        shutil.rmtree(ROOT / folder, ignore_errors=True)

    icon = "google-play.ico" if sys.platform == "win32" else "google-play.png"
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--noconfirm", "--clean", "--windowed",
        "--name", NAME,
        "--paths", "src",
        "--icon", str(Path("assets", "icons", icon)),
        "--add-data", f"assets{os.pathsep}assets",
        "--collect-data", "customtkinter",
        # CTkImage -> PIL.ImageTk needs this and PyInstaller can't see it
        "--hidden-import", "PIL._tkinter_finder",
        # pandas pulls these in but the app never uses them
        "--exclude-module", "matplotlib",
        "--exclude-module", "IPython",
        "--exclude-module", "pytest",
    ]
    # One file on Windows/Linux; macOS gets a proper .app bundle instead.
    if sys.platform != "darwin":
        cmd.append("--onefile")
    cmd.append(str(Path("src", "app_gui.py")))
    run(cmd)

    out = ROOT / "dist" / (f"{NAME}.exe" if sys.platform == "win32" else
                           f"{NAME}.app" if sys.platform == "darwin" else NAME)
    print(f"\n✓ built {out}")
    return out


def find_iscc() -> str | None:
    found = shutil.which("ISCC") or shutil.which("iscc")
    if found:
        return found
    for base in (os.environ.get("ProgramFiles(x86)"), os.environ.get("ProgramFiles")):
        candidate = Path(base or "", "Inno Setup 6", "ISCC.exe")
        if candidate.exists():
            return str(candidate)
    return None


def build_installer() -> None:
    if sys.platform != "win32":
        sys.exit("The installer can only be built on Windows.")
    iscc = find_iscc()
    if not iscc:
        sys.exit("Inno Setup 6 not found. Install it from https://jrsoftware.org/isinfo.php")
    run([iscc, "installer.iss"])
    print("✓ installer written to installer/")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--installer", action="store_true", help="also build the Windows installer")
    args = parser.parse_args()
    build_app()
    if args.installer:
        build_installer()


if __name__ == "__main__":
    main()
