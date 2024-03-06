package main

import (
	"bufio"
	"fmt"
	"math"
	"strconv"
	"strings"
)


func solve01_1 (input *bufio.Scanner) int {
	var instructions []string
	for input.Scan() {
        instructions = strings.Split(input.Text(), ", ")
    }

	x := 0
	y := 0
	bearing := "n" // north

	for _, i := range instructions {
		fmt.Println(i, "  x:", x, "  y:", y)
		num, err := strconv.Atoi(i[1:])
		if err != nil {
			fmt.Println("Error converting string")
		}

		x_moved, y_moved, new_bearing := parse_instruction(string(i[0]), num, bearing)
		x += x_moved
		y += y_moved
		bearing = new_bearing
	}

	return int(math.Abs(float64(x)) + math.Abs(float64(y)))
}

func parse_instruction(direction string, movement int, bearing string) (int, int, string) {
	// move in appropriate direction
	if direction == "L" {
		if bearing == "n" {
			bearing = "w"
		} else if bearing == "w" {
			bearing = "s"
		} else if bearing == "s" {
			bearing = "e"
		} else if bearing == "e"{
			bearing = "n"
		} else {
			fmt.Println("Wrong parsing of bearing!")
		}
	} else if direction == "R" {
		if bearing == "n" {
			bearing = "e"
		} else if bearing == "e" {
			bearing = "s"
		} else if bearing == "s" {
			bearing = "w"
		} else if bearing == "w" {
			bearing = "n"
		} else {
			fmt.Println("Wrong parsing of bearing!")
		}
	} else {
		fmt.Println("Wrong parsing of direction!")
	}

	if bearing == "n" {
		return 0, movement, bearing
	} else if bearing == "e" {
		return movement, 0, bearing
	} else if bearing == "s" {
		return 0, -movement, bearing
	} else {
		return -movement, 0, bearing
	}
}
