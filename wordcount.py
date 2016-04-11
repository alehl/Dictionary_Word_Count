def word_count(file):
	poem_file = open(file)

	ives_dictionary = {}

	for line in poem_file:
		line = line.rstrip()
		word_list = line.split(" ") # This separates the line into a list of strings
		for word in word_list:
			if word in ives_dictionary:
				ives_dictionary[word] += 1
			else:
				ives_dictionary[word] = 1
	for word, quantity in ives_dictionary.iteritems():
		quantity = ives_dictionary[word]
		print word, quantity




word_count("test.txt")