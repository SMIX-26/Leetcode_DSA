class Solution:
    def rotate(self, arr: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(arr)

        k = k % n

        def reverse(left:int, right:int) -> None:
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        reverse( 0, n - 1)
        reverse( 0, k - 1)
        reverse( k, n - 1)
        

        