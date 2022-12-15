
# Load the video
Waft_Success = cv2.VideoCapture('./video/Waft_Success.mp4')
Failed_Waft = cv2.VideoCapture('./video/Failed_Waft.mp4')
New_Champ = cv2.VideoCapture('./video/New_Champ.mp4')
Old_Champ = cv2.VideoCapture('./video/Old_Champ.mp4')
Prayer = cv2.VideoCapture('./video/Prayer.mp4')
Strength_Potion = cv2.VideoCapture('./video/Stength_Potion.mp4')
Heal = cv2.VideoCapture('./video/Heal.mp4')
Damage = cv2.VideoCapture('./video/Damage.mp4')
Clown = cv2.VideoCapture('./video/Clown.mp4')

import cv2
def play_animation( Animation ):
    # Loop through each frame of the video
    while True:
        # Read the next frame from the video
        success, frame = Animation.read()

        # If there are no more frames left, break the loop
        if not success:
            break

        # Show the frame
        cv2.imshow('Video', frame)

        # Wait for a key press
        key = cv2.waitKey(30)
        if key == 27:  # Esc key
            break

        # Release the VideoCapture object
play_animation( Waft_Success )
play_animation( Failed_Waft )
play_animation( New_Champ )
