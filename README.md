# Basic AI Agent

## Introduction

This project was developed as part of the course:

**02AML204 – Introduction to Artificial Intelligence**

The project demonstrates the use of AI-assisted software development practices, GitHub version control, system architecture documentation, and empirical performance analysis.

---


## Features

- Calculator Tool
- Text Search Tool
- Command-Line Interface
- AI-Assisted Development Workflow
- Performance Analysis using py-spy
- C4 Architecture Diagrams

---

## Technologies Used

- Python 3.14
- Git
- GitHub
- VS Code
- PlantUML
- py-spy

---
## Justification & Analysis
Based on the profiling results, Binary Search performed better than Linear Search. Linear Search checks each element one by one, resulting in higher execution time. Binary Search divides the search space into two halves and reaches the target faster. The measured execution times support the theoretical complexities O(n) and O(log n). For larger datasets, the difference in performance will become even more significant.

---

## AI Contribution Note
AI Tool Used: ChatGPT

What AI Helped With:
- Code structure
- Profiling guidance
- Report formatting

What I Did Myself:
- Created files
- Ran programs
- Collected results
- Executed Git commands
- Uploaded to GitHub


## Project Structure

```text
basic-ai-agent/
├── README.md
├── docs/
├── src/
├── performance-analysis/
└── images
│   ├── github-repo.png
│   ├── linear-search_worst_case.png
│   ├── linear-search_best_case.png
|   ├── linear-search_average_case.png
|   ├── binary-search_worst_case.png
│   ├── binary-search_best_case.png
|   ├── binary-search_average_case.png
│   └── py-spy-output.png

---

## Modern AI Architectures (Weeks 8–11)

Created a Multi-Agent Game Strategy architecture using PlantUML and the C4 approach.

---

## Conclusion
This profiling exercise helped me understand the practical performance difference between search algorithms. I learned how to use py-spy for profiling and how to analyze execution time using real measurements.

