# Palindrome with recursion

my_arr = [
    "Abba",
    "Aibohphobia",
    "Bib",
    "Bob",
    "Civic",
    "Deified",
    "Detartrated",
    "Dewed",
    "Eve",
    "Hannah",
    "Kayak",
    "Level",
    "Madam",
    "Malayalam",
    "Minim",
    "Mom",
    "Murdrum",
    "Noon",
    "Nun",
    "Otto",
    "Peep",
    "Pop",
    "Racecar",
    "Radar",
    "Redder",
    "Refer",
    "Repaper",
    "Rotator",
    "Rotavator",
    "Sagas",
    "Sis",
    "Solos",
    "Stats",
    "Tattarrattat",
    "Tenet",
    "Wow",
    "Aha",
    "Ava",
    "Dad",
    "Did",
    "Eke",
    "Ewe",
    "Eye",
    "Gag",
    "Gig",
    "Pip",
    "Pup",
    "Reviver",
    "Sees",
    "Sexes",
    "Succus",
    "Deed",
    "Adda",
    "Ada",
    "Ama",
    "Ana",
    "Lil",
    "Tit",
    "Tot",
    "Tut",
    "Mum",
    "Dud",
    "Tat",
    "Waw",
    "Yay",
    "Pap",
    "Did",
    "",
    "a",
    "about",
    "an",
    "and",
    "angry",
    "another",
    "answer",
    "any",
    "anyone",
    "anything",
    "anytime",
    "appear",
    "apple",
    "are",
    "area",
    "arm",
    "army",
    "around",
    "arrive",
    "art",
    "as",
    "ask",
    "at",
    "attack",
    "aunt",
    "autumn",
    "away"
    ]

def swap(s: str)-> str:
    if len(s) == 0:
        return s
    return swap(s[1:]) + s[0]

def main ():
    for i in range(len(my_arr)):
        if my_arr[i] == "":
            print (True, my_arr[i])
        elif len(my_arr[i]) % 2 != 0:
            middle = len(my_arr[i])//2
            start = my_arr[i][:middle]
            end = my_arr[i][middle+1:]
            #print(start.lower(), swap(end))
            if start.lower() == swap(end):
                print(True, my_arr[i])
            else:
                print(False, my_arr[i])
        else:
            middle = len(my_arr[i])//2
            start = my_arr[i][:middle]
            end = my_arr[i][middle:]
            #print(start.lower(), swap(end))
            if start.lower() == swap(end):
                print(True, my_arr[i])
            else:
                print(False, my_arr[i])

if __name__ == "__main__":
    main()
