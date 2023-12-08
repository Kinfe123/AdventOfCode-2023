package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

type Queue struct {
	elements []rune
}

func NewQueue() *Queue {
	return &Queue{}
}

func (q *Queue) Push(e rune) {
	q.elements = append(q.elements, e)
}

func (q *Queue) Pop() rune {
	if len(q.elements) == 0 {
		return 0
	}
	e := q.elements[0]
	q.elements = q.elements[1:]
	return e
}

func main() {


	mapper := make(map[string][]string)

	sq := ""
	process := make([]string, 0)



	file, err := os.Open("./test.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()
	
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		inp := scanner.Text()
		if inp != "" {
			process = append(process, strings.ReplaceAll(inp, "\n", ""))
		}
	}
	
	sq = process[0]
	
	process = process[1:]
	for i := 0; i < len(process); i++ {
		curr := process[i]
		curr_splitted := strings.Split(curr, "=")
		mapper[strings.ReplaceAll(curr_splitted[0], " ", "")] = strings.Split(strings.Trim(curr_splitted[1][2:len(curr_splitted[1])-1], " "), ",")
	}
	
	startNode := "AAA"
	path := 0
	
	q := NewQueue()
	for _, ch := range sq {
		q.Push(ch)
	}

	sq_t := 0
	// fmt.Println("hELLO W" , string(sq[0]))
	for startNode != "ZZZ" {
		// dxn := q.Pop()
		dxn := string(sq[sq_t])
	
		temp := 0

		if dxn == "R" {
			
			temp = 1
		}

		fmt.Println(mapper[startNode] , startNode)
		startNode = mapper[startNode][temp]
		sq_t++
		sq_t %= len(sq)
		path++
	}
	fmt.Println(path)
}