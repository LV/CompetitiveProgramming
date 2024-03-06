package main

import (
	"fmt"
	"testing"
)

func TestSolve01_1(t *testing.T) {
	var tests = []struct {
		inp  []string // input
		want int      // expected result
	}{
		{[]string{"R2", "L3"}, 5},
		{[]string{"R2", "R2", "R2"}, 2},
		{[]string{"R5", "L5", "R5", "R3"}, 12},
	}

	for _, tt := range tests {
		testname := fmt.Sprintf("Test \"%s\"", tt.inp)
		t.Run(testname, func(t *testing.T) {
			got := solve01_1(tt.inp)
			if got != tt.want {
				t.Errorf("got %d, want %d", got, tt.want)
			}
		})
	}
}

func TestSolve01_2(t *testing.T) {
	var tests = []struct {
		inp  []string // input
		want int      // expected result
	}{
		{[]string{"R8", "R4", "R4", "R8"}, 4},
	}

	for _, tt := range tests {
		testname := fmt.Sprintf("Test \"%s\"", tt.inp)
		t.Run(testname, func(t *testing.T) {
			got := solve01_2(tt.inp)
			if got != tt.want {
				t.Errorf("got %d, want %d", got, tt.want)
			}
		})
	}
}
