# Comprehensive Algorithm Implementation and Analysis

Classic algorithms implemented in Python, each run against generated datasets and measured, so the theoretical complexity can be compared against what actually happens on real input.

The point of the project was not to implement the algorithms — it was to generate the data, measure the runs and see where the textbook behaviour does and does not hold.

## Contents

**1. Generating Data Sets** — `Dataset1.py`, `Dataset2.py`
Scripts that produce the input sets everything else runs on, so every algorithm below is measured against the same data rather than against whatever was convenient.

**2. Heap and Selection Sorting** — `Heap and Selecton.py`
Heap Sort and Selection Sort implemented from scratch and run across both datasets, with the sorted output written out per run and the timings charted. This is where the gap between O(n log n) and O(n²) shows up.

**3. Dijkstra and Kruskal** — `Dijkstra.py`, `Kruskal.py`
Dijkstra's shortest path and Kruskal's minimum spanning tree, each writing its results to file for inspection rather than only printing to screen.

**4. Knapsack** — `Part4.py`
A 0/1 knapsack solved by dynamic programming, using a one-dimensional table with a reverse weight sweep and backtracking to recover which items were selected. Framed as a route-planning problem over a set of stars with weight and profit values, under a fixed capacity.

## Built with

Python
