if __name__ == '__main__':
    
    records=[]
    names=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    
    scores = set([student[1] for student in records])
    second_lowest=sorted(scores)[1]
  
    for student in records:
        if student[1] == second_lowest:
            names.append(student[0])
    
    names.sort()
    for name in names:
        print(name)
