def Check_Character(char,alphabet):
    Char = char.split()
    Ans_char = []
    Ans_idx = []
    Ans_none = ""
    
    for i in Char:
        print(i.replace(",",""))
        for j,k in enumerate(i):
            if alphabet == k.lower():
                Ans_char.append(i.replace(",",""))
                Ans_idx.append(j)
    if Ans_char == []:
        Ans_none =  "No results found"

    Ans_char = list(dict.fromkeys(Ans_char))
    Ans_idx = list(dict.fromkeys(Ans_idx))

    return Ans_char,Ans_idx,Ans_none

if __name__ == '__main__':
    Char,Index,Error = Check_Character("Cat, Dog, Ant, Cat","a")
    if Error == "":
        print(Char)
        print(Index)
    else:
        print(Error)