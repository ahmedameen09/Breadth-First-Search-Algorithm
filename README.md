# Breadth-First Search (BFS) Algorithm in Python

Welcome to the repository containing a Python implementation of the Breadth-First Search (BFS) algorithm, meticulously crafted for Algorithms and Data Structures students and enthusiasts. BFS is a venerable algorithm within the graph searching taxonomy and is pivotal for those venturing into the computational sciences.

## Overview

Graphical algorithms by nature are abstract, necessitating a representational form that is computationally digestible. This project endeavors to bridge this abstraction by translating a visual graph into a dictionary-represented format, facilitating comprehension by algorithmic processes.

### Graph Representation

The vertices in our BFS algorithm are classified by their directional relationship within the traversal process:

- `points_p`: Vertices listed alongside their adjacent vertices in the positive direction.
- `points_n`: Vertices listed alongside their adjacent vertices in the negative direction.

Understanding the traversal directionality is crucial for BFS, as the conventional approach is to progress from the leftmost (start) to the rightmost (end) vertices within a graph.

### Direction Determination

The search direction, as dictated by user input, is determined in the following manner:

```python
if start < end:
    # Positive direction is established
elif start > end:
    # Negative direction is established

## BFS Algorithm Function

At the heart of the function, a queue data structure is employed to orchestrate the BFS:

- The queue is primed with the `start` vertex.
- Vertices are enqueued and dequeued in an orderly fashion, ensuring a breadth-first traversal and preventing cyclic loops.
- Adjacent vertices are tiered and examined against the target `end` vertex.
- On queue depletion, we emerge with a complete BFS path, starting from the initial vertex.
- The algorithm then identifies the `end` vertex and collates vertices of the corresponding level into the `BFS2` list.
- Outputs presented are the BFS complete path, the specific path from the start to the end level, and the hierarchical levels of all involved vertices.

## Usage

To run the BFS algorithm, proceed as follows:

1. Confirm Python installation on your machine.
2. Clone this repository to your desired directory.
3. Run the Python script and respond to the input prompts for the start and end points.

## Conclusion

This BFS algorithm encapsulates a fundamental graph traversal technique in Python, accentuating the language's efficacy in translating complex algorithmic concepts into tangible implementations. It serves as a substantive educational resource for computer science students to grasp graph theory and data structures in practice.

We encourage users to immerse themselves in the code, experiment, and grasp the underlying mechanisms of the BFS operation within graph structures.
