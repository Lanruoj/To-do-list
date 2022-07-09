# python3 -m unittest test_lists.py


# pseudo: 

import unittest
from app import add_task

class TestCases(unittest.TestCases):

    def test_option_executes_function(self):
        self.assertEqual(app.choose_option)


        
    
    # def test_mark_as_done(self):

    
    # def test_sort(self):

if __name__ == '__main__':
    unittest.main()
