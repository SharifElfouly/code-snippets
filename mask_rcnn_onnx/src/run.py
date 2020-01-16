import numpy as np
from PIL import Image
import math
import onnxruntime as rt
from PIL import Image

MODEL_F = '/home/sharif/Documents/mask_rcnn_onnx/src/model/mask_rcnn_R_50_FPN_1x.onnx'
IMG_F = '/home/sharif/Documents/mask_rcnn_onnx/test/test.png'

def load_model(MODEL_F):
    return onnx.load(MODEL_F)

def preprocess(img):
    ratio = 800.0 / min(img.size[0], img.size[1])
    img = img.resize((int(ratio * img.size[0]), int(ratio * img.size[1])), Image.BILINEAR)
    img = np.array(img)[:, :, [2, 1, 0]].astype('float32')
    img = np.transpose(img, [2, 0, 1])
    mean_vec = np.array([102.9801, 115.9465, 122.7717])
    for i in range(img.shape[0]):
        img[i, :, :] = img[i, :, :] - mean_vec[i]
    padded_h = int(math.ceil(img.shape[1] / 32) * 32)
    padded_w = int(math.ceil(img.shape[2] / 32) * 32)
    padded_image = np.zeros((3, padded_h, padded_w), dtype=np.float32)
    padded_image[:, :img.shape[1], :img.shape[2]] = img
    img = padded_image
    return img

def predict(img_arr):
    pass

if __name__ == '__main__':
    sess = rt.InferenceSession(MODEL_F)
    in_name = sess.get_inputs()[0].name
    img_arr = preprocess(Image.open(IMG_F))
    pred = sess.run(None, {in_name: img_arr})
    print(pred)
    