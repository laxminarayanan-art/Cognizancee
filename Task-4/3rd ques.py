no_of_stud=int(input("Input the number of students records :"))
list=[['ROLL Number', 'Name', 'Marks']]
for i in range(no_of_stud):
    Roll_no=int(input("Enter the roll number:"))
    Stud_name=input("Enter the student name:")
    Stud_marks=int(input("Enter the student marks"))
    list.append([Roll_no, Stud_name, Stud_marks])
for i in range(len(list)):
    for j in range(len(list[i])):
        n=list[i][j]
        print(n, end=' ')
    print('\n')
print_row=int(input("Enter the row to be printed:"))
for i in list[print_row]:
    print(i, end=' ')