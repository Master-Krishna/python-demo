def emoplyee_analysis(records,criteria):
    output = []
    dict = {}
    max = 0
    name = []

    if criteria == "high_performers":
        for x in records:
            avg = sum(x[-1])/len(x[-1])
            if avg >= 8.0:
                output += [x[0]]
        return output

    elif criteria == "department_salary":
        for x in records:
            if x[1] not in dict:
                dict[x[1]] = x[2]
            else:
                dict[x[1]] += x[2]

        return dict

    elif criteria == "consistent":
        for x in records:
            for i in x[-1]:
                if i >= 7:
                    output += [x[0]]

        return output

    elif criteria == "top_employee":
        for x in records:
            avg = sum(x[-1])/len(x[-1])
            if x[0] not  in dict:
                dict[x[0]] = avg
           
        for i,x in dict.items():
            if x > max:
                max = x
                name += [i]

        return sorted(dict,key=lambda x:dict[x],reverse=True)[0]

records = [
    ("Amit", "IT", 50000, [8, 9, 7]),
    ("Riya", "HR", 45000, [9, 9, 8]),
    ("Karan", "IT", 60000, [6, 8, 7]),
    ("Neha", "HR", 55000, [10, 9, 9])
]

print(emoplyee_analysis(records,"top_employee"))