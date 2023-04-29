import os

txt_path = r'E:\wyh\DIOR\20shot\20shotlab\\'  # txt文件所在路径
new_txt_path = r'E:\wyh\DIOR\20shot\20shotlabnew\\'  # 新的txt文件所在路径
if not os.path.exists(new_txt_path):  # os模块判断并创建
    os.mkdir(new_txt_path)
class_num = 20  # 样本类别数
shot_num = 20 # 每个类别应该读取的数量
class_list = [i for i in range(class_num)] # 类别编号
class_num_list = [0 for i in range(class_num)] # 统计个数
labels_list = os.listdir(txt_path)
for i in labels_list:
    file_path = os.path.join(txt_path, i)
    file = open(file_path, 'r')  # 打开文件
    file_data = file.readlines()  # 读取所有行
    for every_row in file_data:
        # 读取该行并统计
        class_val = every_row.split(' ')[0]
        class_ind = class_list.index(int(class_val))
        class_num_list[class_ind] += 1

        file_path1 = os.path.join(new_txt_path, i)
        # file1 = open(file_path1, "w", encoding='utf-8') 会抹除旧内容,不用
        file1 = open(file_path1, "a+", encoding='utf-8')
        if  class_num_list[class_ind] < shot_num +1:
            file1.write(every_row)
            file1.close()

    file.close()
# 输出每一类的数量以及总数
print(class_num_list)
print('total:', sum(class_num_list))