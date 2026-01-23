#Reverse a String

s = "hello"
print(s[::-1])

#to checl a pelindrom

s = "madam"
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


#Count Characters in a String

s = "python"
count = 0
for _ in s:
    count += 1
print(count)

#to Count Vowels

s = "education"
vowels = "aeiouAEIOU"
count = 0

for ch in s:
    if ch in vowels:
        count += 1

print(count)


#to Remove Duplicate Characters

s = "programming"
result = ""

for ch in s:
    if ch not in result:
        result += ch

print(result)

#to find Frequency of Each Character

s = "banana"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)
