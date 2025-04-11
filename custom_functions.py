class CustomMethodes:

    def __init__(self):
        self.left = []
        self.right = []
        self.pivot = None
        self.aray = [10, 5, 2, 3, 1, 4, 6, 7, 8, 9]
        self.aray = self.sorter(self.aray)  # Store the sorted result


    def sorter(self, arr):
        if len(arr) <= 1:  # Base case to stop recursion
            return arr
        self.pivot = arr[len(arr) // 2]  # Corrected length calculation
        self.left = [x for x in arr if x < self.pivot]  # Fixed undefined variable
        self.right = [x for x in arr if x > self.pivot]
        return self.sorter(self.left) + [self.pivot] + self.sorter(self.right)  # Fixed infinite recursion