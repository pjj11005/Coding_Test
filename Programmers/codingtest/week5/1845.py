def solution(nums):
    n = len(nums)
    phone = set()
    for num in nums:
        phone.add(num)
    return min(len(phone), (n // 2))
