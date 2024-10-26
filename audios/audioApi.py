import requests
from datetime import datetime
import wave

# Replace with your actual API token
TOKEN = ""

# API URL
url = "http://waves-api.smallest.ai/api/v1/lightning/get_speech"
SAMPLE_RATE = 24000  # Set sample rate (can be 8000, 16000, 24000, 48000)
VOICE_ID = "emily"  # Options: arman, james, emily, etc.

# List of exercises
exercises = [
    # "March in Place", "Jumping Jacks", "Mountain Climbers", "Pelvic Floor Squeeze",
    # "Lateral Lunges", "Pelvic Tilts", "Hold and Release Kegel", "Romanian Deadlifts Right",
    # "Standing Toe Touch", "Prone Pelvic Rotations", "Pelvic Side Press", "Prone Pelvic Thrust",
    # "Thrust Jumps", "Pelvic Attack", "Vertical Hip Swing", "Sky Thrust", "Advanced Bridges",
    # "Back Burden", "Rotating Back Burden", "Slanted Hip Thrust", "V-Thrust", "Deep V-Thrusts",
    # "Supine Leg Raise", "Plank", "Glute Bridges", "Hip Thrusts", "Sumo Squat",
    # "Romanian Deadlifts Right", "Frog Thrusts", "Standing Toe Touch", "Butterfly Hip Thrusts",
    # "Standing Quad Stretch Right", "Cobra Pose", "Child's Pose", "Diaphragmatic Breathing",
    # "Spinal Twists", "Standing Toe Touches", "Chair Pose", "Cat-Cow Pose", "Hold and Release Kegel",
    "8", "10", "12", "15", "20", "120",
    # "start the exercise", "get ready for the next exercise", "seconds", "repeats"
]

# Headers
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

# Loop through each exercise and create an audio file
for exercise in exercises:
    payload = {
        "text": exercise,
        "voice_id": VOICE_ID,
        "sample_rate": SAMPLE_RATE
    }

    # Request audio from the API
    print(f"Sending request for: {exercise} - {datetime.now()}")
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        # Create filename with underscores instead of spaces
        filename = exercise.replace(" ", "_") + ".wav"
        print(f"Saving audio for: {exercise} as {filename}")

        # Save the audio content as a .wav file
        with wave.open(filename, 'wb') as wav_file:
            wav_file.setnchannels(1)  # Mono channel
            wav_file.setsampwidth(2)  # 16-bit samples (2 bytes)
            wav_file.setframerate(SAMPLE_RATE)
            wav_file.writeframes(response.content)
        
        print(f"Audio saved: {filename}")
    else:
        print(f"Error for {exercise}: Status code {response.status_code}")

print("All audio files generated successfully!")
