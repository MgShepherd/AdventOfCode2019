package problems

import (
	"errors"
	"fmt"
	"log"
	"strconv"
	"strings"
)

type Problem2 struct{}

func (p Problem2) Solve(pInput []string, pPart int) (int, error) {
	input := pInput[0]
	elements, err := convertToIntSlice(strings.Split(input, ","))
	if err != nil {
		return 0, err
	}

	if pPart == 1 {
		return runProgram(elements)
	}
	return solvePart2(elements)
}

func runProgram(elements []int) (int, error) {
	i := 0
	var err error
	shouldExit := false
	for !shouldExit {
		shouldExit, err = processOp(elements, i)
		if err != nil {
			return 0, err
		}
		i += 4
	}
	return elements[0], nil
}

func solvePart2(startingElements []int) (int, error) {
	noun, verb, output := -1, 0, 0
	var err error
	elements := make([]int, len(startingElements))

	for output != 19690720 {
		if noun < 100 {
			noun += 1
		} else {
			verb += 1
			noun = 0
		}

		copy(elements, startingElements)
		elements[1] = noun
		elements[2] = verb
		output, err = runProgram(elements)
		if err != nil {
			return 0, err
		}
	}

	return 100*noun + verb, nil
}

func convertToIntSlice(vals []string) ([]int, error) {
	var ints []int
	for _, element := range vals {
		iVal, err := strconv.Atoi(element)
		if err != nil {
			log.Printf("Unable to convert value %s into integer\n", element)
			return ints, err
		}
		ints = append(ints, iVal)
	}
	return ints, nil
}

func processOp(elements []int, index int) (bool, error) {
	switch elements[index] {
	case 1:
		val1, val2 := elements[elements[index+1]], elements[elements[index+2]]
		elements[elements[index+3]] = val1 + val2
		return false, nil
	case 2:
		val1, val2 := elements[elements[index+1]], elements[elements[index+2]]
		elements[elements[index+3]] = val1 * val2
		return false, nil
	case 99:
		return true, nil
	default:
		errMsg := fmt.Sprintf("Unable to process opcode: %d\n", elements[index])
		log.Printf(errMsg)
		return false, errors.New(errMsg)
	}
}
