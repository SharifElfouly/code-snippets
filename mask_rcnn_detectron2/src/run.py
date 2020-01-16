from mask_rcnn import MaskRCNN
CFG_F = 'COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml'
m = MaskRCNN(CFG_F, 640, 320)


