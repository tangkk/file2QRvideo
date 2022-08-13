# Introduction

This project provides tools for converting a single file to a sequece of QRcodes (`file2QRvideo.py`) in `.avi` format video, and back (`QRvideo2file.py`).
If you have a folder of files, you'll first need to pack and compress them in a single file (such as `.zip` or `.tar`), then follow the "single file" process as above.

# Installation
You'll need python packages in `requirements.txt` to run the scripts.

# Usage
- To convert file to video, run:
```python file2QRvideo.py file video.avi```

- To convert video to file, run:
```python QRvideo2file.py video file```

Note that if you want to transfer the video, you can use a camera to shot the computer screen.
Make sure the camera stand still, and the video framerate is not over-high.
You can adjust the output framerate in the `file2QRvideo.py` script.

![Alt Text](https://github.com/tangkk/file2QRvideo/blob/main/testvideo.gif)

