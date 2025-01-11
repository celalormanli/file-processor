import unittest
import tempfile
import os
from datagenerator.generator import *


class TestGeneratorMethods(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def test_create_directory(self):
        dir1 = create_directory()
        self.assertTrue(os.path.isdir(dir1))
        dir2 = create_directory(desired_dir=self.test_dir)
        self.assertTrue(os.path.isdir(dir2))
        dir3 = create_directory(desired_dir=self.test_dir,
                                day=datetime.datetime.today())
        self.assertTrue(os.path.isdir(dir3))

    def test_divide_ids_list(self):
        self.assertEqual(len(divide_ids_list([1, 2, 3, 4, 5, 6], 3)), 3)

    def test_random_value_generator(self):
        self.assertEqual(len(random_value_generator()), 6)
        self.assertEqual(len(random_value_generator(3)), 3)

    def test_get_or_create_ids_list(self):
        self.assertFalse(Path(self.test_dir + "/ids_list.txt").exists())
        ids_list = get_or_create_ids_list(
            number_of_id=6, desired_dir=self.test_dir)
        self.assertEqual(len(ids_list), 6)
        self.assertTrue(Path(self.test_dir + "/ids_list.txt").exists())

    def test_create_file(self):
        ids_list = get_or_create_ids_list(
            number_of_id=6, desired_dir=self.test_dir)
        dir = create_directory(desired_dir=self.test_dir)
        create_file(day_dir=dir, file_number=1, ids_list=ids_list)
        self.assertTrue(Path(dir + "/file" + str(1) + ".txt").exists())
        self.assertFalse(Path(dir + "/file" + str(2) + ".txt").exists())

    def test_create_files(self):
        dir = create_directory(desired_dir=self.test_dir)
        ids_list = get_or_create_ids_list(
            number_of_id=6, desired_dir=self.test_dir)
        ids_list = divide_ids_list(ids_list, 40)
        create_files(day_dir=dir, ids_list=ids_list)
        self.assertTrue(Path(dir + "/file" + str(1) + ".txt").exists())
        self.assertTrue(Path(dir + "/file" + str(40) + ".txt").exists())
        self.assertFalse(Path(dir + "/file" + str(41) + ".txt").exists())
