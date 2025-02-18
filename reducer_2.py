#!/usr/bin/env python3
"""reducer.py - Processes key-value pairs received from the mapper, where each key is a word 
and each value is a document ID where the word appeared. This script aggregates the document IDs 
for each word and outputs the word alongside the set of unique document IDs where the word was found.
The reducer reads lines of input from standard input, where each line has a format of 'word,document_id'.
The input lines are expected to be sorted by the word. The reducer uses this sorted order to efficiently
aggregate document IDs by using a set data structure, transitioning between different words as it processes
the input lines one-by-one.
"""

import sys
word_counts = {}

for line in sys.stdin:
    doc_id, word, count = line.strip().split(',')
    count = int(count)
    if doc_id in word_counts:
        word_counts[doc_id].append((word, count))
    else:
        word_counts[doc_id] = [(word, count)]
for doc_id, word_count_list in word_counts.items():
    sorted_word_count_list = sorted(word_count_list, key=lambda x: x[1], reverse=True)
    for word_count in sorted_word_count_list[:2]:  
        word, count = word_count
        print(f"{doc_id},{word},{count}")
