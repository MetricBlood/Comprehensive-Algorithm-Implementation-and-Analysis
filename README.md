# Comprehensive Algorithm Implementation and Analysis

Implementations of classic algorithms in Python, each benchmarked on generated datasets, with the running times plotted so the theoretical complexity can be compared against what actually happens.

The point of the project was not to implement the algorithms — it was to measure them and see where the textbook complexity does and does not hold.

## Contents

**1. Generating Data Sets**
Scripts that produce input sets of controlled size and shape, so every algorithm below is measured on the same data rather than on whatever was convenient.

**2. Heap and Selection Sorting**
Heap Sort and Selection Sort implemented from scratch and timed across increasing input sizes, showing the gap between O(n log n) and O(n²) opening up as n grows.

**3. Dijkstra and Kruskal**
Dijkstra's shortest path and Kruskal's minimum spanning tree, run over generated graphs of varying density to see how each responds to edge count rather than just vertex count.

**4. Knapsack**
A dynamic programming solution to the knapsack problem, measured against problem size and capacity.

## What came out of it

Performance visualisations covering time and space trade-offs for each algorithm, which is the part that made the difference between having implemented something and having understood it.

## Built with

Python
