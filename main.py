book_path="books/frankenstein.txt"
def main():
    print("Starting bookbot")
    
    print(get_word_count())
    char_stats = get_char_statistics()
   # print(char_stats)
    letter_stats = get_letter_statistics(char_stats)
    
    print(letter_stats)
    #print(get_frankenstein())
    

def get_frankenstein():
    with open(book_path) as f:
        #print(f)
        file_contents = f.read()
        return file_contents
        
def get_word_count():
    words = get_frankenstein().split()
    return len(words)

def get_char_statistics():
    char_stats={}
    frank_letters=list(get_frankenstein().lower())
    for char in frank_letters:
        if char not in char_stats:
            char_stats[char]=1
        else:
            char_stats[char]+=1
    return char_stats


def get_letter_statistics(char_stats):
    #remove non alphabet chars
    #I guess sorting here is a waste of resources but eh it works
    sorted_letters = sorted(char_stats)
    for letter in sorted_letters:
        if not letter.isalpha():
            del char_stats[letter]

    
    #return an alpabetically sorted dict
    sorted_letters = sorted(char_stats)
  #  print(sorted_letters)
    sorted_char_stats={}
    for letter in sorted_letters:
        count = char_stats[letter]
        sorted_char_stats[letter]= count
  
    return sorted_char_stats




if __name__ == "__main__":
    main()