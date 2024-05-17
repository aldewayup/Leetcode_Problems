#Q26
#Remove duplicates in place

def removeDuplicates(self, nums: list[int]) -> int:
    j = 0
    for i in range(1,len(nums)):
        if nums[j] != nums[i]:
            j+=1
            nums[j] = nums[i]
    return j+1

if __name__ == "__main__":
    nums = [3,3,3,4,5,6,6,6,6]
    val = 3
    removeDuplicates(nums)