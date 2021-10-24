from sort_algorithms.SelectionSort import SelectionSort
import unittest


class SelectionSortTest(unittest.TestCase):
    def test_sortArray(self):
        test_array1 = [2, 1]
        test_array2 = [-2, 10, 100, -5, 9, 0, 77]

        sut = SelectionSort()

        sorted_arr1 = sut.sort(test_array1)
        sorted_arr2 = sut.sort(test_array2)

        self.assertEqual(sorted_arr1, [1, 2])
        self.assertEqual(sorted_arr2, [-5, -2, 0, 9, 10, 77, 100])


if __name__ == '__main__':
    unittest.main()
