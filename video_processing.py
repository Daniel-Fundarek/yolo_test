import cv2


def read_video():
    vid_capture = cv2.VideoCapture('Resources/Image_sequence/Cars%04d.jpg')
    vid_capture = cv2.VideoCapture('Resources/Cars.mp4')
    vid_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)


def read_video(video_file: str):
    vid_capture = cv2.VideoCapture('Resources/Image_sequence/Cars%04d.jpg')
