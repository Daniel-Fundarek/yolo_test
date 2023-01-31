import cv2
import numpy as np

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


def read_frame(vid_capture: cv2.VideoCapture):
    if not vid_capture.isOpened():
        print("Error opening the video file")
        return None
    else:
        # vCapture.read() methods returns a tuple, first element is a bool
        # and the second is frame
        ret, frame = vid_capture.read()
        if ret:
            return frame
        else:
            return None


def show_image(image):
    cv2.imshow("", image)


def scale_image(image, wh_size=None, xy_scale_factor=None):
    if wh_size is not None:
        return cv2.resize(image, wh_size, interpolation=cv2.INTER_LINEAR)
    elif xy_scale_factor is not None:
        if type(xy_scale_factor) is tuple:
            x_scale_factor = xy_scale_factor(0)
            y_scale_factor = xy_scale_factor(1)
            return cv2.resize(image, None, x_scale_factor, y_scale_factor, interpolation=cv2.INTER_LINEAR)
        elif type(xy_scale_factor) is float:
            x_scale_factor = xy_scale_factor
            y_scale_factor = xy_scale_factor
            new_image = cv2.resize(image, None, fx=x_scale_factor, fy=y_scale_factor, interpolation=cv2.INTER_LINEAR)
            return new_image
    else:
        return image


def image_size(image):
    return image.shape


def crop_image(image, crop_x1=0, crop_x2=0, crop_y1=0, crop_y2=0):
    y_max, x_max, c = image_size(image)
    x1 = 0
    x2 = x_max
    y1 = 0
    y2 = y_max

    if 0 < crop_x1 < x_max:
        x1 = crop_x1
    if 0 < crop_x2 < x_max:
        x2 = crop_x2
    if 0 < crop_y1 < y_max:
        y1 = crop_y1
    if 0 < crop_y2 < y_max:
        y2 = crop_y2
    return image[y1:y2, x1:x2]
