def Check_Days(DateX,DateY,DateM):
    DateSum = [DateX.replace("/"," "),DateY.replace("/"," "),DateM.replace("/"," ")]
    Daysum = []
    Monthsum = []
    Yearsum = []
    AnsDay = ""
    NumDay = 0
    for i in DateSum:
        Daysum.append(i[0:2])
        Monthsum.append(i[3:5])
        Yearsum.append(i[6:10])
    if Yearsum[0] and Yearsum[1] == Yearsum[2]:
        if Monthsum[0] and Monthsum[1] == Monthsum[2]:
            if Daysum[2] > Daysum[0] and Daysum[2] < Daysum[1]:
                AnsDay = "true"
                NumDay = int(Daysum[2]) - int(Daysum[0]) 
            else:
                AnsDay = "false"
                NumDay = int(Daysum[2]) - int(Daysum[0])
    return AnsDay,NumDay

if __name__ == '__main__':

    AnsDay,NumDay = Check_Days("09/09/2023","12/09/2023","13/09/2023")
    print(AnsDay+",",str(NumDay) + " Days")