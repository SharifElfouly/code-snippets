import numpy as np
import tensorflow as tf
from PIL import Image

interpreter = tf.lite.Interpreter(model_path="/workspaces/tflite/mobilenet_v1_1.0_224.tflite")
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

sz = input_details[0]['shape']
w,h = sz[1],sz[2]

img_arr = np.array(Image.open('test/test.png').resize((w,h)), dtype=np.float32).reshape(sz)
interpreter.set_tensor(input_details[0]['index'], img_arr)

interpreter.invoke()
output_data = interpreter.get_tensor(output_details[0]['index'])
print(output_data.shape)

