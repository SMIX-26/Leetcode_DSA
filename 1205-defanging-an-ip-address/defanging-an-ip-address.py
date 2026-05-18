class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".","[.]")

        #using without inbuilt functions
        # ans = ""
        # for i in address:
        #     if i!=".":
        #         ans+=i
        #     else:
        #         ans+="[.]"
        # return ans