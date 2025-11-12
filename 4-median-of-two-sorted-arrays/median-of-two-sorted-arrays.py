class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        import statistics
        
        n = len(nums1)
        m = len(nums2)
        i = 0
        j = 0
        merged = []
        
        while i < n and j < m:
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        
        while i < n:
            merged.append(nums1[i])
            i += 1
        
        while j < m:
            merged.append(nums2[j])
            j += 1
        
        return statistics.median(merged)