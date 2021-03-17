class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        token = 0
        length = len(nums)
        while token < length:
            if nums[token] == val:
                nums.pop(token)
                #print(mylist)
                #token += 1
                length -= 1
            else:
                token +=1