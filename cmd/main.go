package main

import (
	"log"
	"os"

	"github.com/MgShepherd/AdventOfCode2019/internal/problems"
	"github.com/MgShepherd/AdventOfCode2019/internal/utils"
)

func main() {
	pInput, err := utils.ReadProblemFileLines(2)
	if err != nil {
		os.Exit(1)
	}

	p := problems.Problem2{}
	result, err := p.Solve(pInput, 2)
	if err != nil {
		os.Exit(1)
	}
	log.Printf("Problem solution is: %d\n", result)
}
