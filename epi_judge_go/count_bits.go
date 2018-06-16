package main

import "fmt"
import "os"
import "strconv"

func main() {
	input, err := strconv.Atoi(os.Args[1])
	if err != nil {
		panic(err)
	}
	bits := 0
	for input > 0 {
		bits += 1
		input &= input - 1
	}

	fmt.Println(bits)
}
