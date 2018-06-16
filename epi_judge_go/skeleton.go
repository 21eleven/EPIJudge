package main

import "fmt"
import "os"
import "strconv"

func main() {
	input, err := strconv.Atoi(os.Args[1])
	if err != nil {
		panic(err)
	}

	fmt.Println()
}
