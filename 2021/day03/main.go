package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"strconv"
	"strings"
)

type selector func(a, b int) bool

func getData() ([]string, error) {
	content, err := ioutil.ReadFile("input.txt")
	if err != nil {
		return nil, err
	}
	rows := strings.Split(strings.TrimSpace(string(content)), "\n")
	bins := make([]string, 0, len(rows))
	for _, row := range rows {
		bins = append(bins, row)
	}
	return bins, nil
}

func stringToInt(s string) int {
	output, err := strconv.ParseInt(s, 2, 64)  
	if err != nil {  
		panic("uh oh")  
	}
	return int(output)
}

func recursiveSearch(bits []string, i int, s selector) string {
	if len(bits) == 1 {
		return bits[0]
	}
	var ones, zeros []string
	for _, bit := range bits {
		if string(bit[i]) == "1" {
			ones = append(ones, bit)
		} else {
			zeros =append(zeros, bit)
		}
	}
	if s(len(ones), len(zeros)) {
		return recursiveSearch(ones, i+1, s)
	}
	return recursiveSearch(zeros, i +1, s)
}



func main() {

	data, err := getData()
	if err!=nil {
		panic("error")
	}

	// Part 1
	n := len(data[0])
	bitSums := make([]int, n)
	for i := 0; i < n; i++ {
		bitSums[i] = 0
	}
	for _, el := range data{
		for i := range el{
			if string(el[i]) == "1" {
				bitSums[i] ++
			} else {
				bitSums[i] --
			}
		}
	}
	gama := 0
	epsilon := 0
	for i, b := range bitSums{
		p := n - i - 1 
		if b > 0 {		
			gama +=  int(math.Pow(2, float64(p)))
		} else {
			epsilon += int(math.Pow(2, float64(p)))
		}
	}
	
	fmt.Printf("Part 1: %d\n", gama*epsilon) // 841526
	
	// part 2
	keepOnes := func(a, b int) bool { return a >= b}
	keepZeros := func(a, b int) bool { return a < b}
	oxygen_rating := stringToInt(recursiveSearch(data, 0, keepOnes))
	co2_rating := stringToInt(recursiveSearch(data, 0, keepZeros))

	fmt.Printf("Part 2: %d\n", oxygen_rating * co2_rating ) // 4790390

}