# Half Adder and Full Adder – Python Program

This project is a simple Python implementation of **Half Adder** and **Full Adder** logic, which are basic building blocks in digital electronics. The program uses bitwise operators to perform binary addition and prints the truth tables for both adders.

This is mainly created for learning and understanding how binary addition works at the logic level.

---

## What This Program Does

* Implements a **Half Adder** using Python
* Implements a **Full Adder** using Python
* Prints clear **truth tables** for both
* Uses simple logic that is easy to understand for beginners

---

## Concepts Covered

* Binary addition
* Digital logic fundamentals
* Bitwise operators in Python
* Functions and loops

---

## Logic Used

### Half Adder

* Sum is calculated using XOR (`^`)
* Carry is calculated using AND (`&`)

### Full Adder

* Sum is calculated using XOR with carry input
* Carry out is calculated using a combination of AND and OR operations

---

## How to Run the Program

1. Make sure Python is installed on your system.
2. Download or clone this repository.
3. Run the file using the command below:

```bash
python half_adder.py
```

---

## Sample Output

```
HALF ADDER TRUTH TABLE
----------------------
a=0, b=0 -> Sum=0, Carry=0
a=0, b=1 -> Sum=1, Carry=0
a=1, b=0 -> Sum=1, Carry=0
a=1, b=1 -> Sum=0, Carry=1

FULL ADDER TRUTH TABLE
----------------------
a=0, b=0, carry_in=0 -> Sum=0, Carry_out=0
a=0, b=0, carry_in=1 -> Sum=1, Carry_out=0
...
```

---

## Who Can Use This

* Students learning **Digital Electronics**
* Beginners practicing **Python**
* Anyone interested in understanding **binary addition**
* Mini project for college or school assignments

---

## Files in This Repository

```
half_adder.py
README.md
```

---

If you like this project, feel free to star the repository ⭐
