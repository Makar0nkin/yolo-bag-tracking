from ultralytics import solutions
import cv2 
import argparse
import os

os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

def count_objects_in_region(input_video_path, output_video_path, model_path):
    """Count objects in a specific region within a video."""
    cap = cv2.VideoCapture(input_video_path)
    assert cap.isOpened(), "Error reading video file"
    w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
    video_writer = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

    region_points = [(200, 100), (450, 100)]
    counter = solutions.ObjectCounter(region=region_points, model=model_path)

    while cap.isOpened():
        success, im0 = cap.read()
        if not success:
            print("Video frame is empty or video processing has been successfully completed.")
            break
        im0 = counter.count(im0)
        video_writer.write(im0)

    cap.release()
    video_writer.release()
    cv2.destroyAllWindows()

parser = argparse.ArgumentParser(
    prog='tracker',
    description='Track and count bags on video',
    epilog="Example: python track.py -i video\input.mp4 -o video\output.mp4")

parser.add_argument('-i', '--input', help='relative path to input video for tracking', required=True) 
parser.add_argument('-o', '--output', help='relative path to output video', required=True) 

args = parser.parse_args()

count_objects_in_region(args.input, args.output, "best.pt")