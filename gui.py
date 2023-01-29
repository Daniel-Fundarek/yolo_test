import PySimpleGUI as gui
import video_processing as vp

class MyGui:

    def __init__(self):
        gui.theme("DarkGrey")

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
            [gui.Button("Exit", size=(10, 1))],
        ]
        window = gui.Window("OpenCV Integration", layout, location=(800, 400))
        video_capture = vp.video_source_setup()
        while True:
            event, values = window.read(timeout=20)  # nutne aby sa zobrazilo okno a aby sa updatovali eventy z okna
            if event == "Exit" or event == gui.WIN_CLOSED:
                break
            if not vp.read_video(video_capture):
                break

        window.close()
