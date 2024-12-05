package test

import "testing"

type TestCase struct {
	Input       string
	Fn          func(string) int // Function used to test
	Answer      int              // Answer result
	Description string           // Descriptive name of the test
}

// RunTestCases loops through a slice of test cases and runs each one.
func RunTests(t *testing.T, testCases []TestCase) {
	for _, tc := range testCases {
		t.Run(tc.Description, func(t *testing.T) {
			result := tc.Fn(tc.Input)
			if result != tc.Answer {
				t.Errorf("%s: Answer %d, got %d", tc.Description, tc.Answer, result)
			}
		})
	}
}
