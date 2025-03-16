package tests

import (
	"testing"

	"github.com/MgShepherd/AdventOfCode2019/internal/problems"
)

type ProblemData struct {
	input    []string
	expected int
}

func checkProblemOutput(t *testing.T, c ProblemData, actual int, err error) {
	if err != nil {
		t.Fatalf("Failed for input: %v, Expected: %d, but recieved error: %s", c.input, c.expected, err)
	} else if c.expected != actual {
		t.Fatalf("Failed for input: %v, Expected: %d, but recieved %d", c.input, c.expected, actual)
	}
}

func checkTestCases(t *testing.T, cases []ProblemData, pPart int, p problems.Problem) {
	for _, c := range cases {
		result, err := p.Solve(c.input, pPart)
		checkProblemOutput(t, c, result, err)
	}
}
