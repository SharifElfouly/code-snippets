import caffe

MODEL_DESC = 'src/data/deploy.prototxt'
MODEL_F = 'src/data/mobilenet_iter_73000.caffemodel'

with change_env('GLOG_minloglevel', '2'):
    import caffe
    caffe.set_mode_cpu()
    net = caffe.Net(model_desc, model_file, caffe.TEST)
param_dict = CaffeLayerProcessor(net).process()
logger.info("Model loaded from caffe. Params: " +
            ", ".join(sorted(param_dict.keys())))