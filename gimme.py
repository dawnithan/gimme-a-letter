word = input("enter word: ")

vowel_sound = ['a','e','i','o','r','s','f','h']
article = ''

for letter in word:
	if letter in vowel_sound:
		article = 'an '
	else:
		article = 'a '

	print("Gimme " + article + letter.upper())