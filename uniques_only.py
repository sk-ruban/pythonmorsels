# Original Solution - Too slow as not in list requires looping through whole list!
def uniques_only(iterable):
    checklist = []
    for item in iterable:
        if item not in checklist:
            checklist.append(item)
            # Bonus 1
            yield item
"""
# Cannot use set(iterable) as it is unordered
# However, Sets rely on hashes for lookups -> Much faster

def uniques_only(iterable):
    seen = set()
    for item in iterable:
        if item not in seen:
            yield item
            seen.add(item)
"""
uniques_only([1, 2, 2, 1, 1, 3, 2, 1])
nums = [1, -3, 2, 3, -1]
squares = (n**2 for n in nums)
uniques_only(squares)
nums = iter([1, 2, 3])
output = uniques_only(nums)
