import cv2

from multipledispatch import dispatch


@dispatch()
def video_source_setup():
    """
    video source setup function without parameters create videocapture Object, with camera input source
    """
    vid_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    return vid_capture


@dispatch(str)
def video_source_setup(video_file_path):
    """
       video_file_path: str -> string which contains path and name of video file / pictures file name
       video source setup function with parameters create videocapture Object, with video or photos input source.
       sets of photos are defined: Cars%04d.jpg
    """
    vid_capture = cv2.VideoCapture(video_file_path)
    return vid_capture


def read_video(vid_capture: cv2.VideoCapture):
    if not vid_capture.isOpened():
        print("Error opening the video file")
        return
    else:
        # Get frame rate information
        fps = int(vid_capture.get(cv2.CAP_PROP_FPS))
        print("Frame Rate : ", fps, "frames per second")

        # Get frame count
        frame_count = vid_capture.get(cv2.CAP_PROP_FRAME_COUNT)
        print("Frame count : ", frame_count)

    while (vid_capture.isOpened()):
        # vCapture.read() methods returns a tuple, first element is a bool
        # and the second is frame

        ret, frame = vid_capture.read()
        if ret == True:
            cv2.imshow('Frame', frame)
            k = cv2.waitKey(20)
            # 113 is ASCII code for q key
            if k == 113:
                break
        else:
            break
