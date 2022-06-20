from kata import *
import unittest


class Test_Pete_the_Baker(unittest.TestCase):
    def test0(self):    
        self.assertEqual(0, 1)


if __name__ == '__main__':
    unittest.main()


'''
import codewars_test as test
from solution import cakes

@test.it('Testing Pete, the Baker')
def _():
    recipe = {"flour": 500, "sugar": 200, "eggs": 1}
    available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
    test.assert_equals(cakes(recipe, available), 2, 'example #1')

    recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
    available = {"sugar": 500, "flour": 2000, "milk": 2000}
    test.assert_equals(cakes(recipe, available), 0, 'example #2')

'''