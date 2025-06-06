import whisper

def format_ass_timestamp(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = seconds % 60
    centiseconds = int((seconds - int(seconds)) * 100)
    return f"{hours:01}:{minutes:02}:{int(seconds):02}.{centiseconds:02}"

def transcribe_and_generate_ass(audio_path, ass_path):
    try:
        model = whisper.load_model("base")
        print(f"Model loaded successfully!")
        
        print(f"Transcribing audio file: {audio_path}")
        result = model.transcribe(audio_path, word_timestamps=True)


        if not result["segments"]:
            print("No segments found. The audio may be empty or not transcribed correctly.")
            return
        
        # Create and write to the ASS file
        with open(ass_path, "w", encoding="utf-8") as ass_file:
            # Write ASS header (defines styles)
            ass_file.write("""[Script Info]
Title: Whisper Subtitles
ScriptType: v4.00+
PlayResX: 1280
PlayResY: 720

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,Arial,34,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,2,0,2,30,30,20,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
""")
            # for segment in result["segments"]:
            #     start = format_ass_timestamp(segment["start"])
            #     end = format_ass_timestamp(segment["end"])
            #     text = segment["text"].strip().replace('\n', ' ')
            #     ass_file.write(f"Dialogue: 0,{start},{end},Default,,0,0,0,,{text}\n")
            for segment in result["segments"]:
                words = segment.get("words", [])
                if not words:
                    continue

                start = format_ass_timestamp(words[0]["start"])
                end = format_ass_timestamp(words[-1]["end"])
                text = segment["text"].strip().replace('\n', ' ')
                ass_file.write(f"Dialogue: 0,{start},{end},Default,,0,0,0,,{text}\n")

        print(f"Subtitles successfully written to {ass_path}")
    
    except Exception as e:
        print(f"An error occurred: {e}")


