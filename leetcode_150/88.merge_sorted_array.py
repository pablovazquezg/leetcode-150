from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l1 = len(nums1)
        l2 = len(nums2)
        nums1[l1:].extend(nums2)
        print(nums1)
        nums1.sort()
