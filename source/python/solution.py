from typing import List

class pySolution:
    def canJump(self, nums: List[int]) -> bool:
        # 🧠 Memoization cache
        # cache[i] tells whether it's possible to reach the end starting from index i
        cache: List[bool] = [None] * len(nums)

        def isPossible(currentPosition: int = 0) -> bool:
            # 🚫 Out of bounds check
            # If we jump beyond the array, this path is invalid
            if currentPosition >= len(nums):
                return False

            # 🎯 Success condition
            # If we reach the last index, we can successfully jump to the end
            if currentPosition == len(nums) - 1:
                return True
            
            # 🧩 Compute only if not already solved
            if cache[currentPosition] is None:
                # ❌ Assume false initially (optimistic → pessimistic update)
                cache[currentPosition] = False

                # 👣 Try all possible jump lengths from current position
                for step in range(1, nums[currentPosition] + 1):
                    # 🔄 Recursively check if any jump leads to success
                    if isPossible(currentPosition + step):
                        # ✅ Found a valid path
                        cache[currentPosition] = True
                        break  # No need to try further jumps

            # 📦 Return cached result (True / False)
            return cache[currentPosition] 
        
        # 🚀 Start recursion from index 0
        result: bool = isPossible()

        # 🧹 Cleanup (optional, helps readability)
        del cache

        # 🎉 Final answer: can we reach the last index or not?
        return result