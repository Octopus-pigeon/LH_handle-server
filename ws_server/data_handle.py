import datetime
import json
import queue

# 待处理数据队列
from utils.csv_util import store_data, eeg_file_path

data_handle_queue = queue.Queue()

# 手势信号
data_gesture = []
# 眼电信号
data_eye = []
# 脑电信号
data_eeg = []
# 一个数据处理单元: 一个数据单元包括三种数据源，进行一次处理生成cad指令
data_unit = [data_eeg, data_eye, data_gesture]


def message_handle(message):
    """
    处理接收到客户端的数据，数据格式
    {"client":1，"data":   "dataString"}
    脑电：1
    眼动：2
    手势：3
    :param message:
    """
    receive_data = json.loads(message)
    if type(receive_data) is not dict:
        print("接收数据错误: " + str(receive_data) + "--" + str(datetime.datetime.now()))
        return
    try:
        if receive_data["client"] == 1:
            print("接收到脑电信号：\n")
            print(receive_data["data"])
            data = json.loads(receive_data["data"])

            # 数据暂存，正式运行去掉，影响性能
            store_data(data, eeg_file_path, 1)

            # todo  信号处理，并存入一个信号处理单元
            data_eeg.append(receive_data["data"])

        elif receive_data["client"] == 2:
            print("接收到眼动信号：\n")
            print(receive_data["data"])
            # todo  信号处理，并存入一个信号处理单元
            data_eye.append(receive_data["data"])
        elif receive_data["client"] == 3:
            print("接收到手势信号：\n")
            print(receive_data["data"])
            # todo  信号处理，并存入一个信号处理单元
            data_gesture.append(receive_data["data"])
    except  Exception as e:
        print(e)
        return


def data_unit_listener():
    """
    监听信号收集情况，收集完成一个数据单元后，放入队列，进行后续处理逻辑
    """
    while True:
        # 去三种信号在数据单元中的长度，当长度满足处理要求时，放入信号识别队列
        eeg_length = len(data_unit[0])
        eye_length = len(data_unit[1])
        gesture_length = len(data_unit[2])

        #     长度根据需要定义,根据处理维度
        if eeg_length == 1 & eye_length == 2 & gesture_length == 3:
            data_handle_queue.put(data_unit)


def data_to_cad():
    """
    从队列中取出数据进行信号判别
    """
    data = data_handle_queue.get()
    if data:
        print("处理队列中的数据" + json.dumps(data))


