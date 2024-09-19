import cv2
import json
import pathlib
import argparse

"""
gets a video file and dumps each frame as a png picture in an output dir
"""

parser = argparse.ArgumentParser()

parser.add_argument('-i', '--video_path', help="Path to the input video file",   type=str)
parser.add_argument('-o', '--image_path', help="Path to image output dis",       type=str, default="./")
parser.add_argument('-d', '--decimator',  help="Save only one every _d_ frames", type=int, default=1)
parser.add_argument('-s', '--image_size', help="Output image square resolution", type=int, default=1920)
parser.add_argument('--iod', help="Master config dict, overrides other args",   type=str, nargs='+')

args = parser.parse_args()
iod = json.loads(" ".join(args.iod)) if args.iod else{}

video_path = iod.get("video_path", args.video_path)
image_path = iod.get("image_path", args.image_path)
decimator  = iod.get("decimator",  args.decimator) 
image_size = iod.get("image_size", args.image_size) 
assert(video_path and image_path)


if __name__ == "__main__":
    pathlib.Path(image_path).mkdir(parents=True, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    print("    Converting video to frames... ")
    while(cap.isOpened()):

        ret, frame = cap.read()
        if ret == False:
            break

        if frame_count % decimator == 0:
            frame = cv2.resize(frame, (image_size, image_size))
            cv2.imwrite(f"{image_path}/{frame_count:05}.png", frame)

        frame_count += 1

    cap.release()
    
    print("    Done!")
