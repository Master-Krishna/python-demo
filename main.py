def emoplyee_analysis(records,criteria):
    output = []
    

    if criteria == "high_performers":
        for x in records:
            avg = sum(x[-1])/len(x[-1])
            if avg >= 8.0:
                output += [x[0]]
        return output

    

            
