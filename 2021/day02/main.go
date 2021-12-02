package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

type Command struct {
	direction string
	units int
}
type SubmarinePosition struct {
	horizontal int
	depth int
	aim int
}

// Part 1
func (s *SubmarinePosition) performCommandPart1(c Command){
	switch c.direction {
	case "forward":
		s.horizontal += c.units
	case "down":
		s.depth += c.units
	case "up":
		s.depth -= c.units
	}
}

// Part 2
func (s *SubmarinePosition) performCommandPart2(c Command){
	switch c.direction {
	case "forward":
		s.horizontal += c.units 
		s.depth += c.units * s.aim
	case "down":
		s.aim += c.units
	case "up":
		s.aim -= c.units
	}
}

func (s *SubmarinePosition) getAnswer() int {
	return s.depth * s.horizontal
}

func getData() ([]Command, error) {
	content, err := ioutil.ReadFile("input.txt")
	if err != nil {
		return nil, err
	}
	rows := strings.Split(strings.TrimSpace(string(content)), "\n")
	cmds := make([]Command, 0, len(rows))
	for _, row := range rows {
		el := strings.Split(strings.TrimSpace(string(row)), " ")
		units, err := strconv.Atoi(el[1])
		if err != nil {
			return nil, err
		}
		cmds = append(cmds, Command{el[0], units})
	}
	return cmds, nil
}


 func main() {
	
	data, err := getData()
	if err!=nil {
		panic("error")
	}
	sub1 := SubmarinePosition{0, 0, 0}
	sub2 := SubmarinePosition{0, 0, 0}
	for _, cmd := range data {
		sub1.performCommandPart1(cmd)
		sub2.performCommandPart2(cmd)
	}
	fmt.Printf("Part 1: %d\n", sub1.getAnswer()) // 1480518
	fmt.Printf("Part 2: %d\n", sub2.getAnswer()) // 1282809906

}