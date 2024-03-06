package main

import (
	"fmt"
	"math"
	"strconv"
)

func solve01_1(input []string) int {
	x := 0
	y := 0
	bearing := "n" // north

	for _, i := range input {
		num, err := strconv.Atoi(i[1:])
		if err != nil {
			fmt.Println("Error converting string")
		}

		x_moved, y_moved, new_bearing := parse_instruction01(string(i[0]), num, bearing)
		x += x_moved
		y += y_moved
		bearing = new_bearing
	}

	return int(math.Abs(float64(x)) + math.Abs(float64(y)))
}

func solve01_2(input []string) int {
	x := 0
	y := 0
	bearing := "n" // north

	type IntTuple struct {
		x_coor, y_coor int
	}

	hashSet := make(map[IntTuple]struct{})
	hashSet[IntTuple{0, 0}] = struct{}{}

	for _, i := range input {
		num, err := strconv.Atoi(i[1:])
		if err != nil {
			fmt.Println("Error converting string")
		}

		x_moved, y_moved, new_bearing := parse_instruction01(string(i[0]), num, bearing)
		if x_moved != 0 {
			is_negative := (x_moved < 0)
			if is_negative {
				x_moved = -x_moved
			}
			for i := 0; i < x_moved; i++ {
				if is_negative {
					x -= 1
				} else {
					x += 1
				}

				key := IntTuple{x, y}

				if _, exists := hashSet[key]; exists {
					return int(math.Abs(float64(x)) + math.Abs(float64(y)))
				}

				hashSet[key] = struct{}{}
			}
		} else {
			is_negative := (y_moved < 0)
			if is_negative {
				y_moved = -y_moved
			}
			for i := 0; i < y_moved; i++ {
				if is_negative {
					y -= 1
				} else {
					y += 1
				}

				key := IntTuple{x, y}

				if _, exists := hashSet[key]; exists {
					return int(math.Abs(float64(x)) + math.Abs(float64(y)))
				}

				hashSet[key] = struct{}{}
			}
		}
		bearing = new_bearing
	}

	return int(math.Abs(float64(x)) + math.Abs(float64(y)))
}

func parse_instruction01(direction string, movement int, bearing string) (int, int, string) {
	// move in appropriate direction
	if direction == "L" {
		if bearing == "n" {
			bearing = "w"
		} else if bearing == "w" {
			bearing = "s"
		} else if bearing == "s" {
			bearing = "e"
		} else if bearing == "e" {
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
