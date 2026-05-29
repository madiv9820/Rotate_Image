"""
================================================================================
📄 File: solution.py
================================================================================
Description: 
    The main entry point and runner for the LeetCode 48: Rotate Image problem.
    This file handles the specific interface expected by the caller/tester 
    and delegates the heavy algorithmic lifting to the Approaches class.

Usage:
    Instantiate the Solution class and call the `rotate(matrix)` method.
    You can easily test different time/space complexities by swapping out 
    which underlying approach is executed inside the method! 🧪
================================================================================
"""

from typing import List
from .approaches import Approaches

class Solution(Approaches):
    # 🧩 By inheriting from Approaches, this class automatically gains access 
    # to all the rotation algorithms we built in `approaches.py`!
    
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotates a given n x n 2D matrix by 90 degrees clockwise in-place.
        Do not return anything, modify the input matrix in-place instead.
        """
        
        # 📦 Bind the input matrix to our instance state so the hidden 
        # approach methods can seamlessly access and mutate it.
        self._matrix = matrix
        
        # 🚀 EXECUTION BLOCK
        # Choose your fighter! Comment/uncomment to swap the active algorithm.
        
        # self._approach_01_simulation()             # 🧅 The Layer-by-Layer method
        self._approach_02_tranpose_and_reverse()     # ✨ The Linear Algebra method