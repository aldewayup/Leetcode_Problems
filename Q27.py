#Q27
#remove element in place
def removeelement(nums, val):
    m = len(nums) - 1
    while m >= 0:
        if nums[m] == val:
            del nums[m]
            m -=1
            continue
        m -=1
    
    print(nums)

if __name__ == "__main__":
    nums = [3,3]
    val = 3
    removeelement(nums, val)

    nums = [3,2,2,3]
    val = 3
    removeelement(nums, val)