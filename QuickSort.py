from Sort import Sort


class QuickSort(Sort):
    def partition(self, start, end, steps, reverse):
        self.array: list
        arr = self.array
        pivot_index = start
        pivot = arr[end - 1]

        for i in range(start, end):
            if reverse:
                if arr[i] > pivot:
                    arr[i], arr[pivot_index] = arr[pivot_index], arr[i]
                    pivot_index += 1
            else:
                if arr[i] < pivot:
                    arr[i], arr[pivot_index] = arr[pivot_index], arr[i]
                    pivot_index += 1
            steps.append((self.array.copy(),
                          {
                              start: (127, 255, 90),
                              end: (127, 255, 60),
                              pivot_index + 1: (127, 0, 0)
                          }))

        arr[pivot_index], arr[end - 1] = arr[end - 1], arr[pivot_index]
        steps.append((self.array.copy(), {
            start: (127, 90, 90),
            end: (127, 60, 60),
            pivot_index + 1: (127, 0, 0)
        }))
        return pivot_index

    def quick_sort(self, start, end, steps, reverse):
        if (start >= end): return
        index = self.partition(start, end, steps, reverse)
        self.quick_sort(start, index, steps, reverse)
        self.quick_sort(index + 1, end, steps, reverse)

    def sort(self, reverse=False) -> list:
        steps = []
        self.quick_sort(0, len(self.array), steps, reverse)
        return steps

