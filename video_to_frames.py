import os
from PIL import Image
import cv2

VIDEO_F = '/media/sharif/Elements 1 TB/Verkehrsuebungsplatz_Sequenzen/Axis/Axis_Q1942_E_1923_2020.avi' 
OUT_DIR = '/home/sharif/Documents/Verkehrsuebungsplatz-Auswertung/Axis/Axis_Q1942_E_1850_1915'
N_TO_SKIP = 4
SZ = (800,450)

def video_to_frames(video_f, out_dir, n_to_skip=0, verbose=True):
    'Split `video_f` into frames and save to `out_dir`.'
    i = 0
    n_img_saved = 0
    cap = cv2.VideoCapture(video_f)
    while(cap.isOpened()):
        try:
            ret, frame = cap.read()
            if i % (N_TO_SKIP+1) == 0: 
                img = Image.fromarray(frame)
                img = img.resize(SZ)
                img.save(os.path.join(OUT_DIR, str(i) + '.png'))
                if verbose: print(f'n_img_saved: {n_img_saved}')
                n_img_saved += 1
        except Exception as e: print(e)
        i += 1

if __name__ == '__main__':
    video_to_frames(VIDEO_F, OUT_DIR, N_TO_SKIP)
