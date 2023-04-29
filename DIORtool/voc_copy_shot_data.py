import os
from tqdm import tqdm

from sklearn.model_selection import train_test_split
from shutil import copyfile

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

shot_path = r"D:\DIOR\DIORdata\vocsplit\seed1"
img_path = r"D:\DIOR\Dataset\images\train"
label_path = r"D:\DIOR\Dataset\labels\train"

name_5shot=[]
name_10shot=[]
name_20shot=[]
img_5shot=[]
img_10shot=[]
img_20shot=[]

for name in os.listdir(shot_path):
    name_list = name.split('_')
    key = name_list[1]
    if key=="5shot":
        file_path = os.path.join(shot_path,name)
        file = open(file_path, mode='r', encoding='UTF-8')
        # 读取所有行(直到结束符 EOF)并返回列表
        contents = file.readlines()
        for msg in contents:
            # 删除结尾的\n字符
            msg = msg.split("/")
            msg = msg[-1]
            msg = msg.strip('.jpg\n')
            print(msg)
            img_5shot.append(msg)
        file.close()
    elif key=="10shot":
        file_path = os.path.join(shot_path,name)
        file = open(file_path, mode='r', encoding='UTF-8')
        # 读取所有行(直到结束符 EOF)并返回列表
        contents = file.readlines()
        for msg in contents:
            # 删除结尾的\n字符
            msg = msg.split("/")
            msg = msg[-1]
            msg = msg.strip('.jpg\n')
            print(msg)
            img_10shot.append(msg)
        file.close()
    elif key=="20shot":
        file_path = os.path.join(shot_path,name)
        file = open(file_path, mode='r', encoding='UTF-8')
        # 读取所有行(直到结束符 EOF)并返回列表
        contents = file.readlines()
        for msg in contents:
            # 删除结尾的\n字符
            msg = msg.split("/")
            msg = msg[-1]
            msg = msg.strip('.jpg\n')
            print(msg)
            img_20shot.append(msg)
        file.close()

print("5shot:",img_5shot)
print("10shot:",img_10shot)
print("20shot:",img_20shot)

imagelists_5 = [os.path.join(img_path, image +".jpg") for image in img_5shot]
labellists_5 = [os.path.join(label_path, image +".txt") for image in img_5shot]
imagelists_10 = [os.path.join(img_path, image +".jpg") for image in img_10shot]
labellists_10 = [os.path.join(label_path, image +".txt") for image in img_10shot]
imagelists_20 = [os.path.join(img_path, image +".jpg") for image in img_20shot]
labellists_20 = [os.path.join(label_path, image +".txt") for image in img_20shot]

images_5_dirpath = r"D:\DIOR\5shot\5shotimg"
_mkdir(images_5_dirpath)
images_10_dirpath = r"D:\DIOR\10shot\10shotimg"
_mkdir(images_10_dirpath)
images_20_dirpath = r"D:\DIOR\20shot\20shotimg"
_mkdir(images_20_dirpath)
label_5_dirpath = r"D:\DIOR\5shot\5shotlab"
_mkdir(label_5_dirpath)
label_10_dirpath = r"D:\DIOR\10shot\10shotlab"
_mkdir(label_10_dirpath)
label_20_dirpath = r"D:\DIOR\20shot\20shotlab"
_mkdir(label_20_dirpath)

# 复制图片/标签列表中的数据到指定子目录下
for image_path in tqdm(imagelists_5, desc="process 5 images"):
    image_newpath = os.path.join(images_5_dirpath, get_filename(image_path))
    copyfile(image_path, image_newpath)
for image_path in tqdm(imagelists_10, desc="process 10 images"):
    image_newpath = os.path.join(images_10_dirpath, get_filename(image_path))
    copyfile(image_path, image_newpath)
for image_path in tqdm(imagelists_20, desc="process 20 images"):
    image_newpath = os.path.join(images_20_dirpath, get_filename(image_path))
    copyfile(image_path, image_newpath)
for image_path in tqdm(labellists_5, desc="process 5 images"):
    image_newpath = os.path.join(label_5_dirpath, get_filename(image_path))
    copyfile(image_path, image_newpath)
for image_path in tqdm(labellists_10, desc="process 10 images"):
    image_newpath = os.path.join(label_10_dirpath, get_filename(image_path))
    copyfile(image_path, image_newpath)
for image_path in tqdm(labellists_20, desc="process 20 images"):
    image_newpath = os.path.join(label_20_dirpath, get_filename(image_path))
    copyfile(image_path, image_newpath)