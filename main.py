import string

NUM_LETTERS = 26

CONSTANT_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                   47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101] #hardcoding first 26 primes. Could generate, but
                                                                    #not worth the hassle when the # of letters is
                                                                    #constant and will always be English. If we wanted
                                                                    #to count anagrams in other languages with other
                                                                    #alphabets, generating might be better.
LOWERCASE = list(string.ascii_lowercase) # ['a', 'b' ....]
UPPERCASE = list(string.ascii_uppercase) # ['A', 'B' ....]
CONSTANT_PRIMES_MAP = {};
for i in range(NUM_LETTERS):
    CONSTANT_PRIMES_MAP[LOWERCASE[i]] = CONSTANT_PRIMES[i] #map lowercase to the correct prime
    CONSTANT_PRIMES_MAP[UPPERCASE[i]] = CONSTANT_PRIMES[i] #and map uppercase the correct prime


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
    primes = CONSTANT_PRIMES_MAP; #map from character (case insensitive) to prime number
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
