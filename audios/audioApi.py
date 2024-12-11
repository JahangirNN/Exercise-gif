import requests
from datetime import datetime
import wave

# Replace with your actual API token
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiI2NzA4NDAzYTU4MzJiMTcyYzJkMWI5MWEiLCJrZXlOYW1lIjoibXktbmV3LWFwaSIsImlhdCI6MTcyOTE1MjE5MX0.VKRRfWJZt0OHJBij9doiP1uKfm18ZuhymJR2eXIgjsE"

# API URL
url = "http://waves-api.smallest.ai/api/v1/lightning/get_speech"
SAMPLE_RATE = 24000  # Set sample rate (can be 8000, 16000, 24000, 48000)
VOICE_ID = "emily"  # Options: arman, james, emily, etc.

# Audio fix merge 
exercises = [
    ("March in Place", "Start the exercise. March in Place. Lift knees and pump arms."),
    ("Jumping Jacks", "Start the exercise. Jumping Jacks. Jump, spread legs, and raise arms."),
    ("Mountain Climbers", "Start the exercise. Mountain Climbers. Alternate knees towards your chest."),
    ("Pelvic Floor Squeeze", "Start the exercise. Pelvic Floor Squeeze. Contract and release pelvic floor muscles."),
    ("Lateral Lunges", "Start the exercise. Lateral Lunges. Step out to the side and lower hips."),
    ("Pelvic Tilts", "Start the exercise. Pelvic Tilts. Flatten back against the floor."),
    ("Hold and Release Kegel", "Start the exercise. Hold and Release Kegel. Tighten and relax pelvic muscles."),
    ("Romanian Deadlifts Right", "Start the exercise. Romanian Deadlifts Right. Lower torso while extending one leg."),
    ("Romanian Deadlifts Left", "Start the exercise. Romanian Deadlifts Left. Lower torso while extending the other leg."),
    ("Standing Toe Touch", "Start the exercise. Standing Toe Touch. Bend forward to touch your toes."),
    ("Prone Pelvic Rotations", "Start the exercise. Prone Pelvic Rotations. Rotate lower back and pelvis."),
    ("Pelvic Side Press", "Start the exercise. Pelvic Side Press. Press lower back towards the ground."),
    ("Prone Pelvic Thrust", "Start the exercise. Prone Pelvic Thrust. Controlled thrusting motion with pelvis."),
    ("Thrust Jumps", "Start the exercise. Thrust Jumps. Jump feet towards hands in a V-shape."),
    ("Pelvic Attack", "Start the exercise. Pelvic Attack. Controlled hip thrusts in a stable position."),
    ("Vertical Hip Swing", "Start the exercise. Vertical Hip Swing. Swing hips vertically with control."),
    ("Sky Thrust", "Start the exercise. Sky Thrust. Thrust hips upward in a controlled motion."),
    ("Advanced Bridges", "Start the exercise. Advanced Bridges. Lift hips forming a straight line."),
    ("Back Burden", "Start the exercise. Back Burden. Rapid thrusting motions with pelvis."),
    ("Rotating Back Burden", "Start the exercise. Rotating Back Burden. Rotate hips side to side while thrusting."),
    ("Slanted Hip Thrust", "Start the exercise. Slanted Hip Thrust. Thrust hips forward while keeping stable."),
    ("V-Thrust", "Start the exercise. V-Thrust. Pelvis thrusts downward in a V-shape."),
    ("Deep V-Thrusts", "Start the exercise. Deep V-Thrusts. Thrust pelvis downwards in a wide stance."),
    ("Supine Leg Raise", "Start the exercise. Supine Leg Raise. Lift legs to a 90-degree angle."),
    ("Plank", "Start the exercise. Plank. Body in a straight line from head to heels."),
    ("Glute Bridges", "Start the exercise. Glute Bridges. Lift hips towards the ceiling."),
    ("Hip Thrusts", "Start the exercise. Hip Thrusts. Push hips upward with a weight."),
    ("Sumo Squat", "Start the exercise. Sumo Squat. Lower hips back and down, keeping knees aligned."),
    ("Romanian Deadlifts Right", "Start the exercise. Romanian Deadlifts Right. Lower torso while extending one leg."),
    ("Frog Thrusts", "Start the exercise. Frog Thrusts. Thrust hips in a frog-like position."),
    ("Standing Toe Touch", "Start the exercise. Standing Toe Touch. Bend forward to touch your toes."),
    ("Butterfly Hip Thrusts", "Start the exercise. Butterfly Hip Thrusts. Thrust hips upward from a seated position."),
    ("Standing Quad Stretch Right", "Start the exercise. Standing Quad Stretch Right. Pull foot towards butt to stretch."),
    ("Cobra Pose", "Start the exercise. Cobra Pose. Arch back and stretch chest."),
    ("Child's Pose", "Start the exercise. Child's Pose. Rest forehead on the floor and breathe."),
    ("Diaphragmatic Breathing", "Start the exercise. Diaphragmatic Breathing. Inhale deeply and exhale slowly."),
    ("Spinal Twists", "Start the exercise. Spinal Twists. Bend knee across body, keeping shoulders grounded."),
    ("Standing Toe Touches", "Start the exercise. Standing Toe Touches. Reach towards your toes with straight legs."),
    ("Chair Pose", "Start the exercise. Chair Pose. Lower hips as if sitting in a chair."),
    ("Cat-Cow Pose", "Start the exercise. Cat-Cow Pose. Alternate between arching and rounding your back."),
    ("Hold and Release Kegel", "Start the exercise. Hold and Release Kegel. Tighten and relax pelvic muscles."),
    ("get ready for the next exercise", "get ready for the next exercise."),

]


# # List of exercises with their descriptions
# # exercises = [
# #     ("March in Place", "Lift knees and pump arms."),
# #     ("Jumping Jacks", "Jump, spread legs, and raise arms."),
# #     ("Mountain Climbers", "Alternate knees towards your chest."),
# #     ("Pelvic Floor Squeeze", "Contract and release pelvic floor muscles."),
# #     ("Lateral Lunges", "Step out to the side and lower hips."),
# #     ("Pelvic Tilts", "Flatten back against the floor."),
# #     ("Hold and Release Kegel", "Tighten and relax pelvic muscles."),
# #     ("Romanian Deadlifts Right", "Lower torso while extending one leg."),
# #     ("Romanian Deadlifts Left", "Lower torso while extending the other leg."),
# #     ("Standing Toe Touch", "Bend forward to touch your toes."),
# #     ("Prone Pelvic Rotations", "Rotate lower back and pelvis."),
# #     ("Pelvic Side Press", "Press lower back towards the ground."),
# #     ("Prone Pelvic Thrust", "Controlled thrusting motion with pelvis."),
# #     ("Thrust Jumps", "Jump feet towards hands in a V-shape."),
# #     ("Pelvic Attack", "Controlled hip thrusts in a stable position."),
# #     ("Vertical Hip Swing", "Swing hips vertically with control."),
# #     ("Sky Thrust", "Thrust hips upward in a controlled motion."),
# #     ("Advanced Bridges", "Lift hips forming a straight line."),
# #     ("Back Burden", "Rapid thrusting motions with pelvis."),
# #     ("Rotating Back Burden", "Rotate hips side to side while thrusting."),
# #     ("Slanted Hip Thrust", "Thrust hips forward while keeping stable."),
# #     ("V-Thrust", "Pelvis thrusts downward in a V-shape."),
# #     ("Deep V-Thrusts", "Thrust pelvis downwards in a wide stance."),
# #     ("Supine Leg Raise", "Lift legs to a 90-degree angle."),
# #     ("Plank", "Body in a straight line from head to heels."),
# #     ("Glute Bridges", "Lift hips towards the ceiling."),
# #     ("Hip Thrusts", "Push hips upward with a weight."),
# #     ("Sumo Squat", "Lower hips back and down, keeping knees aligned."),
# #     ("Romanian Deadlifts Right", "Lower torso while extending one leg."),
# #     ("Frog Thrusts", "Thrust hips in a frog-like position."),
# #     ("Standing Toe Touch", "Bend forward to touch your toes."),
# #     ("Butterfly Hip Thrusts", "Thrust hips upward from a seated position."),
# #     ("Standing Quad Stretch Right", "Pull foot towards butt to stretch."),
# #     ("Cobra Pose", "Arch back and stretch chest."),
# #     ("Child's Pose", "Rest forehead on the floor and breathe."),
# #     ("Diaphragmatic Breathing", "Inhale deeply and exhale slowly."),
# #     ("Spinal Twists", "Bend knee across body, keeping shoulders grounded."),
# #     ("Standing Toe Touches", "Reach towards your toes with straight legs."),
# #     ("Chair Pose", "Lower hips as if sitting in a chair."),
# #     ("Cat-Cow Pose", "Alternate between arching and rounding your back."),
# #     ("Hold and Release Kegel", "Tighten and relax pelvic muscles.")
# # ]
# exercises = [
#     ("March in Place", "घुटनों को उठाएं और भुजाओं को पंप करें।"),
#     ("Jumping Jacks", "कूदें, पैरों को फैलाएं, और भुजाओं को उठाएं।"),
#     ("Mountain Climbers", "एक के बाद एक घुटनों को छाती की ओर लाएं।"),
#     ("Pelvic Floor Squeeze", "पेल्विक फ्लोर मसल्स को संकुचित और छोड़ें।"),
#     ("Lateral Lunges", "साइड में कदम रखें और कूल्हों को नीचे करें।"),
#     ("Pelvic Tilts", "पीठ को फर्श के खिलाफ चपटा करें।"),
#     ("Hold and Release Kegel", "पेल्विक मसल्स को कसें और ढीला करें।"),
#     ("Romanian Deadlifts Right", "एक पैर को बढ़ाते हुए धड़ को नीचे करें।"),
#     ("Romanian Deadlifts Left", "दूसरे पैर को बढ़ाते हुए धड़ को नीचे करें।"),
#     ("Standing Toe Touch", "आगे झुकें और अपने पैर की अंगुलियों को छुएं।"),
#     ("Prone Pelvic Rotations", "कमर और पेल्विस को घुमाएं।"),
#     ("Pelvic Side Press", "कमर को ज़मीन की ओर दबाएं।"),
#     ("Prone Pelvic Thrust", "पेल्विस के साथ नियंत्रित धक्का दें।"),
#     ("Thrust Jumps", "हाथों की ओर पैरों को वी-आकृति में कूदें।"),
#     ("Pelvic Attack", "एक स्थिर स्थिति में नियंत्रित कूल्हे का धक्का दें।"),
#     ("Vertical Hip Swing", "नियंत्रण के साथ कूल्हों को लंबवत झूलाएं।"),
#     ("Sky Thrust", "नियंत्रित गति में कूल्हों को ऊपर धकेलें।"),
#     ("Advanced Bridges", "सीधे लाइन बनाने के लिए कूल्हों को उठाएं।"),
#     ("Back Burden", "पेल्विस के साथ तेज़ धक्का देने वाली गति।"),
#     ("Rotating Back Burden", "धक्का देते समय कूल्हों को साइड से घुमाएं।"),
#     ("Slanted Hip Thrust", "स्थिर रखते हुए कूल्हों को आगे धकेलें।"),
#     ("V-Thrust", "पेल्विस को वी-आकृति में नीचे धकेलें।"),
#     ("Deep V-Thrusts", "चौड़े स्टांस में पेल्विस को नीचे धकेलें।"),
#     ("Supine Leg Raise", "90-डिग्री कोण पर पैर उठाएं।"),
#     ("Plank", "सिर से एड़ी तक सीधे लाइन में शरीर।"),
#     ("Glute Bridges", "छत की ओर कूल्हों को उठाएं।"),
#     ("Hip Thrusts", "वजन के साथ कूल्हों को ऊपर धकेलें।"),
#     ("Sumo Squat", "कूल्हों को पीछे और नीचे करें, घुटनों को संरेखित रखते हुए।"),
#     ("Romanian Deadlifts Right", "एक पैर को बढ़ाते हुए धड़ को नीचे करें।"),
#     ("Frog Thrusts", "मेंढक की स्थिति में कूल्हों को धक्का दें।"),
#     ("Standing Toe Touch", "आगे झुकें और अपने पैर की अंगुलियों को छुएं।"),
#     ("Butterfly Hip Thrusts", "बैठे हुए स्थिति से कूल्हों को ऊपर धकेलें।"),
#     ("Standing Quad Stretch Right", "पैर को बट की ओर खींचें ताकि खिंचाव हो।"),
#     ("Cobra Pose", "पीठ को आर्च करें और छाती को खींचें।"),
#     ("Child's Pose", "माथे को फर्श पर रखें और सांस लें।"),
#     ("Diaphragmatic Breathing", "गहरी सांस लें और धीरे-धीरे छोड़ें।"),
#     ("Spinal Twists", "घुटने को शरीर के पार मोड़ें, कंधों को ज़मीन पर रखें।"),
#     ("Standing Toe Touches", "सीधे पैरों के साथ अपनी पैर की अंगुलियों की ओर पहुंचें।"),
#     ("Chair Pose", "कुर्सी में बैठने की तरह कूल्हों को नीचे करें।"),
#     ("Cat-Cow Pose", "पीठ को आर्च और गोल करें।"),
#     ("Hold and Release Kegel", "पेल्विक मसल्स को कसें और ढीला करें।")
# ]

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
# # exercises = [ 
# #     "इस एक्सरसाइज को आठ", 
# #     "इस एक्सरसाइज को दस ", 
# #     "इस एक्सरसाइज को बारह ", 
# #     "इस एक्सरसाइज को पंद्रह ", 
# #     "इस एक्सरसाइज को बीस ", 
# #     "इस एक्सरसाइज को एक सौ बीस", 
# #     "एक्सरसाइज शुरू करें", 
# #     "अगले एक्सरसाइज के लिए तैयार हो जाएं", 
# #     "सेकंड करें",
# #     "बार दोहराव करें"
# #     "Ready to boost your confidence and connection? Max Out in 30 Days is designed for men 16+ to feel stronger and more assured in every area of life. Start with a quick quiz to personalize your path, then level up through 50+ targeted Kegel exercises that fit right into your day. Get stronger, feel more confident, and take control. Download Max Out in 30 Days and start your journey now!"
# # ]

# # exercises = [
# #     "March in Place", "Jumping Jacks", "Mountain Climbers", "Pelvic Floor Squeeze",
# #     "Lateral Lunges", "Pelvic Tilts", "Hold and Release Kegel", "Romanian Deadlifts Right",
# #     "Standing Toe Touch", "Prone Pelvic Rotations", "Pelvic Side Press", "Prone Pelvic Thrust",
# #     "Thrust Jumps", "Pelvic Attack", "Vertical Hip Swing", "Sky Thrust", "Advanced Bridges",
# #     "Back Burden", "Rotating Back Burden", "Slanted Hip Thrust", "V-Thrust", "Deep V-Thrusts",
# #     "Supine Leg Raise", "Plank", "Glute Bridges", "Hip Thrusts", "Sumo Squat",
# #     "Romanian Deadlifts Right", "Frog Thrusts", "Standing Toe Touch", "Butterfly Hip Thrusts",
# #     "Standing Quad Stretch Right", "Cobra Pose", "Child's Pose", "Diaphragmatic Breathing",
# #     "Spinal Twists", "Standing Toe Touches", "Chair Pose", "Cat-Cow Pose", "Hold and Release Kegel",
# #     "8", "10", "12", "15", "20", "120",
# #     "start the exercise", "get ready for the next exercise", "seconds", "repeats"
# # ]
# # exercises = ['Start the exercise', '']

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
#         filename ="ausio"+ ".wav"
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
