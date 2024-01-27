import cv2

def list_camera_indices():
    # Try accessing cameras from index 0 to 10
    for i in range(10):
        cap = cv2.VideoCapture(i)
        if not cap.isOpened():
            break
        cap.release()
        print(f"Camera index {i} is available.")

if __name__ == "__main__":
    list_camera_indices()
