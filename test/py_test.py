import unittest
from timeout_decorator import timeout
from source.python.solution import pySolution

class testPySolution(unittest.TestCase):
    def setUp(self):
        self.__testcases = (
            ([2,3,1,1,4], True),
            ([3,2,1,0,4], False)
        )
        self.__solution = pySolution()
        return super().setUp()
    
    @timeout(0.5)
    def testCase_0(self):
        nums, expectedOutput = self.__testcases[0]
        actualOutput = self.__solution.canJump(nums = nums)
        return self.assertEqual(actualOutput, expectedOutput)
    
    @timeout(0.5)
    def testCase_1(self):
        nums, expectedOutput = self.__testcases[1]
        actualOutput = self.__solution.canJump(nums = nums)
        return self.assertEqual(actualOutput, expectedOutput)
    
if __name__ == '__main__': unittest.main()