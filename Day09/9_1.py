student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}


student_grades={
    
}

for x in student_scores:
    if student_scores[x]>90:
        grade= "Outstanding"
    elif student_scores[x]>80:
        grade = "Exceeds Expectations"
    elif student_scores[x]>70:
        grade =  "Acceptable"
    else :
        grade = "Fail"
    student_grades[x] =grade
    
    


print(student_grades)