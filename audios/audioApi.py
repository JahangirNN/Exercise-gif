import requests
from datetime import datetime
import wave

# Replace with your actual API token
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiI2NzA4NDAzYTU4MzJiMTcyYzJkMWI5MWEiLCJrZXlOYW1lIjoibXktbmV3LWFwaSIsImlhdCI6MTcyOTE1MjE5MX0.VKRRfWJZt0OHJBij9doiP1uKfm18ZuhymJR2eXIgjsE"

# API URL
url = "http://waves-api.smallest.ai/api/v1/lightning/get_speech"
SAMPLE_RATE = 24000  # Set sample rate (can be 8000, 16000, 24000, 48000)
VOICE_ID = "emily"  # Options: arman, james, emily, etc.

# List of exercises with their descriptions
exercises = [
    ("March in Place", "Lift knees and pump arms."),
    ("Jumping Jacks", "Jump, spread legs, and raise arms."),
    ("Mountain Climbers", "Alternate knees towards your chest."),
    ("Pelvic Floor Squeeze", "Contract and release pelvic floor muscles."),
    ("Lateral Lunges", "Step out to the side and lower hips."),
    ("Pelvic Tilts", "Flatten back against the floor."),
    ("Hold and Release Kegel", "Tighten and relax pelvic muscles."),
    ("Romanian Deadlifts Right", "Lower torso while extending one leg."),
    ("Romanian Deadlifts Left", "Lower torso while extending the other leg."),
    ("Standing Toe Touch", "Bend forward to touch your toes."),
    ("Prone Pelvic Rotations", "Rotate lower back and pelvis."),
    ("Pelvic Side Press", "Press lower back towards the ground."),
    ("Prone Pelvic Thrust", "Controlled thrusting motion with pelvis."),
    ("Thrust Jumps", "Jump feet towards hands in a V-shape."),
    ("Pelvic Attack", "Controlled hip thrusts in a stable position."),
    ("Vertical Hip Swing", "Swing hips vertically with control."),
    ("Sky Thrust", "Thrust hips upward in a controlled motion."),
    ("Advanced Bridges", "Lift hips forming a straight line."),
    ("Back Burden", "Rapid thrusting motions with pelvis."),
    ("Rotating Back Burden", "Rotate hips side to side while thrusting."),
    ("Slanted Hip Thrust", "Thrust hips forward while keeping stable."),
    ("V-Thrust", "Pelvis thrusts downward in a V-shape."),
    ("Deep V-Thrusts", "Thrust pelvis downwards in a wide stance."),
    ("Supine Leg Raise", "Lift legs to a 90-degree angle."),
    ("Plank", "Body in a straight line from head to heels."),
    ("Glute Bridges", "Lift hips towards the ceiling."),
    ("Hip Thrusts", "Push hips upward with a weight."),
    ("Sumo Squat", "Lower hips back and down, keeping knees aligned."),
    ("Romanian Deadlifts Right", "Lower torso while extending one leg."),
    ("Frog Thrusts", "Thrust hips in a frog-like position."),
    ("Standing Toe Touch", "Bend forward to touch your toes."),
    ("Butterfly Hip Thrusts", "Thrust hips upward from a seated position."),
    ("Standing Quad Stretch Right", "Pull foot towards butt to stretch."),
    ("Cobra Pose", "Arch back and stretch chest."),
    ("Child's Pose", "Rest forehead on the floor and breathe."),
    ("Diaphragmatic Breathing", "Inhale deeply and exhale slowly."),
    ("Spinal Twists", "Bend knee across body, keeping shoulders grounded."),
    ("Standing Toe Touches", "Reach towards your toes with straight legs."),
    ("Chair Pose", "Lower hips as if sitting in a chair."),
    ("Cat-Cow Pose", "Alternate between arching and rounding your back."),
    ("Hold and Release Kegel", "Tighten and relax pelvic muscles.")
]

# Headers
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

# Loop through each exercise and create an audio file
for exercise_name, description in exercises:
    payload = {
        "text": description,
        "voice_id": VOICE_ID,
        "sample_rate": SAMPLE_RATE
    }

    # Request audio from the API
    print(f"Sending request for: {exercise_name} - {datetime.now()}")
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        # Create filename with underscores instead of spaces
        filename = exercise_name.replace(" ", "_") + ".wav"
        print(f"Saving audio for: {exercise_name} as {filename}")

        # Save the audio content as a .wav file
        with wave.open(filename, 'wb') as wav_file:
            wav_file.setnchannels(1)  # Mono channel
            wav_file.setsampwidth(2)  # 16-bit samples (2 bytes)
            wav_file.setframerate(SAMPLE_RATE)
            wav_file.writeframes(response.content)
        
        print(f"Audio saved: {filename}")
    else:
        print(f"Error for {exercise_name}: Status code {response.status_code}")

print("All audio files generated successfully!")

# import requests
# from datetime import datetime
# import wave

# # Replace with your actual API token
# TOKEN = ""

# # API URL
# url = "http://waves-api.smallest.ai/api/v1/lightning/get_speech"
# SAMPLE_RATE = 24000  # Set sample rate (can be 8000, 16000, 24000, 48000)
# VOICE_ID = "emily"  # Options: arman, james, emily, etc.

# # List of exercises
# exercises = [
#     # "March in Place", "Jumping Jacks", "Mountain Climbers", "Pelvic Floor Squeeze",
#     # "Lateral Lunges", "Pelvic Tilts", "Hold and Release Kegel", "Romanian Deadlifts Right",
#     # "Standing Toe Touch", "Prone Pelvic Rotations", "Pelvic Side Press", "Prone Pelvic Thrust",
#     # "Thrust Jumps", "Pelvic Attack", "Vertical Hip Swing", "Sky Thrust", "Advanced Bridges",
#     # "Back Burden", "Rotating Back Burden", "Slanted Hip Thrust", "V-Thrust", "Deep V-Thrusts",
#     # "Supine Leg Raise", "Plank", "Glute Bridges", "Hip Thrusts", "Sumo Squat",
#     # "Romanian Deadlifts Right", "Frog Thrusts", "Standing Toe Touch", "Butterfly Hip Thrusts",
#     # "Standing Quad Stretch Right", "Cobra Pose", "Child's Pose", "Diaphragmatic Breathing",
#     # "Spinal Twists", "Standing Toe Touches", "Chair Pose", "Cat-Cow Pose", "Hold and Release Kegel",
#     "8", "10", "12", "15", "20", "120",
#     # "start the exercise", "get ready for the next exercise", "seconds", "repeats"
# ]

# # Headers
# headers = {
#     "Authorization": f"Bearer {TOKEN}",
#     "Content-Type": "application/json"
# }

# # Loop through each exercise and create an audio file
# for exercise in exercises:
#     payload = {
#         "text": exercise,
#         "voice_id": VOICE_ID,
#         "sample_rate": SAMPLE_RATE
#     }

#     # Request audio from the API
#     print(f"Sending request for: {exercise} - {datetime.now()}")
#     response = requests.post(url, json=payload, headers=headers)

#     if response.status_code == 200:
#         # Create filename with underscores instead of spaces
#         filename = exercise.replace(" ", "_") + ".wav"
#         print(f"Saving audio for: {exercise} as {filename}")

#         # Save the audio content as a .wav file
#         with wave.open(filename, 'wb') as wav_file:
#             wav_file.setnchannels(1)  # Mono channel
#             wav_file.setsampwidth(2)  # 16-bit samples (2 bytes)
#             wav_file.setframerate(SAMPLE_RATE)
#             wav_file.writeframes(response.content)
        
#         print(f"Audio saved: {filename}")
#     else:
#         print(f"Error for {exercise}: Status code {response.status_code}")

# print("All audio files generated successfully!")
