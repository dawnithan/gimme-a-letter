word = input("enter word: ")

vowel_sound = ['a', 'e', 'f', 'h', 'i','l', 'm', 'n', 'o', 'r', 's', 'x']
article = ''

for letter in word:
	if letter in vowel_sound:
		article = 'an '
	else:
		article = 'a '

	print("Gimme " + article + letter.upper())
