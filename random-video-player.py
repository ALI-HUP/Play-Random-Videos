#!/usr/bin/env python3

import os
import secrets  # Replaced 'random' with 'secrets' for true OS-level randomness
import subprocess
import sys

# 1. Define constants
VIDEO_DIR = "/home/ali/Disk/Programing/html/New folder/New folder/New folder/New folder"
VIDEO_EXTENSIONS = {".mp4", ".mkv", ".avi", ".mov", ".flv", ".webm", ".wmv"}

def get_random_video():
    """Finds all valid video files and picks one with cryptographic randomness."""
    if not os.path.exists(VIDEO_DIR):
        print(f"Error: The directory '{VIDEO_DIR}' does not exist.", file=sys.stderr)
        sys.exit(1)

    # Filter files by checking extensions (case-insensitive)
    files = [
        f for f in os.listdir(VIDEO_DIR)
        if os.path.isfile(os.path.join(VIDEO_DIR, f)) and os.path.splitext(f)[1].lower() in VIDEO_EXTENSIONS
    ]

    if not files:
        print("Error: No valid video files found in the folder.", file=sys.stderr)
        sys.exit(1)

    # secrets.choice is completely random and unpredictable
    return secrets.choice(files)

def generate_unique_name(ext):
    """Generates a totally random, unpredictable 16-digit filename."""
    while True:
        # First digit (1-9) to avoid leading zeros if you treat it as an integer later
        first_digit = str(secrets.choice(range(1, 10)))
        # Remaining 15 digits (0-9) generated independently
        remaining_digits = "".join(str(secrets.choice(range(10))) for _ in range(15))
        
        new_name = f"{first_digit}{remaining_digits}{ext}"
        new_path = os.path.join(VIDEO_DIR, new_name)
        
        if not os.path.exists(new_path):
            return new_name, new_path

def main():
    # 1. Totally random video selection
    selected_video = get_random_video()
    video_path = os.path.join(VIDEO_DIR, selected_video)
    
    print(f"Playing: {selected_video}")
    
    # 2. Play the video via MPV
    try:
        subprocess.run(["mpv", video_path], check=True)
    except FileNotFoundError:
        print("Error: 'mpv' player is not installed or not in PATH.", file=sys.stderr)
        sys.exit(1)
    except subprocess.CalledProcessError:
        print("Warning: mpv closed with an error status.", file=sys.stderr)

    # 3. Totally random renaming
    _, ext = os.path.splitext(selected_video)
    new_filename, new_path = generate_unique_name(ext.lower())
    
    try:
        os.rename(video_path, new_path)
        print(f"Successfully renamed to: {new_filename}")
    except Exception as e:
        print(f"Failed to rename file: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()