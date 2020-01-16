INPUT_DIR="/workspaces/mask_rcnn_detectron/src/test"
OUTPUT_DIR="/workspaces/mask_rcnn_detectron/vis"
CFG="Detectron/configs/12_2017_baselines/e2e_mask_rcnn_R-101-FPN_2x.yaml"

python Detectron/tools/infer_simple.py \
     $INPUT_DIR \
    --cfg  $CFG\
    --output-dir $OUTPUT_DIR \
    --image-ext png \
    --wts https://dl.fbaipublicfiles.com/detectron/35861858/12_2017_baselines/e2e_mask_rcnn_R-101-FPN_2x.yaml.02_32_51.SgT4y1cO/output/train/coco_2014_train:coco_2014_valminusminival/generalized_rcnn/model_final.pkl \
    