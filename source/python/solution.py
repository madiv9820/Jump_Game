from typing import List

class pySolution:
    def canJump(self, nums: List[int]) -> bool:
        # 🏁 Initialize the farthest position we can reach
        farthest: int = 0
        
        # 🎯 Last index we need to reach
        lastIndex: int = len(nums) - 1

        # 🔄 Iterate through each index in the array
        for index in range(len(nums)):
            # 🚀 Update the farthest reachable position from current index
            farthest = max(farthest, index + nums[index])

            # ✅ If we can reach or pass the last index, return True
            if farthest >= lastIndex:  return True
            
            # 🛑 If we can't move forward from current position, break early
            if farthest <= index: break
        
        # ❌ If loop ends without reaching last index, return False
        return False