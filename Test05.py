import cv2
URL_list = []
State_URL_list = -1
URL_now = ""
URL_none_web = ""
while(1):
    command = input('คำสั่ง : ')
    if command[0:5] == "input":
        URL_list.append(command[6::])
        State_URL_list +=1
        URL_now = URL_list[State_URL_list]
        # print(URL_list)

    elif command == "prev":
        State_URL_list = State_URL_list - 1
        # print(State_URL_list)
        if State_URL_list == -1:
            URL_none_web = "No website to previous"
            State_URL_list = State_URL_list + 1
            print(URL_none_web)
        else:
            URL_now = URL_list[State_URL_list]
            print("Now you on " + URL_now)

    elif command == "next":
        State_URL_list = State_URL_list + 1
        
        if State_URL_list > len(URL_list) - 1:
            URL_none_web = "No website to go"
            State_URL_list = State_URL_list - 1
            print(URL_none_web)
        else:
            URL_now = URL_list[State_URL_list]
            print("Now you on " + URL_now)
    elif command == "current":
        print(URL_now)
    elif command == "all":
        print(URL_list)