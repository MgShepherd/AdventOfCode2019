package problems

import (
	"log"
	"strconv"
	"strings"
)

type Problem1 struct{}

func (p Problem1) Solve(pInput []string, pPart int) (int, error) {
	var sumFuel int
	for _, line := range pInput {
		iVal, err := strconv.Atoi(strings.TrimSpace(line))
		if err != nil {
			log.Printf("Unable to process line: %s\n", line)
			return 0, err
		}

		if pPart == 1 {
			sumFuel += iVal/3 - 2
		} else {
			sumFuel += getFuelPart2(iVal)
		}
	}

	return sumFuel, nil
}

func getFuelPart2(mass int) int {
	if mass <= 0 {
		return 0
	}

	fuel := max(mass/3-2, 0)
	return fuel + getFuelPart2(fuel)
}
