tweet = input("gimme a string")

vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"] # list of all vowels i want GONE
newText = ""

for i in range(len(tweet)):       #iterates through every character in string
    if tweet[i] not in vowels:    # checks if the letter is NOT a vowel
        newText += tweet[i]       # adds the characters to new value newtext if not a vowel

tweet = newText
print(tweet)