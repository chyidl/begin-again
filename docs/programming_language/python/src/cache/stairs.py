from timeit import repeat
from functools import lru_cache


# limiting the cache to a maximum of 16 entries
@lru_cache(maxsize=16)
def steps_to(stair):
    if stair == 1:
        # You can reach the first stair with only a single step
        # from the floor.
        return 1
    elif stair == 2:
        # You can reach the second stair by jumping from the
        # floor with a single two-stair hop or by jumping a single
        # stair a couple of times
        return 2
    elif stair == 3:
        # You can reach the third stair using four possible
        # combinations:
        # 1. Jumping all the way from the floor
        # 2. Jumping two stairs, them one
        # 3. Jumping one stair, then two
        # 4. Jumping one stair three times
        return 4
    else:
        # You can reach your current stair from three different places:
        # 1. From three stairs down
        # 2. From two stairs down
        # 3. From one stair down
        #
        # If you add up the number of ways of getting to those
        # those three positions, then you should have your solution.
        return steps_to(stair - 3) + steps_to(stair - 2) + steps_to(stair - 1)


setup_code = "from __main__ import steps_to"
stmt = "steps_to(30)"
"""
Time measurements are noisy because the system runs other processes concurrently.
The shortest time is always the least noisy, making it the best representation of the function's runtime
"""
times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)
print(f"Minimum execution time: {min(times)}")

print(steps_to.cache_info())
steps_to.cache_clear()
