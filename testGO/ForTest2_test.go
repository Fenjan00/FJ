package testGO

import (
	"fmt"
	"github.com/stretchr/testify/suite"
	"testing"

)

type run_Suite struct {
	suite.Suite
}

// SetupSuite() 和 TearDownSuite() 仅执行一次
// SetupTest() TearDownTest() BeforeTest() AfterTest() 对套件中的每个测试执行一次

func (s *run_Suite) AfterTest(suiteName,testName string) {
	fmt.Printf("4.AferTest: suiteName=%s,testName=%s\n",suiteName,testName)
}

func (s *run_Suite) BeforeTest(suiteName,testName string) {
	fmt.Printf("3.BeforeTest: suiteName=%s,testName=%s\n",suiteName,testName)
}

// SetupSuite() 仅执行一次
func (s *run_Suite) SetupSuite() {
	fmt.Printf("1.SetupSuite() ...\n")
}

// TearDownSuite() 仅执行一次
func (s *run_Suite) TearDownSuite() {
	fmt.Printf("6.TearDowmnSuite()...\n")
}

func (s *run_Suite) SetupTest() {
	fmt.Printf("2.SetupTest()... \n")
}

func (s *run_Suite) TearDownTest() {
	fmt.Printf("5.TearDownTest()... \n")
}

func (s *run_Suite) TestFoo() {
		set := []int{17, 23, 100, 76, 55}
		foo(set)
}

func (s *run_Suite) TestGoo() {
	goo()   //9.
}

// 让 go test 执行测试
func TestGooFoo(t *testing.T) {
	suite.Run(t,new(run_Suite))
}
