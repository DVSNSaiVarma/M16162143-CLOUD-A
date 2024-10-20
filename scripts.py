import os
import socket

# File paths
file1 = '/home/data/IF.txt'
file2 = '/home/data/AlwaysRememberUsThisWay.txt'
output_file = '/home/data/output/result.txt'

# Create an output directory if not exists
os.makedirs('/home/data/output', exist_ok=True)

# Function to count words in a file
def count_words(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    words = text.split()
    return len(words), words

# Handle contractions in the text
def handle_contractions(words):
    contractions = {"I'm": "I am", "can't": "cannot", "don't": "do not"}
    expanded_words = []
    for word in words:
        if word in contractions:
            expanded_words.extend(contractions[word].split())
        else:
            expanded_words.append(word)
    return expanded_words

# Get word count and most frequent words
def get_word_frequencies(words):
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:3], word_freq

# Get the IP address of the machine running the container
def get_ip_address():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)

# Main logic
total_words_file1, words_file1 = count_words(file1)
total_words_file2, words_file2 = count_words(file2)

# Handle contractions for the second file
expanded_words_file2 = handle_contractions(words_file2)

# Get top 3 words and word counts
top_words_file1, freq_file1 = get_word_frequencies(words_file1)
top_words_file2, freq_file2 = get_word_frequencies(expanded_words_file2)

# Calculate the grand total of words
grand_total_words = total_words_file1 + total_words_file2

# Get the IP address
ip_address = get_ip_address()

# Write results to the output file
with open(output_file, 'w') as f:
    f.write(f"Total words in IF.txt: {total_words_file1}\n")
    f.write(f"Total words in AlwaysRememberUsThisWay.txt: {total_words_file2}\n")
    f.write(f"Grand total of words: {grand_total_words}\n")
    f.write(f"Top 3 words in IF.txt: {top_words_file1}\n")
    f.write(f"Top 3 words in AlwaysRememberUsThisWay.txt: {top_words_file2}\n")
    f.write(f"Container IP Address: {ip_address}\n")

# Read and print the result file
with open('/home/data/output/result.txt', 'r') as result_file:
    print(result_file.read())
