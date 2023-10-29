import cv2
import numpy as np
from helper_functions import calculate_angle, calorie_counter
import time
import streamlit as st


class Highknee():
    def __init__(self):
        self.callibration_check = False
        self.start_time = None
        self.init_time = None
        self.test_timeout = None
        self.final_timeout = None
        self.counter_timeout_text = None
        self.counter_timeout = None
        self.counter = None
        self.count = 0
        self.calories_burned = 0
        self.up = False

    def callibration(self, left_ankle, left_shoulder):
        if left_ankle[0] > 0.2 and left_ankle[0] < 0.9 and left_ankle[1] < 0.95 and left_shoulder[0] > 0.2 and left_shoulder[0] < 0.9:
            self.callibration_check = True

    def draw_initial_text(self):
        cv2.putText(self.image, str('Stand with full body visible'),
                    (150, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 247, 255), 2, cv2.LINE_AA
                    )

    def draw_position_text(self):
        cv2.putText(self.image, str('Stand in right position'),
                    (150, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 247, 255), 2, cv2.LINE_AA
                    )

    def draw_reps_and_calories(self):
        # Visualize Count
        cv2.putText(self.image, "Rep Count = " + str(self.count),
                    (5, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 247, 255), 2, cv2.LINE_AA,
                    )

        cv2.putText(self.image, "Caloried Burned = " + str(self.calories_burned)[:5],
                    (5, 65),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 247, 255), 2, cv2.LINE_AA,
                    )

    def initialize_time_counter(self):
        if self.init_time == None:
            self.init_time = time.time()
            self.test_timeout = self.init_time+61
            self.final_timeout = self.init_time+17
            self.counter_timeout_text = self.init_time+1
            self.counter_timeout = self.init_time+1
            self.counter = 60

    def draw_counter(self):
        if self.init_time is not None:
            if (time.time() > self.counter_timeout_text and time.time() < self.test_timeout):
                cv2.putText(self.image, 'Timer : ' + str(self.counter), (700, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 247, 255), 2, cv2.LINE_AA)
                # draw_text(frame, str(counter), center_x, center_y)
                self.counter_timeout_text += 0.03333
            if (time.time() > self.counter_timeout and time.time() < self.test_timeout):
                self.counter -= 1
                self.counter_timeout += 1

    def fill_top_part(self):
        h, w, _ = self.image.shape
        x, y, w, h = 0, 0, w, 100
        sub_img = self.image[y:y+h, x:x+w]
        white_rect = np.zeros(sub_img.shape, dtype=np.uint8) * 255
        res = cv2.addWeighted(sub_img, 0.45, white_rect, 0.5, 1.0)
        self.image[y:y+h, x:x+w] = res

    def start_exercise(self, mp_drawing, mp_pose, col, video_path):
        # Streamlit
        with col:  # Horizontal Aline
            run = st.checkbox('HighKnee', key='highknee')
        FRAME_WINDOW = st.image([])  # Streamlit Image

        cap = cv2.VideoCapture(video_path)
        # Setup mediapipe instance
        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            while cap.isOpened() and run:
                ret, frame = cap.read()
                if ret:
                    # Recolor self.image to RGB
                    self.image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    w, h, _ = self.image.shape
                    # Make detection
                    results = pose.process(self.image)
                    self.fill_top_part()

                    # Recolor back to BGR
                    self.image.flags.writeable = True
                    self.image = cv2.cvtColor(self.image, cv2.COLOR_RGB2BGR)
                    self.image = cv2.resize(self.image, (900, 650))
                    # Extract landmarks
                    try:
                        landmarks = results.pose_landmarks.landmark
                        # print(landmarks)

                        # Get coordinates
                        left_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                                         landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                        left_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                                      landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                        left_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                                      landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
                        left_hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                                    landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                        left_knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                                     landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
                        left_ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
                                      landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]

                        right_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                                          landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                        right_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                                       landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
                        right_wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                                       landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
                        right_hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                                     landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
                        right_knee = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,
                                      landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
                        right_ankle = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,
                                       landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]

                        # Calculate angle
                        left_angle = calculate_angle(
                            left_wrist, left_elbow, left_shoulder)
                        right_angle = calculate_angle(
                            right_wrist, right_elbow, right_shoulder)

                        left_position_angle = calculate_angle(
                            left_hip, left_knee, left_ankle)
                        right_position_angle = calculate_angle(
                            right_hip, right_knee, right_ankle)

                        if not self.callibration_check:
                            self.callibration(left_ankle, left_shoulder)
                            self.draw_initial_text()
                            continue
                        else:
                            self.initialize_time_counter()

                        # Visualize angle
                        # cv2.putText(self.image, "Left: " + str(left_angle),
                        #             tuple(np.multiply(
                        #                 left_knee, [h, w]).astype(int)),
                        #             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (
                        #                 0, 0, 0), 2, cv2.LINE_AA
                        #             )
                        # cv2.putText(self.image, "Right: " + str(right_angle),
                        #             tuple(np.multiply(
                        #                 right_knee, [h, w]).astype(int)),
                        #             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (
                        #                 0, 0, 0), 2, cv2.LINE_AA
                        #             )

                        # cv2.putText(self.image, "Left: " + str(left_position_angle),
                        #             tuple(np.multiply(
                        #                 left_ankle, [h, w]).astype(int)),
                        #             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (
                        #                 0, 0, 255), 2, cv2.LINE_AA
                        #             )
                        # cv2.putText(self.image, "Right: " + str(right_position_angle),
                        #             tuple(np.multiply(
                        #                 right_hip, [h, w]).astype(int)),
                        #             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (
                        #                 0, 0, 255), 2, cv2.LINE_AA
                        #             )

                        if ((left_position_angle < 20 and right_angle < 20) and (right_position_angle > 80 and left_angle > 80)) or ((left_position_angle > 80 and right_angle > 80) and (right_position_angle < 20 and left_angle < 20)):
                            self.up = True
                        if ((left_position_angle > 80 and right_angle > 80) and (right_position_angle > 80 and left_angle > 80)) and self.up:
                            self.up = False
                            self.count += 1
                            self.calories_burned += calorie_counter("high_knee")

                        # Render detections
                        mp_drawing.draw_landmarks(self.image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                                  mp_drawing.DrawingSpec(
                                                      color=(245, 117, 66), thickness=2, circle_radius=2),
                                                  mp_drawing.DrawingSpec(
                                                      color=(245, 66, 230), thickness=2, circle_radius=2)
                                                  )
                    except:
                        pass

                    self.draw_counter()

                    # print(self.counter)
                    if self.counter == 0:
                        cap.release()
                        # cv2.destroyAllWindows()
                    if not self.callibration_check:
                        self.draw_initial_text()
                    else:
                        self.draw_reps_and_calories()

                    try:
                        FRAME_WINDOW.image(cv2.cvtColor(
                            self.image, cv2.COLOR_BGR2RGB))
                    except:
                        FRAME_WINDOW.empty()
                        break
                else:
                    break

                    # cv2.imshow('Exercise Feed', self.image)

                    # if cv2.waitKey(10) & 0xFF == ord('q'):
                    #     break

            cap.release()
            FRAME_WINDOW.empty()

            if self.count > 0:
                st.header("")
                st.header("")
                _, output_col1, output_col2, _ = st.columns(4)
                with output_col1:
                    st.metric(label="Total Rep Count", value=str(self.count))
                with output_col2:
                    st.metric(label="Caloried Burned",
                              value=str(self.calories_burned)[:5])
            # cv2.destroyAllWindows()
