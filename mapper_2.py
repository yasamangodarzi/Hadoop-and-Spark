#!/usr/bin/env python3
"""mapper.py - This mapper script reads text input from standard input, in the format "document_id,text".
It processes each line to extract words and emits each word along with the document ID it appeared in. 
Each word is emitted only once per document to ensure uniqueness.
"""
import sys
word_counts = {}
for line in sys.stdin:
    doc_id, text = line.strip().split(',', 1)
    words = text.split(" ")
    for word in words:
        if (doc_id, word) in word_counts:
            word_counts[(doc_id, word)] += 1
        else:
            word_counts[(doc_id, word)] = 1
for doc_word, count in sorted(word_counts.items(), key=lambda x: x[1], reverse=True):
    doc_id, word = doc_word
    print(f"{doc_id},{word},{count}")
