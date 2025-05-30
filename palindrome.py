def is_palindrome(word):
    for i in range (0,int(len(word)/2)):
        if word[i] == word[len(word)-1-i]:
            return True
        else:
            return False
        
word = input("enter to check a palindrome : ")
if is_palindrome(word):
    print("the word is a palindrome")
else:
    print("the word is not a palindrome")

print("the lenght of the word is : " + str(int(len(word)/2)))