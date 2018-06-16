package main

import "fmt"
import "os"
import "strconv"

func main() {
	input, err  := strconv.Atoi(os.Args[1])
	if err!=nil { panic(err) }
	parity := 0
	for input > 0 {
		parity ^= 1
		input &= input-1
	}
	fmt.Println(parity)
}
