maths=int(input("enter the marks in maths out of 100:"))
science=int(input("enter the marks in science out of 100:"))
english=int(input("enter the marks in english out of 100:"))
total_marks=maths+science+english
average_marks=total_marks/3
print(f"Total Marks:{total_marks}\nAverage Marks:{average_marks}")
if(average_marks>=90 ):
    print("Grade:A+")
elif(average_marks>=80 and average_marks<90):
    print("Grade:A")
elif(average_marks>=70 and average_marks<80):
    print("Grade:B+")
elif(average_marks>=60 and average_marks<70):
    print("Grade:B")
elif(average_marks>=50 and average_marks<60):
    print("Grade:c+")
elif(average_marks>=40 and average_marks<50):
    print("Grade:c")
else:
    print("Grade:Fail")