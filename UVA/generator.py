"""
USAGE: python3 generator.py [PROBLEM NUMBER]

Generates base submission file given test case inputs and expected test case outputs
"""
from datetime import datetime
import sys
import os


def check_if_files_exist(input_file: str, output_file: str) -> None:
    if os.path.isfile(input_file):
        print(f"Input file {input_file} exists.")
        return
    if os.path.isfile(output_file):
        print(f"Output file {output_file} exists.")
        return


def get_and_write_inputs(input_file: str, output_file: str, directory: str) -> None:
    if not os.path.exists(directory):
        os.makedirs(directory)


    def read_multi_line(prompt: str) -> str:
        print(prompt)
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        return "\n".join(lines)

    try:
        inp = read_multi_line("Insert input testcases (end with blank line): ") + "\n"
        with open(input_file, 'w') as file:
            file.write(inp)

        out = read_multi_line("Insert output testcases (end with blank line): ") + "\n"
        with open(output_file, 'w') as file:
            file.write(out)

    except Exception as e:
        print(f"An error occurred: {e}")
        return


### START OF TEMPLATES ###

def print_comments(problem_title: str, problem_number: str) -> str:
    return f"""/**
 * @brief {problem_title}
 * @note https://vjudge.net/problem/UVA-{problem_number}
 * @note https://github.com/LV/CompetitiveProgramming/blob/master/UVA/UVA-{problem_number}/UVA-{problem_number}.cpp
 * @author Luis Victoria
 * @date {datetime.now().strftime('%Y-%m-%d %H:%M')}
 */"""


def imports_normal() -> str:
    return """#include <iostream>
#include <string>"""


def imports_parse() -> str:
    return """#include <iostream>
#include <string>
#include <sstream>
#include <vector>"""


def func_parse_line_ints() -> str:
    return """std::vector<int> parseLineToInts(const std::string& line)
{
    std::istringstream stream(line);
    std::vector<int> numbers;
    int number;

    while (stream >> number)
        numbers.push_back(number);

    return numbers;
}"""


def func_parse_line_ints_vec() -> str:
    return """std::vector<int> parseLineToIntsSpecifyingDimensions(const int& dimensions, const std::string& number_line)
{
    std::istringstream stream(number_line);
    std::vector<int> numbers(dimensions);
    int number;
    unsigned int count = 0;

    while (stream >> number)
        numbers[count++] = number;

    return numbers;
}"""


def func_parse_line_strs() -> str:
    return """std::vector<std::string> parseLineToStrings(const std::string& line)
{
    std::istringstream stream(line);
    std::vector<std::string> words;
    std::string word;

    while (stream >> word)
        words.push_back(word);

    return words;
}"""


def func_parse_line_strs_vec() -> str:
    return """std::vector<std::string> parseLineToStringsSpecifyingDimensions(const int& dimensions, const std::string& word_line)
{
    std::istringstream stream(word_line);
    std::vector<std::string> words(dimensions);
    std::string word;
    unsigned int count = 0;

    while (stream >> word)
        words[count++] = word;

    return words;
}"""


def func_solve_strs() -> str:
    return """void solve(std::vector<std::string>& word_line)
{
    // begin solving here
}"""


def func_solve_without_lines_ints() -> str:
    return """void solve()
{
    std::string line;

    while (std::getline(std::cin, line)) {
        std::vector<int> input_line = parseLineToInts(line);

        // begin solving here
    }
}"""


def func_solve_ints() -> str:
    return """void solve(std::vector<int>& number_line)
{
    // begin solving here
}"""


def func_solve_without_lines_strs() -> str:
    return """void solve()
{
    std::string line;

    while (std::getline(std::cin, line)) {
        std::vector<std::string> numbers = parseLineToStrings(line);

        // begin solving here
    }
}"""


def main_with_lines_vec_ints() -> str:
    return """int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(0);

    int test_cases;
    std::cin >> test_cases;
    std::cin.ignore(); // ignore newline after test_cases

    for (int t = 0; t < test_cases; ++t) {
        int dimensions;
        std::cin >> dimensions;
        std::cin.ignore(); // ignore newline after dimensions

        std::string number_line;
        std::getline(std::cin, number_line);

        std::vector<int> numbers = parseLineToIntsSpecifyingDimensions(dimensions, number_line);
        solve(numbers);
    }

    return 0;
}"""


def main_with_lines_ints() -> str:
    return """int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(0);

    int test_cases;
    std::cin >> test_cases;
    std::cin.ignore(); // ignore newline
    for (int t = 0; t < test_cases; ++t) {
        std::string line;
        std::getline(std::cin, line);

        std::vector<int> number_line = parseLineToInts(line);
        solve(number_line);
    }

    return 0;
}"""


def main_with_lines_vec_strs() -> str:
    return """int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(0);

    int test_cases;
    std::cin >> test_cases;
    std::cin.ignore(); // ignore newline after test_cases

    for (int t = 0; t < test_cases; ++t) {
        int dimensions;
        std::cin >> dimensions;
        std::cin.ignore(); // ignore newline after dimensions

        std::string word_line;
        std::getline(std::cin, word_line);

        std::vector<std::string> words = parseLineToStringsSpecifyingDimensions(dimensions, word_line);
        solve(words);
    }

    return 0;
}"""



def main_with_lines_strs() -> str:
    return """int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(0);

    int test_cases;
    std::cin >> test_cases;
    std::cin.ignore(); // ignore newline
    for (int t = 0; t < test_cases; ++t) {
        std::string line;
        std::getline(std::cin, line);

        std::vector<std::string> word_line = parseLineToStrings(line);
        solve(word_line);
    }

    return 0;
}"""


def main_without_lines() -> str:
    return """int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(0);

    solve();

    return 0;
}"""

### END OF TEMPLATES ###


def ask_and_generate_code_template(problem_number: str, problem_title: str) -> str:
    print("\nAvailable types: char, default, int, str")
    input_type = input("Specify input type: ")

    has_first_line_as_num_of_testcases: bool = False
    input_has_num_testcases_line = input("Does the first line specify number of test cases?: ")
    match input_has_num_testcases_line.lower():
        case "yes" | "ye" | "y" | "true" | "t":
            has_first_line_as_num_of_testcases = True
        case "no" | "n" | "false" | "f":
            has_first_line_as_num_of_testcases = False

    has_first_testcase_line_as_vec_length: bool = False
    input_has_vec_length = input("Does the first line of a testcase specify vector length?: ")
    match input_has_vec_length.lower():
        case "yes" | "ye" | "y" | "true" | "t":
            has_first_testcase_line_as_vec_length = True
        case "no" | "n" | "false" | "f":
            has_first_testcase_line_as_vec_length = False

    content: str = ""

    match input_type.lower():
        case "chars" | "char" | "c":
            raise NotImplementedError("Chars Template Not Implemented Yet")
        case "default" | "def" | "d":
            raise NotImplementedError("Default Template Not Implemented Yet")
        case "ints" | "int" | "i":
            content += f"{imports_parse()}\n\n"
            if has_first_testcase_line_as_vec_length:
                content += f"{func_parse_line_ints_vec()}\n\n"
                content += f"{func_solve_ints()}\n\n"
                content += main_with_lines_vec_ints()
            else:
                content += f"{func_parse_line_ints()}\n\n"
                content += f"{func_solve_ints()}" if has_first_line_as_num_of_testcases else f"{func_solve_without_lines_ints()}"
                content += f"\n\n"
                content += main_with_lines_ints() if has_first_line_as_num_of_testcases else main_without_lines()
        case "strings" | "strs" | "str" | "s":
            content += f"{imports_parse()}\n\n"
            if has_first_testcase_line_as_vec_length:
                content += f"{func_parse_line_strs_vec()}\n\n"
                content += f"{func_solve_strs()}\n\n"
                content += main_with_lines_vec_strs()
            else:
                content += f"{func_parse_line_strs()}\n\n"
                content += f"{func_solve_strs()}" if has_first_line_as_num_of_testcases else f"{func_solve_without_lines_strs()}"
                content += f"\n\n"
                content += main_with_lines_strs() if has_first_line_as_num_of_testcases else main_without_lines()
        case _:
            raise ValueError("Invalid type specified")


    final_content = f"{print_comments(problem_title, problem_number)}\n\n{content}\n"

    return final_content


def write_to_file(filename: str, content: str):
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"C++ template written to {filename}")
    except Exception as e:
        print(f"An error occurred while writing the template: {e}")


def generator(problem_number: str) -> None:
    input_title: str = input("Enter name of problem: ")
    uva_str: str = f"UVA-{problem_number}"
    input_file: str = os.path.join(uva_str, f"{uva_str}-input.txt")
    output_file: str = os.path.join(uva_str, f"{uva_str}-output.txt")
    cpp_file: str = os.path.join(uva_str, f"{uva_str}.cpp")
    check_if_files_exist(input_file, output_file)
    get_and_write_inputs(input_file, output_file, uva_str)
    write_to_file(cpp_file, ask_and_generate_code_template(problem_number, input_title))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generator.py <problem_number>")
        sys.exit(1)

    problem_number: str = sys.argv[1]
    generator(problem_number)
