#include <vector>
using namespace std;

class Solution {
private:
    vector<int> nums;          // 📦 Stores the input array
    vector<int> cache;         // 🧠 Memoization cache: -1 = unknown, 0 = false, 1 = true

    bool isPossible(int currentPosition = 0) {
        // 🚫 Out-of-bounds check
        // If we jump beyond the array, this path is invalid
        if (currentPosition >= nums.size()) 
            return false;

        // 🎯 Success condition
        // If we reach the last index, we can jump successfully
        if (currentPosition == nums.size() - 1) 
            return true;
        
        // 🧩 Solve only if this state hasn't been computed before
        if (cache[currentPosition] == -1) {
            // ❌ Assume it's not possible initially
            cache[currentPosition] = 0;

            // 👣 Try all possible jump lengths from current position
            for (int step = 1; step <= nums[currentPosition]; ++step) {
                // 🔄 Recursively check if any jump leads to success
                if (isPossible(currentPosition + step)) {
                    // ✅ Found a valid path
                    cache[currentPosition] = 1;
                    break;  // No need to explore further
                }
            }
        }

        // 📦 Return cached result
        return cache[currentPosition];
    }

public:
    bool canJump(vector<int>& nums) {
        // 📥 Store input array
        this->nums = nums;

        // 🧠 Initialize cache with -1 (unvisited state)
        this->cache = vector<int>(this->nums.size(), -1);

        // 🚀 Start recursion from index 0
        bool result = isPossible();

        // 🧹 Cleanup memory (good practice)
        vector<int>().swap(nums);
        vector<int>().swap(cache);

        // 🎉 Final result
        return result;
    }
};