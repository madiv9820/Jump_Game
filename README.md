## 🧠 Memoization Approach

In this approach, we solve the problem by breaking it into **smaller subproblems** and caching their results to avoid redundant work.

We recursively try all possible jumps from the current position. Once a position is solved, its result is stored in a cache, so the same state is never recomputed again.

### 🔄 How It Works
- 🎯 If we reach the last index → return `true`
- 🚫 If we go out of bounds → return `false`
- 🧩 If the result for a position is already cached → reuse it
- 👣 Otherwise, try all valid jump lengths and stop early if any path succeeds

### ⚡ Optimization
- 🧠 Memoization prevents exponential recomputation
- ✂️ Early pruning stops exploration as soon as a valid path is found

### ⏱️ Complexity
- **Time Complexity:** `O(N²)` (worst case, when all jumps are explored)
- **Space Complexity:** `O(N)` (cache + recursion stack)

### ⚖️ Trade-off
This approach is **easy to understand and debug**, but it is less efficient than the greedy solution, which achieves `O(N)` time by changing the problem perspective.

---