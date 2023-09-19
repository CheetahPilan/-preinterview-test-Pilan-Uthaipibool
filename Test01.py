def Check_numbers(num):
    Ans = ''
    for i in range(1,num+1):
        if i%3 == 0 and i%5 != 0:
            Ans = Ans + str(i) + " Ping" + "\n"
        elif i%5 == 0 and i%3 != 0:
            Ans = Ans + str(i) + " Pong" + "\n"
        elif i%3 == 0 and i%5 == 0:
            Ans = Ans + str(i) + " Ping Pong" + "\n"
    return Ans

if __name__ == '__main__':
    Answer = Check_numbers(6)
    print(Answer)