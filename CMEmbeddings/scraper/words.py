from collections import Counter

def analyze(file_name):
	lines = open(file_name).read().splitlines()
	sentences = []

	for line in lines:
		sentence = line.split(",")
		if(len(sentence)>=2):
			sentences.append([word for word in sentence[1].split()])
		else:
			print(sentence)

	words = [word for sentence in sentences for word in sentence]

	print(len(words))


analyze("scraped/merged.txt")