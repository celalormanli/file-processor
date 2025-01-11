import unittest
import tempfile
import os
from datasearcher.searcher import *
from datagenerator.generator import *


class TestSearcherMethods(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def test_get_directory(self):
        dir1 = get_directory(desired_dir=self.test_dir,
                             day=datetime.datetime.today())
        self.assertIsNone(dir1)
        created_directory = create_directory(desired_dir=self.test_dir)
        dir2 = get_directory(desired_dir=self.test_dir,
                             day=datetime.datetime.today())
        self.assertEqual(created_directory, dir2)

    def test_get_last_10_days_directories(self):
        last_10_days_directories1 = get_last_10_days_directories(
            desired_dir=self.test_dir)
        self.assertEqual(len(last_10_days_directories1), 0)
        created_directory = create_directory(desired_dir=self.test_dir)
        last_10_days_directories2 = get_last_10_days_directories(
            desired_dir=self.test_dir)
        self.assertEqual(len(last_10_days_directories2), 1)
        self.assertIn(created_directory, last_10_days_directories2)

    def test_get_files_directories(self):
        dir = create_directory(desired_dir=self.test_dir)
        ids_list = get_or_create_ids_list(
            number_of_id=6, desired_dir=self.test_dir)
        ids_list = divide_ids_list(ids_list, 40)
        create_files(day_dir=dir, ids_list=ids_list)
        files_directories = get_files_directories(files_directory=dir)
        self.assertEqual(len(files_directories), 40)

    def test_read_and_search_file(self):
        dir = create_directory(desired_dir=self.test_dir)
        ids_list = get_or_create_ids_list(
            number_of_id=6, desired_dir=self.test_dir)
        ids_list = divide_ids_list(ids_list, 40)
        create_files(day_dir=dir, ids_list=ids_list)
        files_directories = get_files_directories(files_directory=dir)
        s_data1 = {}
        with open(files_directories[0], "r") as file:
            lines = file.readlines()
            data = json.loads(lines[0])
            s_data1 = {
                "ids": [data["id"]],
                "attributes": data["attributes"]
            }
        searched_data1 = read_and_search_file(
            file_dir=files_directories[0], search_data=s_data1)
        self.assertEqual(len(searched_data1), 11)

        s_data2 = {}
        with open(files_directories[0], "r") as file:
            lines = file.readlines()
            data = json.loads(lines[0])
            s_data2 = {
                "ids": [data["id"]],
                "attributes": {}
            }
        searched_data2 = read_and_search_file(
            file_dir=files_directories[0], search_data=s_data2)
        self.assertEqual(len(searched_data2), 1)

        s_data3 = {
            "ids": [],
            "attributes": {}
        }
        searched_data3 = read_and_search_file(
            file_dir=files_directories[0], search_data=s_data3)
        self.assertEqual(len(searched_data3), 0)

    def test_check_and_create_output_directory(self):
        output_dir = self.test_dir + "/output"
        self.assertFalse(os.path.isdir(output_dir))
        check_and_create_output_directory(desired_dir=self.test_dir)
        self.assertTrue(os.path.isdir(output_dir))

    def test_create_output_file(self):
        output_dir = self.test_dir + "/output"
        check_and_create_output_directory(desired_dir=self.test_dir)
        self.assertEqual(len(glob.glob(output_dir + "/*.txt")), 0)
        create_output_file(desired_dir=self.test_dir)
        self.assertEqual(len(glob.glob(output_dir + "/*.txt")), 1)

    def test_search_data(self):
        dir = create_directory(desired_dir=self.test_dir)
        ids_list = get_or_create_ids_list(
            number_of_id=6, desired_dir=self.test_dir)
        ids_list = divide_ids_list(ids_list, 40)
        create_files(day_dir=dir, ids_list=ids_list)
        files_directories = get_files_directories(files_directory=dir)
        s_data1 = {}
        with open(files_directories[0], "r") as file:
            lines = file.readlines()
            data = json.loads(lines[0])
            s_data1 = {
                "ids": [data["id"]],
                "attributes": data["attributes"]
            }
        output_dir = self.test_dir + "/output"
        self.assertEqual(len(glob.glob(output_dir + "/*.txt")), 0)
        search_data(s_data=s_data1, processes=1, desired_dir=self.test_dir)
        self.assertEqual(len(glob.glob(output_dir + "/*.txt")), 1)
