#!/usr/bin/env python

"""Tests for `starter` package."""
# pylint: disable=redefined-outer-name

import unittest
import logging
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

logger = logging.getLogger('TestStarter')


class TestStarter(unittest.TestCase):
    test_data_path: str = os.path.join('test_data', 'test_starter')

    def test_sample(self):
        with open(os.path.join(self.test_data_path, 'my_data.txt'), 'r') as my_data_f:
            my_data = my_data_f.read()

        expected_data = 'sample'
        self.assertEqual(my_data, expected_data)

    @staticmethod
    def _setup_log() -> None:
        # noinspection PyArgumentList
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S',
                            handlers=[logging.StreamHandler()
                                      ]
                            )

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @classmethod
    def setUpClass(cls):
        cls._setup_log()

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()
