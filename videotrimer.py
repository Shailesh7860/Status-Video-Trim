from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# Input video file paths
video_files = ["video1.mp4", "video2.mp4", "video3.mp4"]

# Loop through each video file
for video_file in video_files:
    # Specify the start and end times in seconds for trimming (e.g., 0 to 15 seconds)
    start_time = 0
    end_time = 15

    # Output file name for the trimmed video
    output_file = f"trimmed_{video_file}"

    # Trim the video
    ffmpeg_extract_subclip(video_file, start_time, end_time, targetname=output_file)

print("Trimming completed.")
