# Video Trimmer Script

## Overview
This Python script efficiently trims multiple video files to a specific duration using the `moviepy` library. It is particularly useful for content creators, social media managers, or anyone needing to extract short clips from longer videos quickly.

## Features
- **Batch Processing**: Automatically trims multiple video files in a loop.
- **Customizable Duration**: By default, extracts the first 15 seconds of each video (can be adjusted in the script).
- **Simple & Lightweight**: Uses `moviepy`'s `ffmpeg_extract_subclip` for fast processing without excessive dependencies.
- **Automated File Naming**: Saves the trimmed videos with a `trimmed_` prefix to prevent overwriting original files.

## Requirements
Make sure you have Python installed along with the required library:

```bash
pip install moviepy
```

## Usage
1. Place the script in the same directory as your video files.
2. Modify the `video_files` list with the names of the videos you want to trim.
3. Adjust `start_time` and `end_time` if needed.
4. Run the script:

```bash
python videotrimer.py
```

## Customization
- Modify `start_time` and `end_time` to change the duration of the trimmed clips.
- Add more filenames to `video_files` for bulk processing.
- Enhance the script with user input for dynamic trimming durations.

## License
This project is open-source under the MIT License.

---

This script simplifies video trimming tasks, making it an excellent tool for quick edits. Feel free to improve and extend its functionality!

