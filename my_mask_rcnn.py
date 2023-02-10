_base_ = [
    '../_base_/models/mask_rcnn_r50_fpn.py',
    '../_base_/datasets/coco_instance.py',
    '../_base_/schedules/schedule_1x.py', '../_base_/default_runtime.py'
]

model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=1),
        mask_head=dict(num_classes=1))
)
# my change
dataset_type = 'CocoDataset'
num_classes = 1
classes = ('balloon',)
data_root = 'E:/python-project/other/mmdetection-master/data/balloon/'
data = dict(
    samples_per_gpu=1,
    workers_per_gpu=0,
    train=dict(
        type=dataset_type,
        classes=classes,
        ann_file=data_root + 'train/train.json',
        img_prefix=data_root + 'train/',
        ),
    val=dict(
        type=dataset_type,
        ann_file=data_root + 'val/val.json',
        classes=classes,
        img_prefix=data_root + 'val/',
        ),
    test=dict(
        type=dataset_type,
        ann_file=data_root + 'val/val.json',
        img_prefix=data_root + 'val/',
        ))
