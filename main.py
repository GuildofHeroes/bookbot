def word_count(text):
    
    words = text.split()

    return len(words)

def book_character_count(text):

    counts = {}

    lower_text = text.lower()

    for char in lower_text:

        if char.isalpha():    # just this simple condition
            
            if char in counts:
                
                counts[char] += 1
            
            else:
                
                counts[char] = 1
    
    return counts

def sort_character_count(counts):
    
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

    return sorted_counts



def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count(file_contents)} words found in the document\n")

    char_counts = sort_character_count(book_character_count(file_contents))
    # Now loop through char_counts and format each line
    for char, count in char_counts:
        print(f"The '{char}' character was found {count} times")
        
    print("--- End report ---") 

if __name__ == "__main__":
    
    main()