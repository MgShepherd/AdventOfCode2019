package utils

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func ReadProblemFileLines(problemNumber int) ([]string, error) {
	path := fmt.Sprintf("resources/problems/problem%d.txt", problemNumber)
	file, err := os.Open(path)
	if err != nil {
		log.Printf("Unable to open file at location: %s\n", path)
		return nil, err
	}

	var output []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		output = append(output, scanner.Text())
	}

	return output, nil
}
