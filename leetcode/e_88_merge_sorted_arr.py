def merge(nums1, m, nums2, n):
    n1 = m-1
    n2 = n-1
    for i in range(len(nums1)-1, -1, -1):
        if n2 <0 :
            break
            
        if n1 >= 0 and nums1[n1] > nums2[n2]:
            nums1[i]=nums1[n1]
            n1-=1
        else:
            nums1[i]=nums2[n2]
            n2-=1
