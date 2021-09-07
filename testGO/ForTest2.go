package testGO

import "fmt"

func foo(setumb []int) int {
	var result int
	for _, num := range setumb {
		result += num
	}
	return result

}

func goo() {
	fmt.Printf("second func test\n")
}

