package main

import (
	"bufio"
	"flag"
	"fmt"
	"os"
)

func OpenFileScanner(filePath string) (*bufio.Scanner, *os.File, error) {
	file, err := os.Open(filePath)
	if err != nil {
		fmt.Println("Error reading file:", err)
		return nil, nil, err
	}

	return bufio.NewScanner(file), file, nil
}

func main() {
	day := flag.Int("day", 0, "Day of the challenge")
	part := flag.Int("part", 0, "Part of the challenge")

	parse_error := false

	flag.Parse()

	if *day == 1 {
		scanner, file, err := OpenFileScanner("input/01.txt")
		if err != nil {
			fmt.Println("Error opening file: ", err)
			return
		}
		defer file.Close() // Ensure the file is closed after function execution

		if *part == 1 {
			fmt.Println(solve01_1(scanner))
		} else {
			parse_error = true
		}
	}

	if parse_error {
		fmt.Println("Please specify a valid challenge day and part")
		fmt.Println("e.g. ./advent-of-code -day 1 -part 1")
		os.Exit(1)
	}
}
