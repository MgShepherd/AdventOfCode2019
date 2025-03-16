package tests

import (
	"testing"

	"github.com/MgShepherd/AdventOfCode2019/internal/problems"
)

func TestSolveProblem1Part1(t *testing.T) {
	p := problems.Problem1{}
	testCases := []ProblemData{
		{[]string{"12"}, 2},
		{[]string{"12\t\n\n"}, 2},
		{[]string{"14"}, 2},
		{[]string{"1969", "100756"}, 34237},
	}
	checkTestCases(t, testCases, 1, p)
}

func TestSolveProblem1Part2(t *testing.T) {
	p := problems.Problem1{}
	testCases := []ProblemData{
		{[]string{"14"}, 2},
		{[]string{"14\t\n\n"}, 2},
		{[]string{"1969\t\n\n"}, 966},
		{[]string{"1969", "100756"}, 51312},
	}
	checkTestCases(t, testCases, 2, p)
}
