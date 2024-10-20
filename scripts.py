import re
import socket
from collections import Counter

# Dictionary to handle common contractions
contraction_mapping = {
    "n't": " not", "'re": " are", "'s": " is", "'d": " would",
    "'ll": " will", "'t": " not", "'ve": " have", "'m": " am"
}

# Function to expand contractions
def expand_contractions(text):
    for contraction, expanded in contraction_mapping.items():
        text = re.sub(contraction, expanded, text)
    return text

# Function to process a file, expand contractions, and count words
def process_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    # Expand contractions
    text = expand_contractions(text.lower())
    
    # Use regex to split the text into words
    words = re.findall(r'\b\w+\b', text)
    
    # Count word frequencies
    word_counts = Counter(words)
    total_words = len(words)
    
    # Get top 3 most common words
    top_words = word_counts.most_common(3)
    
    return total_words, top_words

# Function to get the container's IP address
def get_container_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

# Main function to handle both files, calculate totals, and write output
def main():
    # Process both text files
    total_if, top_if = process_file("IF.txt")
    total_always, top_always = process_file("AlwaysRememberUsThisWay.txt")
    
    # Calculate grand total of words
    grand_total = total_if + total_always
    
    # Get container IP address
    container_ip = get_container_ip()
    
    # Prepare the result text
    result = (
        f"Total words in IF.txt: {total_if}\n"
        f"Total words in AlwaysRememberUsThisWay.txt: {total_always}\n"
        f"Grand total of words: {grand_total}\n"
        f"Top 3 words in IF.txt: {top_if}\n"
        f"Top 3 words in AlwaysRememberUsThisWay.txt: {top_always}\n"
        f"Container IP Address: {container_ip}\n"
    )
    
    # Write result to a file
    with open("/home/data/output/result.txt", "w") as f:
        f.write(result)
    
    # Print the result to the console
    print(result)

if __name__ == "__main__":
    main()
