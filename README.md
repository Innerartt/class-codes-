# 💻 Class Codes — Python Programming

Welcome to the **Class Codes** repository. This repository contains classroom lectures, laboratory exercises, algorithm implementations, and object-oriented programming examples for Python coursework at UPES.

---

## 📂 Repository Contents

| File / Notebook | Topic / Description | Concepts Covered |
| :--- | :--- | :--- |
| **[`Matrix_Multiplication.ipynb`](Matrix_Multiplication.ipynb)** | Matrix Multiplication (Square & Asymmetric) | Nested Loops, List Comprehensions, `zip(*B)` Transposition, NumPy `@` Operator |
| **[`class 15-10-2026.py`](class%2015-10-2026.py)** | Student Management System | Object-Oriented Programming (OOP), Classes, Methods, Attributes & Calculations |
| **[`New Text Document (3).py`](New%20Text%20Document%20(3).py)** | Basic Matrix Multiplication Script | Pure Python 2D List Processing |

---

## 🧮 Featured Topic: Matrix Multiplication

### 1. Square Matrix Multiplication ($2 \times 2$)
- **Iterative Approach (3 Nested Loops):**
  Uses traditional index traversal $\mathcal{O}(n^3)$ over rows ($i$), columns ($j$), and inner dimension ($k$):
  $$C[i][j] = \sum_{k=0}^{n-1} A[i][k] \times B[k][j]$$
- **Pythonic Approach:**
  Uses `zip(*B)` to transpose columns of $B$ into rows, paired with list comprehension:
  ```python
  C = [[sum(x * y for x, y in zip(row_a, col_b)) for col_b in zip(*b)] for row_a in a]
  ```

### 2. Asymmetric (Rectangular) Matrix Multiplication
- **Condition:** $\text{Columns}(A) = \text{Rows}(B)$
- Automatically determines dimensions dynamically:
  - Matrix $A$: $m \times k$ ($2 \times 3$)
  - Matrix $B$: $k \times n$ ($3 \times 2$)
  - Result Matrix $C$: $m \times n$ ($2 \times 2$)
- **NumPy Vectorized (`@` operator):**
  ```python
  import numpy as np
  C = A @ B
  ```

---

## 🎓 Featured Topic: Object-Oriented Student Records

The [`class 15-10-2026.py`](class%2015-10-2026.py) script demonstrates OOP fundamentals by modeling student performance and academic criteria:
- **Eligibility Check:** Evaluates whether 12th board percentage meets threshold criteria ($< 60\%$).
- **Subject Average:** Computes average marks across Core Computer Science courses.
- **Attendance & Placement Score:** Aggregates attendance records and placement readiness scores.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- (Optional) NumPy and Jupyter Notebook:
  ```bash
  pip install numpy notebook
  ```

### Running the Notebooks
To start the Jupyter Notebook environment:
```bash
jupyter notebook Matrix_Multiplication.ipynb
```

### Running Python Scripts
```bash
python "class 15-10-2026.py"
```

---

## 👤 Author
**Vivek Kumar Thakur**  
Department of Computer Science & Engineering  
University of Petroleum and Energy Studies (UPES)  
GitHub: [@Innerartt](https://github.com/Innerartt)
