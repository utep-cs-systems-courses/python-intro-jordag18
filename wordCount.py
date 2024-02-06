import sys
import string


def count_words(input_file, output_file):
    # Initialize a dictionary to hold word counts
    word_counts = {}

    # Open the input file and read contents
    with open(input_file, 'r') as file:
        for line in file:
            # Remove punctuation, but preserve hyphens
            line = line.translate(str.maketrans('', '', string.punctuation.replace('-', '')))
            # Convert line to lowercase to ensure case-insensitivity
            words = line.lower().split()

            # Process each word
            for word in words:
                # Split hyphenated words into separate words
                subwords = word.split('-')
                for subword in subwords:
                    if subword in word_counts:
                        word_counts[subword] += 1
                    else:
                        word_counts[subword] = 1

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
    count_words(input_file, output_file)

