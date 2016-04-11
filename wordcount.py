def word_count(file):
	poem_file = open(file)

	ives_dictionary = {}

	for line in poem_file:
		line = line.rstrip()
		word_list = line.split(" ")
			ives_dictionary[word] = ives_dictionary.get(word, 0) + 1

	for word, quantity in ives_dictionary.iteritems():
		quantity = ives_dictionary[word]
		print word, quantity


word_count("test.txt")