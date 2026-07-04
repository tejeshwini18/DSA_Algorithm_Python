# DSA_Algorithm_Python

A comprehensive collection of **Data Structures and Algorithms** implementations in Python, designed for interview preparation and algorithm mastery. This repository contains practical solutions, detailed explanations, and interview-ready transcripts to help you ace technical interviews.

---

## 📋 Table of Contents

- [About This Repository](#about-this-repository)
- [Key Features](#key-features)
- [Repository Structure](#repository-structure)
- [Tech Stack](#tech-stack)
- [Installation & Setup](#installation--setup)
- [Content Overview](#content-overview)
- [Interview Transcripts](#interview-transcripts)
- [How to Use](#how-to-use)
- [Contributing](#contributing)

---

## About This Repository

This repository is a curated resource for software engineers preparing for technical interviews or looking to strengthen their understanding of data structures and algorithms. Each problem includes:

- **Clean, optimized Python implementations**
- **Multiple approaches** (brute force, optimized, advanced)
- **Time and space complexity analysis**
- **Interview-ready transcripts** for verbal explanation practice
- **Executable examples** with test cases

Whether you're preparing for FAANG interviews or just leveling up your DSA skills, this repository has you covered.

---

## 🎯 Key Features

✅ **25+ Curated DSA Problems** - Hand-picked problems that frequently appear in tech interviews  
✅ **Interview Transcripts** - Detailed, human-friendly explanations for every problem  
✅ **Multiple Solutions** - Compare brute force, optimized, and advanced approaches  
✅ **Complexity Analysis** - Time and space complexity for each solution  
✅ **Executable Code** - All files include runnable examples with `if __name__ == "__main__"` blocks  
✅ **Well-Organized** - Structured by problem type: Arrays, Trees, Graphs, Dynamic Programming, etc.  
✅ **Python 3.8+** - Modern Python with type hints and best practices  

---

## 📁 Repository Structure

```
DSA_Algorithm_Python/
│
├── README.md                          # This file
│
├── DSA_Problems/                      # Core DSA interview problems
│   ├── 01_lru_cache.py
│   ├── 02_lfu_cache.py
│   ├── 03_find_median_from_data_stream.py
│   ├── 04_merge_k_sorted_lists.py
│   ├── 05_word_ladder.py
│   ├── ... (18 problems total)
│   │
│   ├── interview_transcripts/         # Verbal explanation scripts
│   │   ├── README.md
│   │   ├── 01_lru_cache_transcript.md
│   │   ├── 02_lfu_cache_transcript.md
│   │   └── ... (one per problem)
│   │
│   └── README.md                      # DSA Problems overview
│
├── algorithms/                        # Algorithm implementations by category
│   ├── sorting/
│   ├── searching/
│   ├── graph_traversal/
│   ├── dynamic_programming/
│   │
│   ├── interview_transcripts/         # Explanations for algorithms
│   │   └── README.md
│   │
│   └── README.md                      # Algorithms overview
│
└── data_structures/                   # Data structure implementations
    ├── linked_lists/
    ├── trees/
    ├── heaps/
    ├── hash_tables/
    │
    ├── interview_transcripts/         # Explanations for data structures
    │   └── README.md
    │
    └── README.md                      # Data Structures overview
```

---

## 💻 Tech Stack

| Component | Version |
|-----------|---------|
| **Language** | Python 3.8+ |
| **Format** | 77.4% Python, 22.6% Jupyter Notebooks |
| **Dependencies** | None (pure Python stdlib) |
| **Testing** | Built-in examples with `if __name__ == "__main__"` |

---

## Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/tejeshwini18/DSA_Algorithm_Python.git
   cd DSA_Algorithm_Python
   ```

2. **Verify Python installation**
   ```bash
   python --version
   ```

3. **Run any problem solution**
   ```bash
   python DSA_Problems/01_lru_cache.py
   ```

4. **Explore Jupyter Notebooks** (optional)
   ```bash
   pip install jupyter
   jupyter notebook
   ```

---

## 📚 Content Overview

### DSA Problems (18+ Solutions)

| # | Problem | Category | Difficulty |
|---|---------|----------|-----------|
| 01 | LRU Cache | Design | Hard |
| 02 | LFU Cache | Design | Hard |
| 03 | Find Median from Data Stream | Heap | Hard |
| 04 | Merge K Sorted Lists | Heap | Hard |
| 05 | Word Ladder | Graph/BFS | Medium |
| 06 | Detect Cycle in Directed Graph | Graph | Medium |
| 07 | Kth Largest Element in a Stream | Heap | Medium |
| 08 | Top K Frequent Elements | Heap | Medium |
| 09 | Maximum Subarray Sum (Kadane) | DP | Medium |
| 10 | Sliding Window Maximum | Deque | Hard |
| 11 | Longest Substring Without Repeating | Sliding Window | Medium |
| 12 | Minimum Window Substring | Sliding Window | Hard |
| 13 | Lowest Common Ancestor (Binary Tree) | Tree | Medium |
| 14 | Serialize & Deserialize Binary Tree | Tree | Hard |
| 15 | Number of Islands | DFS/BFS | Medium |
| 16 | Course Schedule (Topological Sort) | Graph | Medium |
| 17 | Coin Change (DP) | DP | Medium |
| 18 | Task Scheduler with Priorities | Greedy | Medium |

For the complete list and problem links, see [`DSA_Problems/README.md`](DSA_Problems/README.md)

### Algorithms

- Sorting Algorithms (Quick Sort, Merge Sort, etc.)
- Searching Algorithms (Binary Search, etc.)
- Graph Traversal (BFS, DFS, Topological Sort)
- Dynamic Programming Techniques
- Greedy Algorithms

See [`algorithms/README.md`](algorithms/README.md) for details.

### Data Structures

- Linked Lists
- Binary Trees & BSTs
- Heaps & Priority Queues
- Hash Tables & Dictionaries
- Graphs & Adjacency Lists

See [`data_structures/README.md`](data_structures/README.md) for details.

---

## 🎤 Interview Transcripts

Each problem has a detailed, interview-ready transcript that explains:
- The problem statement in simple terms
- Your thought process and approach
- Step-by-step solution walkthrough
- Complexity analysis
- Potential follow-up questions

**Transcripts are available in:**
- [`DSA_Problems/interview_transcripts/`](DSA_Problems/interview_transcripts/README.md)
- [`algorithms/interview_transcripts/`](algorithms/interview_transcripts/README.md)
- [`data_structures/interview_transcripts/`](data_structures/interview_transcripts/README.md)

---

## 🚀 How to Use

### For Interview Preparation

1. **Pick a problem** from the DSA_Problems directory
2. **Read the problem** and try solving it yourself first (15-30 min)
3. **Check the solution** in the corresponding `.py` file
4. **Review the transcript** to practice your verbal explanation
5. **Analyze complexity** and understand trade-offs
6. **Repeat** with different problems

### For Learning

1. **Explore data structures** first to build foundational knowledge
2. **Study algorithms** to understand common patterns
3. **Solve DSA problems** to apply these concepts
4. **Use transcripts** to learn how to explain solutions clearly

### Running Examples

Each file includes runnable examples:

```bash
python DSA_Problems/01_lru_cache.py
```

Output will show test cases and results.

---

## 📝 Contributing

Contributions are welcome! If you'd like to:

- Add new problems or solutions
- Improve existing explanations
- Fix bugs or optimize code
- Add more interview transcripts

Please feel free to open a pull request or issue.

---

## 📄 License

This repository is open source and available under the MIT License.

---

## 🙋 Support & Questions

If you have questions or need clarification on any topic, feel free to open an issue or reach out.

**Happy Learning! 🎉**

---

**Last Updated:** July 2026  
**Language Composition:** 77.4% Python | 22.6% Jupyter Notebook
