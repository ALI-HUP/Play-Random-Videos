# Random Video Player & Auto-Renamer

This project is a small Python utility that randomly selects a video file from a directory,
plays it using a media player, and automatically renames the played file after playback ends.

Each video file is renamed to a new, unique **16-digit numeric filename** that never starts with zero
and never conflicts with existing files. The original file extension is always preserved.

---

## Requirements

- Python 3
- mpv media player
- Linux-based operating system (tested on Ubuntu)

---

## What This Script Does

- Scans a specified directory for video files
- Randomly selects one file
- Plays the selected video using `mpv`
- Waits until the media player is closed
- Renames the played file to a new random 16-digit number
- Prevents filename collisions
- Ensures filenames never start with `0`

---

## Process Overview

1. All regular files in the target directory are collected.
2. One file is chosen randomly.
3. The selected video is played via `mpv`.
4. The script blocks until the player is closed.
5. After playback:
   - A new 16-digit filename is generated.
   - The first digit is guaranteed to be between `1` and `9`.
   - If the generated name already exists, a new one is generated.
6. The played video file is renamed using the new unique name.

---

## Setup & Usage

1. Clone the repository or download the script.
2. Edit the script and set the correct absolute path for `VIDEO_DIR`.
3. Make the script executable:
   ```bash
   chmod +x play_random_video.py

---

## Script execution

   - Randomly selects: 1928374650918273.mkv
   - Plays the video using mpv
   - Waits for the player to close