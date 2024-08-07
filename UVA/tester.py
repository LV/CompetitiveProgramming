import subprocess
import sys
from typing import List
import os

def run_test(problem_number: str) -> None:
    input_file: str = f"UVA-{problem_number}-input.txt"
    output_file: str = f"UVA-{problem_number}-output.txt"
    source_file: str = f"UVA-{problem_number}.cpp"
    executable: str = f"UVA-{problem_number}"
    temp_output_file: str = "program_output.txt"

    # Check if input, output, and source files exist
    if not os.path.isfile(input_file):
        print(f"Input file {input_file} does not exist.")
        return
    if not os.path.isfile(output_file):
        print(f"Output file {output_file} does not exist.")
        return
    if not os.path.isfile(source_file):
        print(f"Source file {source_file} does not exist.")
        return

    try:
        # Compile the C++ program
        compile_process: subprocess.CompletedProcess = subprocess.run(
            ["g++", source_file, "-o", executable],
            capture_output=True,
            text=True
        )
        if compile_process.returncode != 0:
            print("Compilation failed:")
            print(compile_process.stderr)
            return

        # Run the compiled program with input from the specified file
        with open(input_file, "r") as infile, open(temp_output_file, "w") as outfile:
            run_process: subprocess.CompletedProcess = subprocess.run(
                [f"./{executable}"],
                stdin=infile,
                stdout=outfile,
                stderr=subprocess.PIPE,
                text=True
            )
            if run_process.returncode != 0:
                print("Runtime error:")
                print(run_process.stderr)
                return

        # Compare the program's output with the expected output
        with open(temp_output_file, "r") as program_output, open(output_file, "r") as expected_output:
            program_output_lines: List[str] = program_output.readlines()
            expected_output_lines: List[str] = expected_output.readlines()

            if program_output_lines == expected_output_lines:
                print("Test passed!")
            else:
                print("Test failed!")
                print("Expected output:")
                print("".join(expected_output_lines))
                print("Program output:")
                print("".join(program_output_lines))

    finally:
        # Clean up the executable and the temporary output file
        if os.path.isfile(executable):
            os.remove(executable)
        if os.path.isfile(temp_output_file):
            os.remove(temp_output_file)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python tester.py <problem_number>")
        sys.exit(1)

    problem_number: str = sys.argv[1]
    run_test(problem_number)
