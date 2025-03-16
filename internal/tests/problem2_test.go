package tests

import (
	"testing"

	"github.com/MgShepherd/AdventOfCode2019/internal/problems"
)

func TestSolveProblem2Part1(t *testing.T) {
	p := problems.Problem2{}
	testCases := []ProblemData{
		{[]string{"1,0,0,0,99"}, 2},
		{[]string{"2,3,0,3,99"}, 2},
		{[]string{"2,4,4,5,99,0"}, 2},
		{[]string{"1,1,1,4,99,5,6,0,99"}, 30},
	}
	checkTestCases(t, testCases, 1, p)
}
