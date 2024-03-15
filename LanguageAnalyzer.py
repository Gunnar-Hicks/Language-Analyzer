# Defines a function to detect languages
def detect_language(text):
    # Creates a library that contains common words in English and Spanish that will allow the program to determine which language a text is written in
    common_words = {
        'English': {'the', 'and', 'of', 'to', 'a', 'in', 'is', 'you', 'that', 'it'},
        'Spanish': {'de', 'la', 'que', 'el', 'en', 'y', 'a', 'los', 'se', 'del'},
    }

    # Converts a text to lowercase and split it into words
    words = text.lower().split()

    # Creates an empty dictionary to store the frequency of common words within the text
    word_frequencies = {}
    # Iterates through each key-value pair in common_words
    for lang, common_words_set in common_words.items():
        # Calculates the frequency of common words for the current language, represented by lang, within the text by iterating over each word and checking if it is within the list of common words.
        # The count is then stored in the word_frequencies dictionary with the language as the key
        word_frequencies[lang] = sum(1 for word in words if word in common_words_set)

    # Finds the language with the highest word frequency, then assigns the highest to detected_language
    detected_language = max(word_frequencies, key=word_frequencies.get)

    # Returns the detected language
    return detected_language

def analyze_text(file_path):
    try:
        # Tries to read the contents of a specified file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

            # Counts the number of words after splitting the content
            words = content.split()
            word_count = len(words)

            # Count paragraphs by assuming they are separated by new lines
            paragraph_count = content.count('\n\n') + 1

            # Calls the detect_language function on the desired content and assigns it to the "language" variable
            language = detect_language(content)

            print(f"Total words: {word_count}")
            print(f"Total paragraphs: {paragraph_count}")
            print(f"Language detected: {language}")

    # Throws an exception if the file could not be found
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    # Throws an exception if another error occurs and prints the error
    except Exception as e:
        print(f"An error occurred: {e}")

# Allows the code to run when it is a script, but not when imported as a module
if __name__ == "__main__":
    # Prompts the user for the filepath of the content to be examined
    file_path = input("Enter the path to the text file (Be sure to include the file's name): ")
    # Calls the analyze_text function on the designated file
    analyze_text(file_path)
    input("Press enter to close the program.")
