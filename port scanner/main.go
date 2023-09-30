package main

import (
	"bufio"
	"fmt"
	"main/port"
	"os"
	"strconv"
)

func main() {
	fmt.Println("port scanner in golang")
	fmt.Println("select an option\n1. Initial scan(scan 1024 ports)\n2. Select port to scan")
	reader := bufio.NewReader(os.Stdin)
	choice, _ := reader.ReadString('\n')
	option, _ := strconv.Atoi(choice)
	switch option {
	case 1:
		results := port.InitialScan("localhost")
		for i := 1; i < len(results); i++ {
			fmt.Println(results)
		}
	case 2:
		fmt.Println("enter the port to scan")
		input, _ := reader.ReadString('\n')
		pno, _ := strconv.Atoi(input)
		open := port.ScanPort("tcp", "localhost", pno)
		fmt.Printf("port " + open.Port + ": " + open.State + "\n")
	default:
		fmt.Println("choose options 1 or 2")
	}

}
