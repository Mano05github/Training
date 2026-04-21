import collections

sentence = "python is easy and python is powerful"

words = sentence.split()
freq = collections.Counter(words)

print(freq)


