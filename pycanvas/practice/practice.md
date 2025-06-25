# Practice

These are some practice problems that we are going to work on.

## Set 1
The purpose of this first set is to get some practice writing basic Python functions while reinforcing best practices. We will get experience with `flake8`, `mypy`, and `git`. 

> 💡 **Note:** AI would probably solve this in an instant — please **don’t use it**. The goal is not to be correct right away but to **learn** by practicing.

### Git Setup
1. Make sure you are in the `canvas-helper/` directory.

2. Create a branch off of this one to work on
<details>
<summary>Click to reveal the solution</summary>

```bash
git pull
git switch gustavo/practice-problems
git switch -c angel/practice-problems
```
</details>

### Prerequisites
I am assuming that you are using `wsl` here.

1. Run `python3 --version`, ensure that it is installed. Otherwise run the following:
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip -y
```

2. After installing `python3`, create a [virtual environment](https://docs.python.org/3/library/venv.html)
```bash
python3 -m venv venv
source venv/bin/activate

# You can run `deactivate` to deactivate the virtual environment
```

3. Once you are in your virtual environment, run the following to install `mypy` and `flake8`
```bash
pip install mypy flake8
```

4. Verify
```bash
mypy --version
flake8 --version
```

### The Problem Set
Take a look at `pycanvas/practice/set1/set1.py`.

We are writing three functions here. The goal is to pass all checks (like flake8 and mypy) when you make a pull request. These will show up as ✅ checkmarks in the GitHub UI once your code is clean.

Don't feel like you need to wait until the very end to make a pull request.

```python
def is_even(n: int) -> bool:
```
- This function is going to take in an integer and return true if it is even, false otherwise.
- Look into the [modulo](https://www.geeksforgeeks.org/python/what-is-a-modulo-operator-in-python/) operator
- Notice the `(n: int)` and `-> bool` here. This is telling `mypy` that we expect `n` to be an integer and the return of the function to be a boolean (`True` or `False`).

```python
def average(numbers: list[float]) -> float:
```
- This function is going to take a list of numbers (may be decimals) and return the average of them.
- Notice the `(numbers: list[float])` and `-> float` here. This is telling `mypy` that we expect `numbers` to be a list of float and the return of the function to be a float representing the average.

```python
def is_positive(n: int) -> bool:
```
- This function is going to take in an integer and return true if it is positive, false if it is negative.
- Start with whatever solution you can think of, try to make it a one liner if possible.

### Testing
There are some tests in the `tests/` directory but feel free to write your own manual tests in the file.

> If **any one** of the CI fails, the PR will show ❌. Check the **"Actions" tab** to see exactly which part failed and what the error message was.

```python
print(is_even(4))      # Expected: True
print(average([1.0, 2.0, 3.0]))  # Expected: 2.0
print(is_positive(-1)) # Expected: False
```

Running tests locally (not CI)
```bash
python3 -m unittest discover -s tests
```

Running flake locally
```bash
flake8 pycanvas tests
```

Running mypy locally
```bash
mypy pycanvas
```


