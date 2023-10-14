student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

n=0
summ =0
for x in student_heights:
    summ += x
    n+=1
average = round(summ/n)
print(f'Average Height of students is {average}')


