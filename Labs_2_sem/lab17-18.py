class StringArray:
    def __init__(self, size):
        self.size = size
        self.array = [(0, None)] * size

    def set_element(self, index, length, value):
        if index < 0 or index >= self.size:
            print("Index out of range")
            return
        if len(value) != length:
            print("Invalid string length")
            return
        self.array[index] = (length, value)

    def get_element(self, index):
        if index < 0 or index >= self.size:
            print("Index out of range")
            return None
        return self.array[index][1]

    def concatenate(self, other_array):
        if self.size != other_array.size:
            print("Arrays have different sizes")
            return
        concatenated_array = StringArray(self.size)
        for i in range(self.size):
            length1, value1 = self.array[i]
            length2, value2 = other_array.array[i]
            concatenated_array.set_element(i, length1 + length2, value1 + value2)
        return concatenated_array

    def merge(self, other_array):
        if self.size != other_array.size:
            print("Arrays have different sizes")
            return
        merged_array = StringArray(self.size)
        for i in range(self.size):
            length1, value1 = self.array[i]
            length2, value2 = other_array.array[i]
            merged_value = ""
            for j in range(length1):
                if value1[j] not in merged_value:
                    merged_value += value1[j]
            for j in range(length2):
                if value2[j] not in merged_value:
                    merged_value += value2[j]
            merged_array.set_element(i, len(merged_value), merged_value)
        return merged_array

    def print_element(self, index):
        element = self.get_element(index)
        if element is not None:
            print(element)

    def print_all(self):
        for i in range(self.size):
            self.print_element(i)