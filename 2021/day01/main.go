package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func getData() ([]int, error) {
	content, err := ioutil.ReadFile("input.txt")
	if err != nil {
		return nil, err
	}
	split := strings.Split(strings.TrimSpace(string(content)), "\n")
	ints := make([]int, 0, len(split))
	for _, c := range split {
		i, err := strconv.Atoi(c)
		if err != nil {
			return nil, err
		}
		ints = append(ints, i)
	}
	return ints, nil
}

func Sum(input ...int) int {
    sum := 0
    for _, i := range input {
        sum += i
    }
    return sum
}

func rollingSum(data []int, window_size int) int {
	sum := 0
	previous := Sum(data[:window_size]...)
	for i := 1; i < len(data)-window_size+1; i++ {
		current := Sum(data[i:i+window_size]...)
		if previous <  current {
			sum++
		}
		previous = current
	}
	return sum
}

func main() {
	data, err := getData()
	if err!=nil {
		panic("error")
	}
	fmt.Printf("Part 1: %d\n", rollingSum(data, 1)) // 1233
	fmt.Printf("Part 2: %d\n", rollingSum(data, 3)) // 1275

}