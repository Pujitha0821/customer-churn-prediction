from collections import Counter

with open("poem.txt", "r") as file:
    text = file.read().lower()

words = text.split()

word_count = Counter(words)

max_count = max(word_count.values())

most_frequent_words = [word for word, count in word_count.items() if count == max_count]

print(f"Most frequent words: {most_frequent_words}")
print(f"Occurrences: {max_count}")
