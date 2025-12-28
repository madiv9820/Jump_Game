# [🕹️ Jump Game](https://leetcode.com/problems/jump-game/?envType=study-plan-v2&envId=top-interview-150)

You are given an integer array `nums` 🔢 where **each element tells you the maximum jump** length you can take from that position.

🚦 You start at the **first index (0)** and your mission is simple but tricky:

👉 **Can you reach the last index of the array or not?**

### 🧠 How the Game Works
- From index i, you can jump **forward only** 🏃‍♂️
- You may jump to **any index between**:
    ```
    i + 1  ➡️  i + nums[i]
    ```
- Landing on a `0` ⛔ means **no further moves** from that position

### 🎯 Goal
Return:
- `true` — if you can reach the final index
- `false` — if you get stuck before reaching the end

### 🔍 Examples
- [2,3,1,1,4] 🟢 → Multiple valid jumps allow you to reach the end
- [3,2,1,0,4] 🔴 → You’re forced to stop at index 3

### ⚠️ Constraints
- 📏 `1 ≤ nums.length ≤ 10⁴`
- 🔢 `0 ≤ nums[i] ≤ 10⁵`

💡 Think of it like a platform game — every number gives you jump power, but one wrong landing and the game’s over 🎮🔥

## 💡 Approaches

- ### [🔁 Brute Force](https://github.com/madiv9820/Jump_Game/blob/Approach_01-Brute_Force_Recursion)
    Explores **all possible jump paths** using recursion.

    - ✅ Returns `true` if **any path** reaches the last index  
    - ❌ Returns `false` if **all paths fail**

    ⚠️ Inefficient for large inputs due to repeated recursive calls.

- ### [🧩 Memoization](https://github.com/madiv9820/Jump_Game/blob/Approach_02-Memoization)
    Enhances brute force by **caching results** for each index.

    - 🧠 Avoids recalculating previously solved states  
    - ✅ Faster than pure recursion  
    - ❌ Still slower than optimal solutions

- ### [📐 Dynamic Programming](https://github.com/madiv9820/Jump_Game/blob/Approach_03-Dynamic_Programming)
    Uses **bottom-up DP** to build reachability from the end.

    - 🎯 Last index is reachable by definition  
    - 🔁 Each index checks all valid forward jumps  
    - ❌ Higher time complexity due to nested loops

- ### [⚡ Greedy](https://github.com/madiv9820/Jump_Game/blob/Approach_04-Greedy)
    Tracks the **farthest reachable index** in a single pass.
    - 🚀 Always extends maximum reach  
    - ✅ Returns `true` once the last index is reachable  
    - ❌ Stops early if forward movement becomes impossible

    🔥 **Most efficient approach** — optimal for interviews.
---