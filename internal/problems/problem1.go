package problems

import (
	"log"
	"strconv"
	"strings"
)

func SolveProblem1(pInput []string) (int, error) {
	var sumFuel int
	for _, line := range pInput {
		if len(line) == 0 {
			continue
		}

		iVal, err := strconv.Atoi(strings.TrimSpace(line))
		if err != nil {
			log.Printf("Unable to process line: %s\n", line)
			return 0, err
		}

		sumFuel += iVal/3 - 2
	}

	return sumFuel, nil
}
