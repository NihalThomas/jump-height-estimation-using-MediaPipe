import cv2
import mediapipe as mp

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Video Capture
cap = cv2.VideoCapture(0)

# Calibration Variables
baseline_y = None
max_displacement = 0
jumping = False
pixel_to_cm = 0.5  # Can be adjusted based on user's setup
jump_count = 0
jump_heights = []

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to RGB for MediaPipe
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(frame_rgb)

    # Extract landmarks if detected
    if results.pose_landmarks:
        # Calculate mid-hip point
        left_hip = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP]
        right_hip = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP]
        current_y = (left_hip.y + right_hip.y) / 2

        # Convert normalized y-coordinate to pixel space
        H = frame.shape[0]
        current_y_px = current_y * H

        # Baseline Calibration
        if baseline_y is None:
            baseline_y = current_y_px

        # Jump Detection
        threshold = 10  # Minimum upward movement required to detect a jump
        if baseline_y - current_y_px > threshold:
            jumping = True
            displacement = baseline_y - current_y_px
            max_displacement = max(max_displacement, displacement)
        else:
            if jumping:
                # Calculate jump height and display
                jump_height_cm = max_displacement * pixel_to_cm
                jump_heights.append(jump_height_cm)
                jump_count += 1
                print(f"Jump {jump_count}: {jump_height_cm:.2f} cm")
                jumping = False
                max_displacement = 0

        # Draw landmarks
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    
    cv2.putText(frame, f"Jumps: {jump_count}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    if jump_heights:
        cv2.putText(frame, f"Last Jump: {jump_heights[-1]:.2f} cm", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    
    cv2.imshow('Jump Height Estimation', frame)

    # Quit with 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
