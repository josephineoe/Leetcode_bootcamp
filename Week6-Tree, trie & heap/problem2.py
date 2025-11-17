class Solution:
    def topKFrequent(self, nums, k):
        freq = Counter(nums)  # frequency map
        
        # bucket where index = frequency, value = list of numbers
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for num, count in freq.items():
            buckets[count].append(num)
        
        result = []
        # iterate freq from high to low
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result