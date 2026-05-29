"""
================================================================================
📄 File: approaches.py
================================================================================
Description: 
    Solutions for rotating an n x n 2D matrix 90 degrees clockwise in-place.
    Often recognized as standard technical interview question (LeetCode 48).

Problem Statement:
    Given an n x n 2D matrix representing an image, rotate the image by 
    90 degrees (clockwise). You must rotate the image in-place, which means 
    you have to modify the input 2D matrix directly. DO NOT allocate another 
    2D matrix to do the rotation.

Approaches Included:
    1. _approach_01_simulation            -> Layer-by-Layer ("Onion" Method) 🧅
    2. _approach_02_transpose_and_reverse -> Linear Algebra (Transpose + Flip) ✨

================================================================================
"""

class Approaches:
    def _approach_01_simulation(self) -> None:
        # 🎯 APPROACH 1: Layer-by-Layer Simulation (The "Onion" Method 🧅)
        # We physically rotate the matrix ring by ring, starting from the outside and moving in! 🔄
        
        # 📍 Setup our initial boundary pointers (Left, Right, Top, Bottom)
        left_ptr:   int = 0
        right_ptr:  int = len(self._matrix) - 1
        top_ptr:    int = 0
        bottom_ptr: int = len(self._matrix) - 1

        # 🎡 Keep spinning as long as we have layers left to process!
        while left_ptr < right_ptr and top_ptr < bottom_ptr:
            # 🚶‍♂️ Walk through the current layer (offset by `i`)
            for i in range(right_ptr - left_ptr):
                
                # 💾 Save the top-left-ish element before we overwrite it
                temp: int                                   = self._matrix[top_ptr][left_ptr + i]
                
                # ⬆️ Move Bottom-Left to Top-Left
                self._matrix[top_ptr][left_ptr + i]         = self._matrix[bottom_ptr - i][left_ptr]
                
                # ⬅️ Move Bottom-Right to Bottom-Left
                self._matrix[bottom_ptr - i][left_ptr]      = self._matrix[bottom_ptr][right_ptr - i]
                
                # ⬇️ Move Top-Right to Bottom-Right
                self._matrix[bottom_ptr][right_ptr - i]     = self._matrix[top_ptr + i][right_ptr]
                
                # ➡️ Move saved Top-Left to Top-Right
                self._matrix[top_ptr + i][right_ptr]        = temp
            
            # 🧅 Layer complete! Shrink the boundaries to peel to the next inner ring
            left_ptr    += 1
            right_ptr   -= 1
            top_ptr     += 1
            bottom_ptr  -= 1

    def _approach_02_tranpose_and_reverse(self) -> None:
        # 📐 APPROACH 2: Linear Algebra Magic (Transpose + Reflect ✨)
        # Rotating 90° clockwise is mathematically identical to a transpose followed by a horizontal flip! 🪞
        
        n: int = len(self._matrix)
        
        # 🔄 STEP 1: Transpose the matrix (swap rows with columns)
        # We start `j` at `i` to only process the upper triangle and avoid undoing our swaps!
        for i in range(n):
            for j in range(i, n):
                # 🔀 Swap elements across the main diagonal (top-left to bottom-right)
                self._matrix[i][j], self._matrix[j][i] = \
                    self._matrix[j][i], self._matrix[i][j]

        # ↔️ STEP 2: Reverse every row (Horizontal Reflection)
        # We set up two column pointers to flip the matrix left-to-right
        left_ptr:   int = 0
        right_ptr:  int = n - 1

        # 🪞 Keep flipping columns until the pointers meet in the middle
        while left_ptr < right_ptr:
            for i in range(n):
                # 🔀 Swap the left-side element with the right-side element for the current row `i`
                self._matrix[i][left_ptr], self._matrix[i][right_ptr] = \
                    self._matrix[i][right_ptr], self._matrix[i][left_ptr]

            # 🚶‍♂️ Move pointers inward for the next set of columns
            left_ptr    += 1
            right_ptr   -= 1