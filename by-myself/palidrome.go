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

    for scan.Scan() {
        if scan.Text() == "" || len(scan.Text()) == 1 {
            fmt.Println(scan.Text(), true)
        } else {
            line := strings.ToLower(strings.ReplaceAll(scan.Text(), " ", ""))

            for i, j := 0, len(line)-1; i < j; i,j = i+1, j-1 {
                if  line[i] != line[j] {
                     fmt.Println(scan.Text(), false)
                     break
                }
                // reached half of even or odd word so can print true
                if j-1 == i || (j-2 == i && len(line) % 2 == 1) {
                    fmt.Println(scan.Text(), true)
                }
            }
        }
    }
}

