import unittest
import index as app 
import pandas as pd

class Test(unittest.TestCase):
    def test_day_name_of_week(self):
        self.assertEqual(app.day_name_of_week(pd.Timestamp('2022-12-12')), 'Monday')
        self.assertEqual(app.day_name_of_week(pd.Timestamp('2021-03-12')), 'Friday')

if __name__ == '__main__':
    unittest.main()