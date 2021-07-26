// Copyright © 2016 Alan A. A. Donovan & Brian W. Kernighan.
// License: https://creativecommons.org/licenses/by-nc-sa/4.0/

// See page 8.
//!+

// Dup1 prints the text of each line that appears more than
// once in the standard input, preceded by its count.
package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	/*
	   A map holds a set of key/value pairs and provides constant-time operations to store, retrieve, or test for an item in the set.
	*/
	counts := make(map[string]int)
	// Scanner that reads input and breaks it into lines or words
	input := bufio.NewScanner(os.Stdin)

	for input.Scan() {
		counts[input.Text()]++
	}
	// NOTE: ignoring potential errors from input.Err()
	for line, n := range counts {
		if n > 1 {
			// formatted output from a list of expressions.
			fmt.Printf("%d\t%s\n", n, line)
		}
	}
}

/**
➜ go run main.go
say
say
say
hello
3D      say
*/
//!-
