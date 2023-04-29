import os
from tqdm import tqdm

from sklearn.model_selection import train_test_split
from shutil import copyfile

# 先执行voc2yolo在执行该代码进行划分

# 功能: 递归穿件目录文件，有则跳过，没有则创建并验证
def _mkdir(dirpath):
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)
        assert os.path.exists(dirpath), "{} create fail.".format(dirpath)


# 功能: 从图片路径中获取最后的文件名(含后缀或者不含后缀)
def get_filename(filepath, suffix=True):
    if suffix is True:
        image_id = filepath.split('\\')[-1]     # 获取文件名(含后缀)
    else:
        image_id = filepath.split('\\')[-1].split('.')[0]   # 获取文件名(不含后缀)
    return image_id


# 功能: 根据图片数据与标签数据构建yolov5格式的数据集
# imagepath: 存放数据图片的路径
# labelpath: 存放数据标签的路径
# datasetpath: 构建voc格式数据集的目录路径
def dataset_split(imagepath, imagepath_test, labelpath, datasetpath):

    assert os.path.exists(imagepath), "{} not exists.".format(imagepath)
    assert os.path.exists(imagepath_test), "{} not exists.".format(imagepath_test)
    assert os.path.exists(labelpath), "{} not exists.".format(labelpath)

    # 构建图片与标签的路径列表
    # 训练集
    file = open(r"D:\DIOR\DIORdata\ImageSets\Main\train.txt", mode='r', encoding='UTF-8')
    train_list = []
    # 读取所有行(直到结束符 EOF)并返回列表
    contents = file.readlines()
    print(contents)
    for msg in contents:
        # 删除结尾的\n字符
        msg = msg.strip('\n')
        # # 字符串根据空格进行分割
        # adm = msg.split(' ')
        # admin.append(adm)
        train_list.append(msg)
    file.close()

    # images = os.listdir(imagepath)
    imagelists_train = [os.path.join(imagepath, image +".jpg") for image in train_list]
    labellists_train = [os.path.join(labelpath, image +".txt") for image in train_list]
    assert len(imagelists_train) != 0, "{} have no files".format(imagepath)

    file = open(r"D:\DIOR\DIORdata\ImageSets\Main\val.txt", mode='r', encoding='UTF-8')
    val_list = []
    # 读取所有行(直到结束符 EOF)并返回列表
    contents = file.readlines()
    print(contents)
    for msg in contents:
        # 删除结尾的\n字符
        msg = msg.strip('\n')
        # # 字符串根据空格进行分割
        # adm = msg.split(' ')
        # admin.append(adm)
        val_list.append(msg)
    file.close()

    # images = os.listdir(imagepath)
    imagelists_val = [os.path.join(imagepath, image + ".jpg") for image in val_list]
    labellists_val = [os.path.join(labelpath, image + ".txt") for image in val_list]
    assert len(imagelists_val) != 0, "{} have no files".format(imagepath)

    file = open(r"D:\DIOR\DIORdata\ImageSets\Main\test.txt", mode='r', encoding='UTF-8')
    test_list = []
    # 读取所有行(直到结束符 EOF)并返回列表
    contents = file.readlines()
    print(contents)
    for msg in contents:
        # 删除结尾的\n字符
        msg = msg.strip('\n')
        # # 字符串根据空格进行分割
        # adm = msg.split(' ')
        # admin.append(adm)
        test_list.append(msg)
    file.close()

    # images_test = os.listdir(imagepath_test)
    imagelists_test = [os.path.join(imagepath_test, image + ".jpg") for image in test_list]
    labellists_test = [os.path.join(labelpath, image + ".txt") for image in test_list]
    assert len(imagelists_test) != 0, "{} have no files".format(imagepath)



    # 构建voc格式的数据集存放格式
    _mkdir(datasetpath)
    # 在数据路径datasetpath下，分别递归建立目录:
    # | -----Dataset
    #       | -----images
    #           | -----train
    #           | -----val
    #           | -----test
    #       | -----labels
    #           | -----train
    #           | -----val
    #           | -----test
    images_train_dirpath = os.path.join(datasetpath, "images", "train")
    _mkdir(images_train_dirpath)
    images_val_dirpath = os.path.join(datasetpath, "images", "val")
    _mkdir(images_val_dirpath)
    images_test_dirpath = os.path.join(datasetpath, "images", "test")
    _mkdir(images_test_dirpath)
    labels_train_dirpath = os.path.join(datasetpath, "labels", "train")
    _mkdir(labels_train_dirpath)
    labels_val_dirpath = os.path.join(datasetpath, "labels", "val")
    _mkdir(labels_val_dirpath)
    labels_test_dirpath = os.path.join(datasetpath, "labels", "test")
    _mkdir(labels_test_dirpath)

    # 复制图片/标签列表中的数据到指定子目录下
    for image_path in tqdm(imagelists_train, desc="process train images"):
        image_newpath = os.path.join(images_train_dirpath, get_filename(image_path))
        copyfile(image_path, image_newpath)
    for image_path in tqdm(imagelists_val, desc="process val images"):
        image_newpath = os.path.join(images_val_dirpath, get_filename(image_path))
        copyfile(image_path, image_newpath)
    for image_path in tqdm(imagelists_test, desc="process test images"):
        image_newpath = os.path.join(images_test_dirpath, get_filename(image_path))
        copyfile(image_path, image_newpath)
    for image_path in tqdm(labellists_train, desc="process train labels"):
        image_newpath = os.path.join(labels_train_dirpath, get_filename(image_path))
        copyfile(image_path, image_newpath)
    for image_path in tqdm(labellists_val, desc="process val labels"):
        image_newpath = os.path.join(labels_val_dirpath, get_filename(image_path))
        copyfile(image_path, image_newpath)
    for image_path in tqdm(labellists_test, desc="process test labels"):
        image_newpath = os.path.join(labels_test_dirpath, get_filename(image_path))
        copyfile(image_path, image_newpath)

    print("Process Success. The data has save to {}".format(datasetpath))


if __name__ == '__main__':

    imagepath = r"D:\DIOR\DIORdata\JPEGImages-trainval"
    imagepath_test = r"D:\DIOR\DIORdata\JPEGImages-test"
    labelpath = r"D:\DIOR\DIORdata\YoloLabels"
    datasetpath = r"D:\DIOR\DIORdata\Dataset"
    dataset_split(imagepath, imagepath_test,labelpath, datasetpath)
