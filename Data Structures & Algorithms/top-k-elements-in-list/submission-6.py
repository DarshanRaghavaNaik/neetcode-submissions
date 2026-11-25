from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies
        count = Counter(nums)
        
        # Step 2: Extract the top k keys
        # count.most_common(k) returns a list of tuples like [(num, frequency), ...]
        return [item[0] for item in count.most_common(k)]