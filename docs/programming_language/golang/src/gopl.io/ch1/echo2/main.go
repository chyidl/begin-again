// Copyright © 2016 Alan A. A. Donovan & Brian W. Kernighan.
// License: https://creativecommons.org/licenses/by-nc-sa/4.0/

// See page 6.
//!+

// Echo2 prints its command-line arguments.
package main

import (
	"fmt"
	"os"
)

func main() {
	// a short variable declaration only within a function, not for package-level variables
	s, sep := "", ""
	// range produces a pair of values:
	// the index and the value
	for _, arg := range os.Args[1:] {
		// The += statement makes a new string by concatenating the old string.
		s += sep + arg
		sep = " "
	}
	fmt.Println(s)
}

//!-
