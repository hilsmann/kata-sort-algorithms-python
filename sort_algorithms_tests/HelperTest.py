from sort_algorithms.Helper import Helper
import unittest


class HelperTest(unittest.TestCase):
    def test_find_min_number_in_array(self):
        test_array1 = [2, 1]
        test_array2 = [5, 6, 11, 9]
        test_array3 = [5, -6, -101, 9]

        helper = Helper()

        min_number1 = helper.find_min_number_in_array_starting_from_index(test_array1, 0)
        min_number2 = helper.find_min_number_in_array_starting_from_index(test_array2, 0)
        min_number3 = helper.find_min_number_in_array_starting_from_index(test_array3, 1)

        self.assertEqual(min_number1, 1)
        self.assertEqual(min_number2, 0)
        self.assertEqual(min_number3, 2)

    def test_swap_two_numbers_in_array(self):
        test_array1 = [2, 1]
        test_array2 = [-3, 7, 101, -9]

        helper = Helper()

        swapped_array1 = helper.swap_two_numbers_in_array(test_array1, 0, 1)
        swapped_array2 = helper.swap_two_numbers_in_array(test_array2, 2, 3)

        self.assertEqual(swapped_array1, [1, 2])
        self.assertEqual(swapped_array2, [-3, 7, -9, 101])


if __name__ == '__main__':
    unittest.main()
