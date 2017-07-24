# coding=utf-8

import unittest
import demo07


class TestName(unittest.TestCase):
    def test_get_name(self):
        name = demo07.get_name()
        print name
        self.assertEqual(name, "lc")


unittest.main
