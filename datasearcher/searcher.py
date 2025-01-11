import os
import datetime
import glob
import json
import threading
from multiprocessing.pool import ThreadPool


def get_directory(desired_dir=None, day=None):
    if desired_dir == None:
        desired_dir = os.getcwd()
    if type(day) != str:
        day = day.strftime("%y%m%d")
    day_dir = desired_dir + "/days/" + day
    if (os.path.isdir(day_dir)):
        return day_dir
    return None


def get_last_10_days_directories(desired_dir=None, day=None):
    if day == None:
        day = datetime.datetime.today()
    else:
        day = datetime.datetime.strptime(day, "%y%m%d")
    directories = []
    for x in range(10):
        directory = get_directory(
            desired_dir=desired_dir, day=(day - datetime.timedelta(x)))
        if directory:
            directories.append(directory)
    return directories


def get_files_directories(files_directory):
    if files_directory:
        return glob.glob(files_directory + "/*.txt")


def read_and_search_file(file_dir, search_data):
    results = []
    with open(file_dir, "r") as file:
        lines = file.readlines()
        for line in range(len(lines)):
            json_object = json.loads(lines[line])
            if (json_object["id"] in search_data["ids"]):
                result = {
                    "match_key": "id",
                    "match_value": json_object["id"],
                    "match_file_dir": file_dir,
                    "match_file_line": line+1,
                    "match_line_data": json_object
                }
                results.append(result)
            for key, value in search_data["attributes"].items():
                if json_object["attributes"][key] == value:
                    result = {
                        "match_key": key,
                        "match_value": json_object["attributes"][key],
                        "match_file_dir": file_dir,
                        "match_file_line": line+1,
                        "match_line_data": json_object
                    }
                    results.append(result)
        return results


def check_and_create_output_directory(desired_dir=None):
    if desired_dir == None:
        desired_dir = os.getcwd()
    output_dir = desired_dir + "/output"
    if (os.path.isdir(output_dir) == False):
        os.mkdir(output_dir)
    return output_dir


def create_output_file(all_results=[], desired_dir=None):
    output_dir = check_and_create_output_directory(desired_dir=desired_dir)
    output_files_path = output_dir + "/report_file_" + \
        datetime.datetime.today().strftime("%y%m%d%H%M%S%f")[:-3] + ".txt"
    with open(output_files_path, "w") as f:
        for result in all_results:
            f.writelines(json.dumps(result)+"\n")
    print("Report Create: " + output_files_path)


def search_data(s_data, processes=1, desired_dir=None):
    all_results = []
    threads = []
    pool = ThreadPool(processes=processes)
    last_10_days_directories = get_last_10_days_directories()
    for last_10_days_directory in last_10_days_directories:
        sub_directories = get_files_directories(last_10_days_directory)
        for sub_directory in sub_directories:
            thread = pool.apply_async(
                read_and_search_file, (sub_directory, s_data))
            threads.append(thread)

    for thread in threads:
        all_results = all_results + thread.get()
    create_output_file(all_results=all_results, desired_dir=desired_dir)
