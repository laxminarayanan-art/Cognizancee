palindrome_no=int(input("Enter the number to be checked"))
reverse=0
temp=palindrome_no
while palindrome_no > 0:
    reminder=palindrome_no % 10
    reverse=(reverse*10)+reminder
    palindrome_no=palindrome_no//10
if(temp==reverse):
    print('True')
else:
    print('False')
