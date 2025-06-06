import tkinter as tk
from tkinter import filedialog, messagebox
import os

from utils.audio_utils import extract_audio
from utils.ass_utils import transcribe_and_generate_ass  # IMPORT the correct function!

def process_video():
    video_path = filedialog.askopenfilename(
        title="Select your movie file", 
        filetypes=[("Video files", "*.mp4 *.mkv *.avi")]    
    )
    if not video_path:
        return

    output_folder = "output"
    os.makedirs(output_folder, exist_ok=True)
    
    # Define the output audio path
    audio_path = os.path.join(output_folder, "output_audio.wav")

    # Remove old audio if it exists
    if os.path.exists(audio_path):
        os.remove(audio_path)

    # Generate ASS subtitle filename
    ass_filename = os.path.splitext(os.path.basename(video_path))[0] + ".ass"
    ass_path = os.path.join(output_folder, ass_filename)
    
    try:
        # Step 1: Extract audio
        print(f"Extracting audio from {video_path}...")
        extract_audio(video_path, audio_path)

        # Step 2: Transcribe and generate .ass subtitles
        print(f"Transcribing audio and generating subtitles...")
        transcribe_and_generate_ass(audio_path, ass_path)

        # Step 3: Show success message
        messagebox.showinfo("Success", f"Subtitles saved at:\n{ass_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{str(e)}")

# Setting up the GUI
root = tk.Tk()
root.title("Subtitle Generator")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

btn = tk.Button(frame, text="Select Video and Generate Subtitles", command=process_video, padx=10, pady=5)
btn.pack()

root.mainloop()
