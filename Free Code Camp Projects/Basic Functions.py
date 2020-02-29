phrase = 'Giraffe Academy'
print(phrase + 'is cool')  # It is called 'Concatenation'(A series of interconnected things.)
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.islower())
print(len(phrase))

new_phrase = phrase.lower()
print(new_phrase.islower())
print(new_phrase)
   # OR
print(phrase.lower().islower())

print(phrase.replace('Giraffe', 'Elephant'))
