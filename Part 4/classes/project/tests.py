import unittest
from classes import TimeZone, Account
from datetime import timedelta, datetime


def run_tests(test_class):
    suite=unittest.TestRunner().loadTestsFrimTestCase(test_class)
    runner=unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
    
    
class TestAccount(unittest.TestCase):
    def test_create_timezone(self):
        tz=TimeZone('ABC', -1, -30)
        self.assertEqual('ABC', tz.name)
        self.assertEqual(timedelta(hours=-1, minutes=-30), tz.offset)
        
    def test_timezones_equal(self):
        tz1=TimeZone('ABC', -1, 30)
        tz2=TimeZone('ABC', -1, 30)
        self.assertEqual(tz1, tz2)
        
    def test_timezones_not_equal(self):
        tz=TimeZone('ABC', -1, 30)
        test_timezones=(
            TimeZone('DEF', -1, 0),
            TimeZone('GHI', 1, 30),
            TimeZone('JKL', 1, 0)
        )
        for test_tz in test_timezones:
            self.assertNotEqual(tz, test_tz)
            
            
run_tests(TestAccount)