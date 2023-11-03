"""
Input Format
The first line contains the integer n, the number of students' records. The next n
lines contain the names and marks obtained by a student, each value separated by a
space. The final line contains query_name, the name of a student to query.

Sample Input 
3
Krishna 67 68 69
Arjun 79 98 63
Malika 52 56 60
Malika

Sample Output 
56.06
"""
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    total=0
    for i in student_marks[query_name]:
        total+=i
    sonuc=(float(total/3))
    print(f"{sonuc:.2f}")
   
