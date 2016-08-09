def word_count(file):
	poem_file = open(file, 'r')

	wordcount = 0

	for lines in poem_file:
		word_count1 = lines.split()
		wordcount += len(word_count1)
	poem_file.close()

	print str(wordcount)

word_count("alejandra.txt")
