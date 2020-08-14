def topKFrequent(nums, k):
    L = len(nums)
    if L == 0 or L == 1:
        return nums
    dc = dict()
    result = []
    for i in range(L):
        if nums[i] not in dc.keys():
            dc[nums[i]] = 1
        else:
            dc[nums[i]] += 1
    print(dc)
    sorted_dict = sorted(dc.items(),key=lambda x: x[1], reverse=True)
    print(sorted_dict)
    result = [key for key, value in sorted_dict[:k]]
    return result


if __name__ == '__main__':
    print(topKFrequent([1, 1, 1, 3, 2, 2], 2))
