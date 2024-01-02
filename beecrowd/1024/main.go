package main

import (
	"bufio"
	"fmt"
	"os"
)

func isLetter(ch rune) bool {
    return ch >= 65 && ch <= 90 || ch >= 97 && ch<=122
}

func main() {

	scanner := bufio.NewScanner(os.Stdin)

    first_line := true
    var data string
    for scanner.Scan() {
        if scanner.Text() != "" && !first_line {
            line := []rune(scanner.Text())
                for i := range line {
                    if isLetter(line[i]) {
                        line[i] = line[i]+3
                    }
                }
                for i, j := 0, len(line)-1; i < j; i, j = i+1, j-1 {
                    line[i], line[j] = line[j], line[i]
                }
                half := len(line)/2
                for i,val := range line[len(line)/2:] {
                    if len(line)%2 == 0 {
                        line[len(line)-half+i] = val-1
                    } else {
                        line[len(line)-half-1+i] = val-1
                    }
                }
                data += string(line)+"\n"
        }
        first_line = false
    }
    fmt.Println(data) 
}
