from copy import copy

from sort_algorithms.Helper import Helper


class SelectionSort:

    def sort(self, arr):
        helper = Helper()

        sorted_arr = copy(arr)

        for i in range(len(arr)):
            min_index = helper.find_min_number_in_array_starting_from_index(sorted_arr, i)
            sorted_arr = copy(helper.swap_two_numbers_in_array(sorted_arr, i, min_index))

        return sorted_arr
