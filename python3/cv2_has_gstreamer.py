import cv2
import re
def has_gstreamer():
    match = re.findall("GStreamer:\s+YES", cv2.getBuildInformation())
    return bool(match)
