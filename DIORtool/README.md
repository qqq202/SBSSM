# SBSSM
## 1 data prepare
### base dataset
* Modify utils\dataloaders.py include_class = [] to fill in the base class to block new classes;   remember to reset to empty when fine-tuning to properly read all class tags  
* 修改utils\dataloaders.py的include_class = [] 填入基类，以屏蔽新类；  微调时记得重置为空，以正确读取所有类标签  
### noval dataset
* Use prepare_voc_few_shot.py migrated from [https://github.com/ucbdrive/few-shot-object-detection](url) to get few-shot data
* Use voc2yolo.py to convert the tag format
* Use voc2YOLO_dataset_split.py to split dataset by as-is
* Use count_instants_num.py kshot_instants.py to eliminate redundant instances from images例
* 使用迁移自[https://github.com/ucbdrive/few-shot-object-detection](url)的prepare_voc_few_shot.py获取少样本数据
* 使用 voc2yolo.py 转换标签格式
* 使用 voc2YOLO_dataset_split.py 按原样划分数据集
* 使用 count_instants_num.py kshot_instants.py 剔除图像中多余实例
