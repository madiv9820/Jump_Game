#include <vector>
using namespace std;

class Solution {
public:
    bool canJump(vector<int>& nums) {
        // 📏 Length of the array
        int n = nums.size();

        // 🧠 DP table
        // isPossible[i] = true if we can reach the last index starting from i
        vector<bool> isPossible(n, false);

        // 🎯 Base case
        // From the last index, we are already at the destination
        isPossible[n - 1] = true;

        // 🔁 Traverse from right to left (bottom-up DP)
        // We decide if each position can reach the end
        for (int currentPosition = n - 2; currentPosition >= 0; --currentPosition) {

            // 👣 Try all possible jumps from the current position
            for (int step = 1; step <= nums[currentPosition]; ++step) {

                // 📦 Result of jumping to the next position
                // If jump goes out of bounds, treat it as invalid (false)
                bool nextResult = (
                    (currentPosition + step) < n
                        ? isPossible[currentPosition + step]
                        : false
                );

                // 🔗 Update current position
                // If ANY jump can reach the end, mark this index as reachable
                isPossible[currentPosition] =
                    isPossible[currentPosition] | nextResult;
                
                // ✂️ Early pruning: stop checking further jumps 
                // if we already can reach the end
                if(isPossible[currentPosition])
                    break;
            }
        }

        // 🚀 Final answer
        // Can we reach the last index starting from index 0?
        bool result = isPossible[0];

        // 🧹 Cleanup memory (optional good practice)
        vector<bool>().swap(isPossible);

        // 🎉 Return result
        return result;
    }
};