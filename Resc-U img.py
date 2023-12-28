import face_recognition
import cv2
import numpy as np

def draw_landmarks(image, face_landmarks):
    for facial_feature in face_landmarks.keys():
        points = face_landmarks[facial_feature]
        for i in range(len(points) - 1):
            cv2.line(image, points[i], points[i+1], (0, 255, 0), 2)
        cv2.line(image, points[-1], points[0], (0, 255, 0), 2)

def process_image(image_path, target_height=600):
    image = face_recognition.load_image_file(image_path)
    face_landmarks_list = face_recognition.face_landmarks(image)
    
    image_cv2 = cv2.imread(image_path)

    for face_landmarks in face_landmarks_list:
        draw_landmarks(image_cv2, face_landmarks)

    current_height = image_cv2.shape[0]
    scale_factor = target_height / current_height
    image_cv2_resized = cv2.resize(image_cv2, (0, 0), fx=scale_factor, fy=scale_factor)

    return image_cv2_resized

image_paths = ["t.png", "y.png"]

def find_face_encodings(image_path):
    image = cv2.imread(image_path)
    face_enc = face_recognition.face_encodings(image)
    return face_enc[0]

image_1 = find_face_encodings("t.png")
image_2  = find_face_encodings("y.png")



distance = face_recognition.face_distance([image_1], image_2)
distance = round(distance[0] * 100)
accuracy = 100-round(distance)
print(f"[{accuracy}% Match]✅")

images = [process_image(image_path) for image_path in image_paths]
concatenated_image = np.concatenate(images, axis=1)

text_to_display = f"{str(accuracy)}% Match"
cv2.putText(concatenated_image, text_to_display, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 73), 2, cv2.LINE_AA)

cv2.putText(concatenated_image, "Resc-U | AI for Good", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 73), 2, cv2.LINE_AA)


cv2.imshow('Resc-U Image Recognition Model', concatenated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()