import os
import sys
import unittest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import shutil
from utils import (
    create_folder,
    set_name,
    is_valid_url,
)

class TestUtils(unittest.TestCase):
    def test_create_folder(self):
        tmp_dir = create_folder("create_folder_test")
        self.assertEqual(os.path.isdir(tmp_dir), True)

        shutil.rmtree(tmp_dir)
        self.assertEqual(os.path.isdir(tmp_dir), False)

    def test_set_name(self):
        name = set_name("abc", "", "", 1, 1)
        self.assertEqual(name, "abc1")

        name = set_name("abc", ".txt", "", 1, 1)
        self.assertEqual(name, "abc1.txt")

        name = set_name("abc", ".txt", "_", 1, 1)
        self.assertEqual(name, "abc_1.txt")

        name = set_name("abc", ".txt", "_", 38, 1)
        self.assertEqual(name, "abc_38.txt")

        name = set_name("abc", ".txt", "_", 38, 6)
        self.assertEqual(name, "abc_000038.txt")

    def test_is_valid_url(self):
        self.assertEqual(is_valid_url('https://google.com'), True)
        self.assertEqual(is_valid_url(\
            'https://www.google.com/search?q=the+simpsons'), True)
        
        self.assertEqual(is_valid_url('https://google.co'), False)
        self.assertEqual(is_valid_url('//google.com'), False)
        self.assertEqual(is_valid_url('google.com'), False)
        self.assertEqual(is_valid_url('google'), False)
        self.assertEqual(is_valid_url(''), False)

if __name__ == "__main__":
    unittest.main()