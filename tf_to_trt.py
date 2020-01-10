import tensorflow as tf
from tensorflow.python.compiler.tensorrt import trt_convert as trt

params = trt.DEFAULT_TRT_CONVERSION_PARAMS._replace(
    precision_mode='FP16')

converter = tf.experimental.tensorrt.Converter(
    input_saved_model_dir="./tf_model/saved_model", conversion_params=params)
converter.convert()
converter.save('./trt_model')
