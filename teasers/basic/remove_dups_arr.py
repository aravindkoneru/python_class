import pytest

# faster
def remove_duplicates(nums):
    if len(nums) == 0 or len(nums) == 1:
        return len(nums)

    arr_len = 0

    for x in range(len(nums) - 1):
        elem = nums[x]
        if nums[x] != nums[x + 1]:
            nums[arr_len] = nums[x]
            arr_len += 1

    nums[arr_len] = nums[-1]
    arr_len += 1

    return arr_len


# fastest
# def remove_duplicates(nums):
#    nums[:] = sorted(set(nums))
#    return len(nums)


# testing suite
@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1], [1]),
        ([1, 1], [1]),
        ([1, 2, 2], [1, 2]),
        ([1, 2, 2, 3], [1, 2, 3]),
        ([1, 2, 3, 3], [1, 2, 3]),
        ([1, 2, 2, 3, 3], [1, 2, 3]),
        ([1, 1, 2, 2, 3, 3, 4], [1, 2, 3, 4]),
    ],
)
def test_remove_dupes(nums, expected):
    num_unique = remove_duplicates(nums)

    assert num_unique == len(expected)
    assert nums[:num_unique] == expected
