#! /usr/bin/env python3
import os
import re
import sys
import string


def count_words(input_file, output_file):
    # Initialize a dictionary to hold word counts
    word_counts = {}

    # Compile a regular expression pattern for matching words (including hyphenated words)
    # This pattern matches sequences of alphanumeric characters and hyphens but excludes leading or trailing hyphens
    word_pattern = re.compile(r'\b[\w]+\b')

    # Open the input file and read contents
    with open(input_file, 'r') as file:
        for line in file:
            # Convert found words to lowercase to ensure case-insensitivity
            words = [word.lower() for word in word_pattern.findall(line)]

            # Process each word
            for word in words:
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1

    # Sort the words alphabetically
    sorted_words = sorted(word_counts.items())

    # Write the counts to the output file
    with open(output_file, 'w') as file:
        for word, count in sorted_words:
            file.write(f"{word} {count}\n")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python wordCount.py input.txt output.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # make sure text files exist
    if not os.path.exists(input_file):
        print("text file input %s doesn't exist! Exiting" % input_file)
        exit()

    count_words(input_file, output_file)

