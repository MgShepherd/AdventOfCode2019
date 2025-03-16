package problems

type Problem interface {
	Solve(pInput []string, pPart int) (int, error)
}
