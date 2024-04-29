#%%STREAM from CAMERA 
import cv2

# RTSP URL of the stream
# structure is: rtsp://username:password@ip_address:port/path where path is often stream1 or stream2 with stream 1 being higher quality
rtsp_url = "rtsp://username:password@ip_address:port/path"

# Create a VideoCapture object
cap = cv2.VideoCapture(rtsp_url)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Couldn't open the RTSP stream.")
    exit()

# Loop to read and display frames
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break
    
    # Display the frame in fullscreen
    cv2.namedWindow('{COMPANY NAME} RTSP Feed', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('{COMPANY NAME} RTSP Feed', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow('{COMPANY NAME} RTSP Feed', frame)
    
    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close all windows
cap.release()
cv2.destroyAllWindows()
