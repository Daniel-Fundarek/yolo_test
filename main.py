# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import video_processing as vp
def main_fcn():
    # Use a breakpoint in the code line below to debug your script.
    video_capture = vp.video_source_setup()
    vp.read_video(video_capture)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main_fcn()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
