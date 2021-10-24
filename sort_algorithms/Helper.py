class Helper:

    def find_min_number_in_array_starting_from_index(self, array, index):
        min_number = array[index]
        min_index = index

        for x in range(index, len(array)):
            if min_number > array[x]:
                min_number = array[x]
                min_index = x

        return min_index

    def swap_two_numbers_in_array(self, array, index1, index2):
        temp = array[index1]
        array[index1] = array[index2]
        array[index2] = temp
        return array
