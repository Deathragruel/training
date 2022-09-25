def count_words(filename):
    """ Count the approximate number of words in the file. """
    try:
        """ f is a common convention used in place of file_object.
        encoding = utf-8: This argument is used when your system's default encoding
        does not match the encoding of the file that is being read. """
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")
filenames = ['alice.txt', 'siddharta.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)