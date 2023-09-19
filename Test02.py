def Check_numbers2(num,i,j):
    Ans = ''
    for n in range(1,num+1):
        if n%i == 0 and n%j != 0:
            Ans = Ans + str(n) + " Ping" + "\n"
        elif n%j == 0 and n%i != 0:
            Ans = Ans + str(n) + " Pong" + "\n"
        elif n%i == 0 and n%j == 0:
            Ans = Ans + str(n) + " Ping Pong" + "\n"
    return Ans

if __name__ == '__main__':
    Answer = Check_numbers2(35,5,7)
    print(Answer)