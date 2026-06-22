🔍 Searching and Sorting Algorithms in Python
📖 Overview

This repository contains implementations of fundamental Searching and Sorting Algorithms in Python along with:

Explanation
Pseudocode
Example
Time Complexity
Space Complexity
Interview Questions
1. Linear Search
Explanation

Linear Search checks each element one by one until the target element is found.

Example

Array:

[10, 20, 30, 40]

Target:

30

Process:

10 ❌
20 ❌
30 ✅

Output:

Index = 2
Pseudocode
LinearSearch(arr, target)

FOR each element in arr
    IF element == target
        RETURN index

RETURN -1
Time Complexity
Case	Complexity
Best	O(1)
Average	O(n)
Worst	O(n)
Why?
Best Case: Element found at first position.
Worst Case: Element found at last position or not found.
Space Complexity
O(1)
Interview Questions
What is Linear Search?
Can Linear Search work on unsorted arrays?
What is the difference between Linear Search and Binary Search?
