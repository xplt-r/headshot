#!/usr/bin/env python3

import os
import argparse
import subprocess
from urllib.parse import urlparse

# ======== CONFIG ========
OUTPUT_DIR = "screenshots"
CHROMIUM_BIN = "chromium"  # or use "google-chrome" based on your distro
RESOLUTION = "1366x768"
TIMEOUT = 15

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ======== HELPERS ========

def sanitize_filename(url):
    """Sanitize URL to a safe filename."""
    parsed = urlparse(url)
    safe_host = parsed.netloc.replace(":", "_")
    path_part = parsed.path.replace("/", "_") or "home"
    return f"{safe_host}{path_part}.png"

def take_screenshot(url):
    """Run Chromium headless screenshot command."""
    filename = sanitize_filename(url)
    output_path = os.path.join(OUTPUT_DIR, filename)
    print(f"[+] Capturing: {url} → {output_path}")
    
    try:
        subprocess.run(
            [CHROMIUM_BIN, "--headless", "--disable-gpu",
             f"--screenshot={output_path}", f"--window-size={RESOLUTION}", url],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=TIMEOUT
        )
    except subprocess.TimeoutExpired:
        print(f"[!] Timeout for {url}")
    except Exception as e:
        print(f"[!] Error capturing {url}: {e}")

# ======== MAIN ========

def main():
    parser = argparse.ArgumentParser(
        description="📸 HeadShot - Fast CLI-based headless screenshot tool using Chromium"
    )
    parser.add_argument("-u", "--url", help="Single URL to capture")
    parser.add_argument("-l", "--list", help="File containing list of live URLs (http/https)")
    args = parser.parse_args()

    if not args.url and not args.list:
        parser.print_help()
        return

    if args.url:
        take_screenshot(args.url.strip())

    if args.list:
        if not os.path.isfile(args.list):
            print(f"[!] File not found: {args.list}")
            return
        with open(args.list, "r") as f:
            for line in f:
                url = line.strip()
                if url:
                    take_screenshot(url)

    print(f"\n🎯 Done. Screenshots saved in: `{OUTPUT_DIR}/`")

if __name__ == "__main__":
    main()
