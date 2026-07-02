class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # n = len(arr)

        # ans =[0]*n
        # st = []

        # for i in range(n-1,-1,-1):
        #     while len(st)>0 and st[-1]<=arr[i]:
        #         st.pop()
        #     if len(st)==0
        #         ans[i]=-1
        #     else:
        #         ans[i]=st[-1]
            
        #     st.append(arr[i])
        # retur
        ans = []

        for num in nums1:

            # getting index of num in nums2
            index = nums2.index(num)

            found = -1

            
            for i in range(index + 1, len(nums2)):
                if nums2[i] > num:
                    found = nums2[i]
                    break

            ans.append(found)

        return ans