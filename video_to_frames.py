import os
from PIL import Image
import cv2

VIDEO_F = '/media/sharif/Elements 1 TB/Verkehrsuebungsplatz_Sequenzen/Avigilon/THC_640S_H4A_BO12/IR_H5A_BO02_AVI.avi'
OUT_DIR = '/home/sharif/Documents/Verkehrsuebungsplatz-Auswertung/Avigilon/THC_640S_H4A_BO12/IR_H5A_BO02_AVI'
N_TO_SKIP = 9

def video_to_frames(video_f, out_dir, n_to_skip=0, verbose=True):
    'Split `video_f` into frames and save to `out_dir`.'
    i = 0
    n_img_saved = 0
    cap = cv2.VideoCapture(video_f)
    while(cap.isOpened()):
        ret, frame = cap.read()
        if i % (N_TO_SKIP+1) == 0: 
            img = Image.fromarray(frame)
            img = img.resize((800, 450))
            img.save(os.path.join(OUT_DIR, str(i) + '.png'))
            print(f'n_img_saved: {n_img_saved}')
            n_img_saved += 1
        i += 1

if __name__ == '__main__':
    video_to_frames(VIDEO_F, OUT_DIR, N_TO_SKIP)