# Q(1):


sum_evenNumber = 0
sum_oddNumber = 0

for i in range(10):
    n = int(input(f"Enter number {i + 1}: "))
    if n % 2 == 0:
        sum_evenNumber += n
    else:
        sum_oddNumber += n

print(f"The sum of even numbers is: {sum_evenNumber}")
print(f"The sum of odd numbers is: {sum_oddNumber}")



#Q(2):
sentence = input(" Enter sentence: ")
words = sentence.split()
wordsCounter = len(words)
print(f"The number of words in the sentence is: {wordsCounter}")



#Q(3):
userInput = input("Enter string: ")
vowels = "aeiouAEIOU"
modifiedString = ''.join(char for char in userInput if char not in vowels)
print(f"The modified string  is: {modifiedString}")


#Q(4):
kelvin = float(input(" Enter temperature in Kelvin: "))
celsius = kelvin - 273.15
print(f"The temperature in Celsius is: {celsius:.2f} °C")





