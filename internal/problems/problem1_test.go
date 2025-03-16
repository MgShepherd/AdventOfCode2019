package problems

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

type problemData struct {
	input    []string
	expected int
}

func TestSolveProblem1(t *testing.T) {
	testCases := []problemData{
		{[]string{"12"}, 2},
		{[]string{"12\t\n\n"}, 2},
		{[]string{"14"}, 2},
		{[]string{"1969", "100756"}, 34237},
	}
	checkTestCases(t, testCases)
}

func checkTestCases(t *testing.T, cases []problemData) {
	for _, c := range cases {
		result, err := SolveProblem1(c.input)
		checkProblemOutput(t, c.expected, result, err)
	}
}

func checkProblemOutput(t *testing.T, expected, actual int, err error) {
	if err != nil {
		t.Fatalf("Expected result: %d, but recieved error: %s", actual, err)
	}
	assert.Equal(t, expected, actual)
}
