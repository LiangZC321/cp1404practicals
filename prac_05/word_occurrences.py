word_input = input("Enter a string: ")
words = word_input.split()
word_counts = {}

for word in words:
    word = word.lower()
    word_counts[word] = word_counts.get(word, 0) + 1
max_word_length = max(len(word) for word in word_counts)

print("Word Counts:")
for word, count in sorted(word_counts.items()):
    print(f"{word:{max_word_length}} : {count}")