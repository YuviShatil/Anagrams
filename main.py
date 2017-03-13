CONSTANT_PRIMES = {'A': 2,  #one-time cost, simple constant dictionary of letters to primes
            'a': 2,         #this is legal because the problem explicitly states that the words are only
            'B': 3,         #alpha characters.
            'b': 3,
            'C': 5,
            'c': 5,
            'D': 7,
            'd': 7,
            'E': 11,
            'e': 11,
            'F': 13,
            'f': 13,
            'G': 17,
            'g': 17,
            'H': 19,
            'h': 19,
            'I': 23,
            'i': 23,
            'J': 29,
            'j': 29,
            'K': 31,
            'k': 31,
            'L': 37,
            'l': 37,
            'M': 41,
            'm': 41,
            'N': 43,
            'n': 43,
            'O': 47,
            'o': 47,
            'P': 53,
            'p': 53,
            'Q': 59,
            'q': 59,
            'R': 61,
            'r': 61,
            'S': 67,
            's': 67,
            'T': 71,
            't': 71,
            'U': 73,
            'u': 73,
            'V': 79,
            'v': 79,
            'W': 83,
            'w': 83,
            'X': 89,
            'x': 89,
            'Y': 97,
            'y': 97,
            'Z': 101,
            'z': 101};

def anagram_count_ints(arr):
    count = 0;
    anagrams = {};
    for int in arr: #n time
        if int not in anagrams: #constant. Dictionary lookup is O(1)
            anagrams[int] = 1;
        else:
            count+= 1;
            anagrams[int] += 1;
            if anagrams[int] == 2: count += 1; #constant
    return count;



def word_to_identifier(word):
    primes = CONSTANT_PRIMES; #map from character (case insensitive) to prime number
    i = 1; #mapping to primes will create unique identifiers for anagrams because of how prime factorization works
    for letter in word: # m time (run once for each n -- nm time total)
        i*=primes[letter] #could overflow - very unlikely and python actually uses arbitrary precision. In C would need
                            #to mod by a larger prime number to avoid overflow
    return i;

def list_to_identifiers(arr):
    int_arr = [];
    for word in arr: #n time
        int_arr.append(word_to_identifier(word)); #not sure about speed of append in python, assuming it is negligible
    return int_arr;

def anagram_count(arr):
    ints = list_to_identifiers(arr);  # take list of words, convert to unique integer, like a hash that ignores order
    return anagram_count_ints(ints);

if __name__ == "__main__":
    arr = ['Act', 'cat', 'cat', 'dog', 'dog', 'aardvark', 'pus', 'sup', 'dog', 'joseph', 'yuvi']; #could use sys library to take input from text file
    print(anagram_count(arr)); #builds map from unique integer to value, increments and returns counter accordingly.
