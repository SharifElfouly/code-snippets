from mmdet.apis import init_detector, inference_detector, show_result_pyplot, show_result
import mmcv

config_file = '/workspaces/detectro-rs-docker/DetectoRS_mstrain_400_1200_x101_32x4d_40e.py'
checkpoint_file = '/workspaces/detectro-rs-docker/DetectoRS_X101-ed983634.pth'

# build the model from a config file and a checkpoint file
model = init_detector(config_file, checkpoint_file, device='cuda:0')

# test a single image and show the results
img = '/workspaces/detectro-rs-docker/pp.png' 

result = inference_detector(model, img)

show_result(img, result, model.CLASSES, out_file='out.png')
