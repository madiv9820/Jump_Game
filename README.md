## 🧩 Dynamic Programming (Bottom-Up) Approach

In this approach, we use **bottom-up dynamic programming** to determine whether we can reach the last index of the array.

Instead of recursion, we **fill the table from right to left**, solving smaller subproblems first and building up to the full solution.

### 🔄 How It Works
- 🎯 Base Case: The last index can always reach itself → True.
- 🔁 Traverse from right to left: For each position, check all valid jumps.
- 👣 Check possible jumps: If any jump from the current position leads to a True position, mark the current index as True.
- ✂️ Early pruning: Once a True path is found, stop checking further jumps from the same index.

### ⚡ Optimization
- 🧠 Unlike recursion, **no call stack is used**, so memory usage is just the DP array.
- ✅ Avoids repeated computation of subproblems, similar to memoization.

### ⏱️ Complexity
- **Time Complexity:** `O(N²)` (nested loops for each position and jump)
- **Space Complexity:** `O(N)` (DP array)

### ⚖️ Trade-offs
- 👍 Easy to understand and iterative (no recursion)
- 👎 Less efficient than **Greedy** solution, which achieves `O(N)` time by tracking the farthest reachable index

---