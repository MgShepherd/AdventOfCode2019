package main

import (
	"log"
	"os"

	"github.com/MgShepherd/AdventOfCode2019/internal/problems"
	"github.com/MgShepherd/AdventOfCode2019/internal/utils"
)

func main() {
	pInput, err := utils.ReadProblemFileLines(1)
	if err != nil {
		os.Exit(1)
	}

	result, err := problems.SolveProblem1(pInput)
	if err != nil {
		os.Exit(1)
	}
	log.Printf("Problem solution is: %d\n", result)
}
