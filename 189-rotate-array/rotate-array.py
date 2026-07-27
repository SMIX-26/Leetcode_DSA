class Solution:
    def reverse(self, arr, left, right):
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
    def rotate(self, arr: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(arr)

        k = k % n
        self.reverse(arr, 0, n - 1)
        self.reverse(arr, 0, k - 1)
        self.reverse(arr, k, n - 1)
        

        