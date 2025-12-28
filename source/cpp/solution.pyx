# ============================================================
# 🔗 Cython Binding Layer: Python ↔ C++ Solution
# ============================================================
#
# 🧩 Purpose:
# Acts as a thin interoperability layer between Python and C++
# by exposing the C++ `Solution` class to Python code.
#
# ⚙️ What it does:
# - Wraps the C++ `Solution` class using Cython
# - Converts Python lists into `std::vector<int>`
# - Forwards calls to the underlying C++ implementation
# - Converts C++ boolean results into Python-friendly types
#
# 🚧 Design Notes:
# - Keeps this layer intentionally minimal (no business logic)
# - All algorithmic logic lives in C++
# - Python code interacts only with this safe wrapper
#
# 🎯 Goal:
# Enable seamless testing and comparison of Python and C++
# implementations under a unified Python test framework.
# ============================================================

from libcpp.vector cimport vector

cdef extern from "solution.hpp":
    cdef cppclass Solution:
        Solution() except + 
        bint canJump(vector[int]& nums)

cdef class cppSolution:
"""
    🔌 Python-facing wrapper for the C++ Solution class

    Responsibilities:
    - Manage lifetime of the underlying C++ object
    - Translate Python data structures to C++ equivalents
    - Expose a clean, Pythonic API for testing and usage

    ⚠️ No algorithmic logic should be added here
"""
    cdef Solution *thisPtr
    def __cinit__(self): self.thisPtr = new Solution()
    def __dealloc__(self): del self.thisPtr

    def canJump(self, nums):
        cdef vector[int] cppArr
        cdef int num
        cdef bint result

        for num in nums: cppArr.push_back(num)
        result = self.thisPtr.canJump(cppArr)
        return bool(result)