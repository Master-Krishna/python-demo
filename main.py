def emoplyee_analysis(records,criteria):
    output = []
    dict = {}

    if criteria == "high_performers":
        for x in records:
            avg = sum(x[-1])/len(x[-1])
            if avg >= 8.0:
                output += [x[0]]
        return output

    if criteria == "department_salary":
        for x in records:
            if x[1] not in dict:
                dict[x[1]] = x[2]
            else:
                dict[x[1]] += x[2]

    return dict


            
