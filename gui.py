import PySimpleGUI as gui
import video_processing as vp


class MyGui:
    frame_height = 480
    frame_width = 400

    def __init__(self):
        layout = [
            [gui.Text("OpenCV Demo", size=(60, 1), justification="center")],
            [gui.Image(filename="", key="-IMAGE-")],
            [gui.Radio("None", "Radio", True, size=(10, 1))],
            [
                gui.Radio("threshold", "Radio", size=(10, 1), key="-THRESH-"),
                gui.Slider(range=(0, 255), default_value=128, orientation="h", size=(40, 15), key="-THRESH SLIDER-"),
            ],
            [
                gui.Radio("canny", "Radio", size=(10, 1), key="-CANNY-"),
                gui.Slider(
                    (0, 255),
                    128,
                    1,
                    orientation="h",
                    size=(20, 15),
                    key="-CANNY SLIDER A-",
                ),
                gui.Slider(
                    (0, 255),
                    128,
                    1,
                    orientation="h",
                    size=(20, 15),
                    key="-CANNY SLIDER B-",
                ),
            ],
            [
                gui.Radio("blur", "Radio", size=(10, 1), key="-BLUR-"),
                gui.Slider(
                    (1, 11),
                    1,
                    1,
                    orientation="h",
                    size=(40, 15),
                    key="-BLUR SLIDER-",
                ),
            ],
            [
                gui.Radio("hue", "Radio", size=(10, 1), key="-HUE-"),
                gui.Slider(
                    (0, 225),
                    0,
                    1,
                    orientation="h",
                    size=(40, 15),
                    key="-HUE SLIDER-",
                ),
            ],
            [
                gui.Radio("enhance", "Radio", size=(10, 1), key="-ENHANCE-"),
                gui.Slider(
                    (1, 255),
                    128,
                    1,
                    orientation="h",
                    size=(40, 15),
                    key="-ENHANCE SLIDER-",
                ),
            ],
            [
                gui.Checkbox('Resize', size=(13, 1), key="-RESIZE-"),
                gui.Slider(
                    (0.1, 2),
                    1,
                    0.01,
                    orientation="h",
                    size=(40, 15),
                    key="-RESIZE SLIDER-",
                ),
            ],
            [
                gui.Checkbox('Crop', size=(13, 1), key="-CROP-"),
                gui.Slider(
                    (0, self.frame_width),
                    0,
                    1,
                    orientation="h",
                    size=(20, 15),
                    key="-CROP RIGHT SLIDER-",
                    enable_events=True
                ),
                gui.Slider(
                    (0, self.frame_width),
                    0,
                    1,
                    orientation="h",
                    size=(20, 15),
                    key="-CROP LEFT SLIDER-",
                ),
                gui.Slider(
                    (0, self.frame_height),
                    0,
                    1,
                    orientation="h",
                    size=(20, 15),
                    key="-CROP UP SLIDER-",
                ),
                gui.Slider(
                    (0, self.frame_height),
                    0,
                    1,
                    orientation="h",
                    size=(20, 15),
                    key="-CROP DOWN SLIDER-",
                ),
            ],
            [gui.Button("Exit", size=(10, 1))],
        ]
        window = gui.Window("OpenCV Integration", layout, location=(800, 400))
        video_capture = vp.video_source_setup()
        while True:
            event, values = window.read(timeout=20)  # nutne aby sa zobrazilo okno a aby sa updatovali eventy z okna
            frame = vp.read_frame(video_capture)
            self.frame_height, self.frame_width, _ = vp.image_size(frame)
            self.update_gui(window, values)
            frame = self.modify_frame(frame, values, event)
            vp.show_image(frame)

            if event == "Exit" or event == gui.WIN_CLOSED:
                break
            if frame is None:
                break

        window.close()

    def update_gui(self, window, values):
        width_slider_limit = self.frame_width - values["-CROP RIGHT SLIDER-"] - values["-CROP LEFT SLIDER-"]
        height_slider_limit = self.frame_height - values["-CROP UP SLIDER-"] - values["-CROP DOWN SLIDER-"]
        window["-CROP RIGHT SLIDER-"].Update(range=(0, values["-CROP RIGHT SLIDER-"] + width_slider_limit))
        window["-CROP LEFT SLIDER-"].Update(range=(0, values["-CROP LEFT SLIDER-"] + width_slider_limit))
        window["-CROP UP SLIDER-"].Update(range=(0, values["-CROP UP SLIDER-"] + height_slider_limit))
        window["-CROP DOWN SLIDER-"].Update(range=(0, values["-CROP DOWN SLIDER-"] + height_slider_limit))

    def modify_frame(self, frame, values, event):
        if values["-RESIZE-"]:
            resize_factor = values["-RESIZE SLIDER-"]
            frame = vp.scale_image(frame, xy_scale_factor=resize_factor)
        if values["-CROP-"]:
            crop_left = int(values["-CROP LEFT SLIDER-"])
            crop_right = int(self.frame_width - values["-CROP RIGHT SLIDER-"])
            crop_up = int(values["-CROP UP SLIDER-"])
            crop_down = int(self.frame_height - values["-CROP DOWN SLIDER-"])
            frame = vp.crop_image(frame, crop_left, crop_right, crop_up, crop_down)
        return frame
