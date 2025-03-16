package problems

import (
	"testing"
)

type problemData struct {
	input    []string
	expected int
}

func TestSolveProblem1Part1(t *testing.T) {
	testCases := []problemData{
		{[]string{"12"}, 2},
		{[]string{"12\t\n\n"}, 2},
		{[]string{"14"}, 2},
		{[]string{"1969", "100756"}, 34237},
	}
	checkTestCases(t, testCases, 1)
}

func TestSolveProblem1Part2(t *testing.T) {
	testCases := []problemData{
		{[]string{"14"}, 2},
		{[]string{"14\t\n\n"}, 2},
		{[]string{"1969\t\n\n"}, 966},
		{[]string{"1969", "100756"}, 51312},
	}
	checkTestCases(t, testCases, 2)
}

func checkTestCases(t *testing.T, cases []problemData, pPart int) {
	for _, c := range cases {
		result, err := SolveProblem1(c.input, pPart)
		checkProblemOutput(t, c, result, err)
	}
}

func checkProblemOutput(t *testing.T, c problemData, actual int, err error) {
	if err != nil {
		t.Fatalf("Failed for input: %v, Expected: %d, but recieved error: %s", c.input, c.expected, err)
	} else if c.expected != actual {
		t.Fatalf("Failed for input: %v, Expected: %d, but recieved %d", c.input, c.expected, actual)
	}
}
