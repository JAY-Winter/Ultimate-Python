id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]


def solution(id_list, report) :
    
    answer = []

    people_list =[]

    for i in range(len(report)) :

        split_list = report[i].split(" ")

        people_who_report = split_list[0]
        people_who_reported = split_list[1]
                
        people = {people_who_report : people_who_reported}

        people_list.append(people)


    for answers in range(len(id_list)) :

        count = 0

        for j in range(len(people_list)) :

            for o in range(1, len(people_list)-1) :


                # print(people_list[j].values())
                if str(people_list[j].values()) == str(people_list[o].values()) : 
                    # print("yes")
                    count += 1
                # else : print("nope")
        answer.append(count)
    
    print(answer)
    
    # return answer

solution(id_list, report)