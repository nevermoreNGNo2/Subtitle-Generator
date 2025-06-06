import ffmpeg



import subprocess

def extract_audio(video_path, output_audio_path):
    try:
        ffmpeg_path = r"C:\ffmpeg\bin\ffmpeg.exe"
        print(f"Extracting audio from video: {video_path}")
        
        command = [
            ffmpeg_path,
            "-i", video_path,
            "-ac", "1",
            "-ar", "16000",
            "-vn",
            output_audio_path
        ]
        subprocess.run(command, check=True)
        print(f"Audio extracted successfully and saved to {output_audio_path}")
    
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        raise




