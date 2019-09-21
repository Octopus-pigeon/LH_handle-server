import csv
import os

eeg_file_path = "../file/eeg-data.csv"
eye_file_path = "../file/eye-data.csv"
gesture_file_path = "../file/gesture-data.csv"


# 订阅eeg类型数据存入csv
def store_data(data, csv_path, seq):
    data_list = [seq] + [data['time']] + data['eeg']
    csv_file = open(csv_path, 'a', newline='')
    writer = csv.writer(csv_file, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(data_list)
    # csv_file.close()
    print("保存数据成功，处理结束")


def data_sort_file(home_path):
    """
    # 将原始的csv文件数据，根据maker删选出上下左右四个csv文件
    :param home_path: 当前用户文件夹路径
    """
    source_data_path = home_path + '\\source_data\\source_data.csv'
    data_file = open(source_data_path, 'r')
    csv_reader = csv.reader(data_file)

    # 获得标记，开始记录数据标志  上 下 左 右
    start_record_up = False
    start_record_down = False
    start_record_left = False
    start_record_right = False
    # 处理数据次数，每处理一段数据存一个文件
    up_count = 0
    down_count = 0
    left_count = 0
    right_count = 0

    # 需要处理14个触点通道的数据 上 下 左 右
    data_up = []
    data_down = []
    data_left = []
    data_right = []

    for row in csv_reader:

        # 判断读取哪个marker
        if start_record_up:
            data_up.append(row[5:19])
        elif start_record_down:
            data_down.append(row[5:19])
        elif start_record_left:
            data_left.append(row[5:19])
        elif start_record_right:
            data_right.append(row[5:19])
        # print(row)
        # 根据marker值 开始取一段数据
        if row[20] == '1.0':
            data_up.append(row[5:19])
            start_record_up = True
            continue
        elif row[20] == '2.0':
            data_down.append(row[5:19])
            start_record_down = True
            continue
        elif row[20] == '3.0':
            data_left.append(row[5:19])
            start_record_left = True
            continue
        elif row[20] == '4.0':
            data_right.append(row[5:19])
            start_record_right = True
            continue

        # 结束的marker 后面的数据不要，并将此段数据保存为csv
        if row[20] == '11.0':
            start_record_up = False
            up_count = up_count + 1
            # 保存
            path = home_path + '\\sort_by_label\\up_data' + str(up_count) + '.csv'
            if os.path.exists(path):
                os.remove(path)
            label_data_csv(path, data_up)
            data_up.clear()
            continue
        elif row[20] == '22.0':
            start_record_down = False
            down_count = down_count + 1
            # 保存
            path = home_path + '\\sort_by_label\\down_data' + str(down_count) + '.csv'
            if os.path.exists(path):
                os.remove(path)
            label_data_csv(path, data_down)
            data_down.clear()
            continue
        elif row[20] == '33.0':
            start_record_left = False
            left_count = left_count + 1
            # 保存
            path = home_path + '\\sort_by_label\\left_data' + str(left_count) + '.csv'
            if os.path.exists(path):
                os.remove(path)
            label_data_csv(path, data_left)
            data_left.clear()
            continue
        elif row[20] == '44.0':
            start_record_right = False
            right_count = right_count + 1
            # 保存
            path = home_path + '\\sort_by_label\\right_data' + str(right_count) + '.csv'
            if os.path.exists(path):
                os.remove(path)
            label_data_csv(path, data_right)
            data_right.clear()
            continue


# 各类型数据的保存
def label_data_csv(csv_path, data_list):
    if os.path.exists(csv_path):
        os.remove(csv_path)
    csv_file = open(csv_path, 'a', newline='')
    writer = csv.writer(csv_file, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    for row in data_list:
        writer.writerow(row)
    csv_file.close()
    print('---' + csv_path + "文件保存成功，处理结束")


def init_file():
    if os.path.exists(eeg_file_path):
        os.remove(eeg_file_path)
    if os.path.exists(eye_file_path):
        os.remove(eye_file_path)
    if os.path.exists(gesture_file_path):
        os.remove(gesture_file_path)
