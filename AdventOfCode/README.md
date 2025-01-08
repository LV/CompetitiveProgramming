# Advent of Code

## Usage
```sh
python3 main.py -y <YEAR> -d <DAY> -p <PART>
```

- `<YEAR>`: The year of the problem (e.g. `2015`, `2021`)
- `<DAY>`: The day of the problem (e.g. `4`, `12`)
- `<PART>`: The part number (either `1` or `2`)


## Creating a new solution
New solutions _must_ follow this template:

```python
import unittest
from util.input import run_with_input_???
import sys


def solve(input: <INPUT_TYPE>) -> <OUTPUT_TYPE>:
    # ...
    return <ANSWER>


class TestSolve(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(solve(<TEST_CASE_INPUT>), <EXPECTED_RESULT>)

    def test_example2(self):
        self.assertEqual(solve(<TEST_CASE_INPUT>), <EXPECTED_RESULT>)

    # ...


def run() -> None:
    run_with_input_???(<YEAR>, <DAY>, <PART>, sys.modules[__name__])
```
Depending on how you'd like the input file to be processed determines how the template file looks.

If you want `<INPUT_TYPE>` to be `str`, then you must use the `run_with_input_string` function.
If you want `<INPUT_TYPE>` to be `list[str]`, then you must use the `run_with_input_lines` function.

Simply add new `test_example` functions for every test case you want to add.

The running of tests, acquiring input, and running the `solve()` function is automatically taken care of.
