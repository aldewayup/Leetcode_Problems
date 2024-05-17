#Q80
#remove duplicates leaving atmost2
def removeDuplicates(self, nums: list[int]) -> int:
        k=2
        for i in range(2,len(nums)):
            if nums[i] != nums[k-1]:
                print(k,nums[k])
                nums[k] = nums[i]
                k+=1
            elif nums[i] != nums[k-2]:
                print(k,nums[k])
                nums[k] = nums[i]
                k+=1
        
        return k

if __name__ == "__main__":
    nums = [3,3,3,4,5,6,6,6,6]
    val = 3
    removeDuplicates(nums)

    