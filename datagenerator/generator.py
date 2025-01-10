import os
import datetime
import random
import string
import uuid
import threading
from pathlib import Path


def create_directory(desired_dir=None, day=None):
    if desired_dir == None:
        desired_dir = os.getcwd()
    if day == None:
        day = datetime.datetime.today()
    if type(day) != str:
        day = day.strftime("%y%m%d")
    if (os.path.isdir(desired_dir + "/days") == False):
        os.mkdir(desired_dir + "/days")
    day_dir = desired_dir + "/days/" + day
    if (os.path.isdir(day_dir) == False):
        os.mkdir(day_dir)
    return day_dir


def divide_ids_list(ids_list, n):
    random.shuffle(ids_list)
    return [ids_list[i::n] for i in range(n)]


def random_value_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))


def get_or_create_ids_list(number_of_id=20000000, desired_dir=None):
    ids_list = []
    if desired_dir == None:
        desired_dir = os.getcwd()
    ids_list_file = Path(desired_dir + "/ids_list.txt")
    if ids_list_file.exists():
        f = open("ids_list.txt", "r")
        list_from_file = f.read()
        list_from_file = list_from_file.replace(
            "[", "").replace("]", "").replace(" ", "")
        ids_list = list_from_file.split(",")
    else:
        for x in range(number_of_id):
            ids_list.append(str(uuid.uuid4()))
        with open(ids_list_file, "w") as f:
            f.write(str(ids_list))
    return ids_list


def create_file(day_dir, file_number, ids_list):
    with open(day_dir + "/file" + str(file_number) + ".txt", "w") as f:
        for id in ids_list:
            val_0 = random_value_generator()
            val_1 = random_value_generator()
            val_2 = random_value_generator()
            val_3 = random_value_generator()
            val_4 = random_value_generator()
            val_5 = random_value_generator()
            val_6 = random_value_generator()
            val_7 = random_value_generator()
            val_8 = random_value_generator()
            val_9 = random_value_generator()
            data = '{"id": '+str(id)+',"attributes": {"val_0": '+val_0+',"val_1": '+val_1+',"val_2": '+val_2+',"val_3": '+val_3 + \
                ',"val_4": '+val_4+',"val_5": '+val_5+',"val_6": '+val_6 + \
                ',"val_7": '+val_7+',"val_8": '+val_8+',"val_9": '+val_9+'}}'
            f.writelines(str(data)+"\n")


def create_files(day_dir, ids_list):
    for x in range(1, 41):
        thread = threading.Thread(
            target=create_file, args=(day_dir, x, ids_list[x-1]))
        thread.start()


def generate_data(desired_dir=None, day=None, number_of_id=1000):
    day_dir = create_directory(desired_dir=desired_dir, day=day)
    ids_list = get_or_create_ids_list(
        number_of_id=number_of_id, desired_dir=desired_dir)
    ids_list = divide_ids_list(ids_list, 40)
    create_files(day_dir, ids_list)
