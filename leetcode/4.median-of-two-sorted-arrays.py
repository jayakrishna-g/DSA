#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start


### IS FAILING FOR DUPLICATE CASES NEED TO REVISIT
class Solution(object):
    def get_pos(self, arr, ele):
        st = 0
        en = len(arr) - 1
        if len(arr) == 0:
            return 0
        if ele >= arr[en]:
            return en + 1

        if ele < arr[st]:
            return 0

        while st <= en:
            mid = (st + en) // 2
            if arr[mid] > ele and arr[mid - 1] <= ele:
                return mid
            if arr[mid] > ele:
                en = mid - 1
            else:
                st = mid + 1
        return en + 1

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        st = 0
        en = len(nums1) - 1
        tot_len = len(nums1) + len(nums2)
        tar = [0, 0]
        if tot_len % 2 == 0:
            tar = [tot_len // 2 - 1, tot_len // 2]
        else:
            tar = [tot_len // 2]
        ans = []
        print(tar)
        while st <= en:
            print(f"st:{st} en:{en}")
            mid = (st + en) // 2
            pos = self.get_pos(nums2, nums1[mid])
            print(mid, pos)

            if pos + mid in tar:
                if len(ans) >= 1:
                    if nums1[mid] == ans[0]:
                        ans.append()
                ans.append(nums1[mid])

            if (pos + mid) <= tar[0]:
                st = mid + 1
            else:
                en = mid - 1
        print("check")

        st = 0
        en = len(nums2) - 1
        while st <= en:
            print(f"st:{st} en:{en}")
            mid = (st + en) // 2
            pos = self.get_pos(nums1, nums2[mid])
            print(mid, pos)

            if pos + mid in tar:
                ans.append(nums2[mid])

            if (pos + mid) <= tar[0]:
                st = mid + 1
            else:
                en = mid - 1
        print(ans)
        return ans[0] if len(ans) == 1 else (ans[0] + ans[1]) / 2


# @lc code=end
