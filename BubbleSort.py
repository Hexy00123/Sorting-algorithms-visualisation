from Sort import Sort


class BubbleSort(Sort):
    def sort(self, reverse = False) -> list:
        steps = []
        arr = self.array
        for i in range(len(arr)-1):
            for j in range(len(arr)-i-1):
                if reverse is False:
                    if arr[j] > arr[j+1]:
                        arr[j], arr[j+1] = arr[j+1], arr[j]
                else:
                    if arr[i] < arr[j]:
                        arr[j], arr[j+1] = arr[j+1], arr[j]

                steps.append((arr.copy(), {j+1:(127,0,0)}))

        return steps

