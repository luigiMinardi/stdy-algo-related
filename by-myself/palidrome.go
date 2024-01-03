package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)
 
func main() {
    file, _ := os.Open("palindromes")

    scan := bufio.NewScanner(file)

    counter := 0
    for scan.Scan() {
        counter = counter + 1
        fmt.Println(counter)
        if scan.Text() == "" || len(scan.Text()) == 1 {
            fmt.Println(scan.Text(), true)
        } else {
            for i, j := 0, len(scan.Text())-1; i < j; i,j = i+1, j-1 {
                //fmt.Println(i,j, strings.ToLower(string(scan.Text()[i])) == strings.ToLower(string(scan.Text()[j])))
                if  strings.ToLower(string(scan.Text()[i])) != strings.ToLower(string(scan.Text()[j])) {
                     fmt.Println(scan.Text(), false)
                     break
                }
                if (j-1 == i || j-2 == i && len(scan.Text()) % 2 == 1) {
                    fmt.Println(scan.Text(), true)
                }
            }
        }
    }
}

