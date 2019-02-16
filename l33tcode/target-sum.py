import unittest

class Solution:
    def findTargetSumWays(self, nums: 'List[int]', S: 'int') -> 'int':
        if not len(nums):
            return 0

        stack = [(0, -1)]
        number_of_ways = 0

        while len(stack):
            prev_sum, pos = stack.pop()

            sum_minus = prev_sum - nums[pos + 1]
            if pos == len(nums) - 2:
                if sum_minus == S:
                    number_of_ways += 1
            else:
                stack.append((sum_minus, pos + 1))

            sum_plus = prev_sum + nums[pos + 1]
            if pos == len(nums) - 2:
                if sum_plus == S:
                    number_of_ways += 1
            else:
                stack.append((sum_plus, pos + 1))

        return number_of_ways


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty(self):
        self.assertEqual(self.sol.findTargetSumWays([], 0), 0)
        self.assertEqual(self.sol.findTargetSumWays([], 5), 0)

    def test_one_element(self):
        self.assertEqual(self.sol.findTargetSumWays([1], 0), 0)
        self.assertEqual(self.sol.findTargetSumWays([1], -1), 1)
        self.assertEqual(self.sol.findTargetSumWays([1], 1), 1)

    def test_complex1(self):
        self.assertEqual(self.sol.findTargetSumWays([1, 1, 1, 1, 1], 3), 5)

    def test_complex2(self):
        self.assertEqual(self.sol.findTargetSumWays([50,37,6,20,35,41,45,3,20,36,49,1,20,10,43,4,44,15,44,34], 25), 5564)

    def test_complex3(self):
        self.assertEqual(self.sol.findTargetSumWays([14,23,35,48,10,39,34,40,36,45,11,14,41,6,4,17,42,22,0,35], 44), 5844)

    def test_complex4(self):
        for _ in range(20):
            self.assertEqual(self.sol.findTargetSumWays([1] * 20, 10), 15504)


if __name__ == "__main__":
    unittest.main()
