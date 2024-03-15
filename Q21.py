#Q21
#Merge two sorted arrays

def merge(nums1,nums2,m,n):
    i = m - 1
    j = n - 1
    k = m + n - 1

    while j>=0:
        if i>=0 and nums1[i] >= nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

if __name__ == "__main__":
    arr = [1,2,3,0,0,0]
    brr = [1,2,3]
    m = 3
    n = 3
    merge(arr,brr,m,n)
    print(arr)