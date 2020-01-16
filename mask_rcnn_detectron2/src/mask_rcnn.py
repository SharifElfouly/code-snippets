import detectron2
from detectron2.utils.logger import setup_logger
setup_logger()

import numpy as np
import cv2
import random

from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog

class MaskRCNN:
    """Mask R-CNN (https://arxiv.org/abs/1703.06870) for instance segmentation."""
    def __init__(self, cfg_f, w, h, model_f=None, score_thresh=0.5):
        cfg = get_cfg()
        cfg.merge_from_file(model_zoo.get_config_file(cfg_f))
        cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = score_thresh
        cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url(cfg_f)
        self.mask_rcnn = DefaultPredictor(cfg)
        self.w, self.h = w, h

    def resize(self, img):
        """Resize a np `img` to (`self.w`, `self.h`)"""
        if img.shape[1] != self.w or img.shape[0] != self.h:
            img = cv2.resize(img, (self.w, self.h))
        return img

    def vis(self, img_arr, pred):
        """Draw `pred` on `img_arr`"""
        v = Visualizer(im[:, :, ::-1], MetadataCatalog.get(cfg.DATASETS.TRAIN[0]), scale=1.2)
        return v.draw_instance_predictions(outputs["instances"].to("cpu"))


    def predict(self, img):
        """Run inference on np `img`"""
        img = self.resize(img)
        return self.mask_rcnn(img)
