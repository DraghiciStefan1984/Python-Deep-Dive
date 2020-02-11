# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 13:31:24 2020

@author: Stefan Draghici
"""

import unittest
from project import TimeZone, Account
from datetime import timedelta, datetime


def run_tests(test_class):
    suite=unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner=unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
    
    
class TestAccount(unittest.TestCase):
    def setUp(self):
        print('running setup...')
        
    def tearDown(self):
        print('running tear down...')
        
    def test_create_timezone(self):
        tz=TimeZone('abc', -1, -30)
        self.assertEqual('abc', tz.name)
        self.assertEqual(timedelta(hours=-1, minutes=-30), tz.offset)
        
    def test_timezones_equal(self):
        tz1=TimeZone('abc', -1, -30)
        tz2=TimeZone('abc', -1, -30)
        self.assertEqual(tz1, tz2)
        
    def test_timezones_not_equal(self):
        tz=TimeZone('abc', -1, -30)
        test_timezones=(TimeZone('def', -1, -30), TimeZone('abc', -1, 0), TimeZone('abc', 1, -30))
        for test_tz in test_timezones:
            self.assertNotEqual(tz, test_tz)


if __name__=='__main__':
    unittest.main()