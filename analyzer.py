# Simple Text Analyzer

from collections import Counter

# Input
text = input("Enter your text:\n")

# Clean text
text = text.lower()
words = text.split()

# Remove common words
stopwords = ["is", "the", "a", "an", "and", "to", "of", "in", "it"]

filtered_words = [word for word in words if word not in stopwords]

# Count frequency
word_count = Counter(filtered_words)

# Get top keywords
keywords = word_count.most_common(5)

# Stats
total_words = len(words)
total_sentences = text.count('.') + text.count('!') + text.count('?')

# Output
print("\n===== TEXT ANALYSIS =====")
print(f"Total Words: {total_words}")
print(f"Total Sentences: {total_sentences}")

print("\nTop Keywords:")
for word, count in keywords:
    print(f"{word} ({count})")