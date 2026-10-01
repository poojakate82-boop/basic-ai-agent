# Basic AI Agent

## Introduction

This project was developed as part of the course:

**02AML204 – Introduction to Artificial Intelligence**

The project demonstrates the use of AI-assisted software development practices, GitHub version control, system architecture documentation, empirical performance analysis, and the Full C4 Model.

---

## Features

- Calculator Tool
- Text Search Tool
- Command-Line Interface
- AI-Assisted Development Workflow
- Performance Analysis using py-spy
- C4 Architecture Diagrams
- Full C4 Architecture for Search System

---

## Technologies Used

- Python 3.14
- Git
- GitHub
- VS Code
- PlantUML
- Graphviz
- py-spy

---

## Justification & Analysis

Based on the profiling results, Binary Search performed better than Linear Search. Linear Search checks each element one by one, resulting in higher execution time. Binary Search divides the search space into two halves and reaches the target faster.

The measured execution times support the theoretical complexities **O(n)** for Linear Search and **O(log n)** for Binary Search. For larger datasets, the difference in performance will become even more significant.

---

# SLE-3: Architectural Design using Full C4 Model

## System Title

**Search System – Linear Search and Binary Search**

## System Description

The Search System allows a user to search for a target element in a list of data. It provides two search approaches: Linear Search and Binary Search. Linear Search checks elements sequentially, while Binary Search repeatedly reduces the search range on sorted data.

The system accepts the search input and returns the search result to the user.

---

## C4 Level 1 – Context Diagram

The Context Diagram represents the Search System as one main system and the user as the external actor.

The user provides the list and target value. The Search System processes the request using Linear Search or Binary Search and returns the search result.

**Diagram:** `docs/sle3/SLE3_Context.png`

---

## C4 Level 2 – Container Diagram

The Search System is divided into the following containers:

| Container | Responsibility |
|---|---|
| Input Module | Accepts list and target value |
| Search Controller | Selects the search algorithm |
| Linear Search | Checks elements sequentially |
| Binary Search | Searches sorted data by dividing it into halves |
| Result Module | Displays the search result |

The containers separate input, algorithm selection, search processing, and output.

**Diagram:** `docs/sle3/SLE3_Container.png`

---

## C4 Level 3 – Component Diagram

The **Binary Search Engine** is selected as the container for the component-level design.

Main components:

- Initialize Low & High
- Calculate Mid
- Compare Target with Middle Element
- Update Search Range
- Return Search Result

These components work together until the target is found or the search range becomes empty.

**Diagram:** `docs/sle3/SLE3_Component.png`

---

## C4 Level 4 – Code Diagram

The Code Level represents the main functions/code elements inside the Binary Search Engine.

Main code elements:

- `binary_search(arr, target)`
- `calculate_mid(low, high)`
- `compare_target(arr[mid], target)`
- `update_range(low, high)`
- `return_result(index)`

The code elements show the main flow of the Binary Search Engine from calculating the middle position and comparing the target to updating the search range and returning the result.

**Diagram:** `docs/sle3/SLE3_Code.png`

---

## SLE-3 Design Decisions

The Search System is divided into separate modules to keep the architecture simple and easy to understand.

Linear Search and Binary Search are kept as separate containers because they use different search approaches.

The Result Module provides a common output for both algorithms.

---

## AI Contribution Note

AI Tool Used: ChatGPT

### What AI Helped With:

- Understanding the C4 Model
- C4 architecture structure
- Diagram organization
- PlantUML diagram guidance
- Report formatting
- Documentation

### What I Did Myself:

- Created project files
- Created and organized SLE-3 diagrams
- Ran Linear Search and Binary Search programs
- Collected performance results
- Used py-spy for profiling
- Executed Git commands
- Managed the GitHub repository
- Reviewed the final architecture

---

## Project Structure

```text
basic-ai-agent/
├── README.md
├── docs/
│   ├── ADR-001-Tech-Stack.md
│   ├── C4-System-context.puml
│   ├── Contribution-Log.md
│   ├── e-Portfolio.md
│   ├── Peer-Review.md
│   └── sle3/
│       ├── SLE3_Context.puml
│       ├── SLE3_Context.png
│       ├── SLE3_Container.puml
│       ├── SLE3_Container.png
│       ├── SLE3_Component.puml
│       ├── SLE3_Component.png
│       ├── SLE3_Code.puml
│       └── SLE3_Code.png
├── src/
│   └── agent.py
├── performance-analysis/
│   ├── linear_search.py
│   ├── binary_search.py
│   └── comparison-report.md
└── images/
    ├── github-repo.png
    ├── linear-search_worst_case.png
    ├── linear-search_best_case.png
    ├── linear-search_average_case.png
    ├── binary-search_worst_case.png
    ├── binary-search_best_case.png
    ├── binary-search_average_case.png
    └── py-spy-output.png