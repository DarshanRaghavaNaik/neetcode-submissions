class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        if k == len(nums):
            return nums
        for num in nums:
            seen[num] = seen.get(num,0) + 1
        buckets = [[] for _ in range(len(nums) + 1)]

        
        for key, value in seen.items():
            buckets[value].append(key)
        
        result = []
        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result

