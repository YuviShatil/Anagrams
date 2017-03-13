# Anagrams
Solves the following interview question in linear time:

The Anagram problem: Output the number of words w in a list of n words, such that at least one of the other n-1 words in the list is an anagram of w. A word is an anagram of itself. Ignore case. The input has only alpha characters. For example:

    anagram_count( ['Act', 'cat', ‘cat’, 'dog', 'dog', 'aardvark'] ) returns 5

The algorithm should perform reasonably when operating on a list of 1 million words. You can write in the language of your choice or in pseudo-code. Also describe the complexity of your algorithm using O notation.

Feel free to ask questions if the problem description is not clear. You can use the Internet, but not for solutions to this problem. Please do this problem without the help of others.

My description of how this algorithm works:
In regards to the anagram problem - here is a brief description of how my algorithm works. Let n be the number of elements in the list, and m be the length of the words in the list. The algorithm avoids sorting the list (a costly nmlog(n): nlogn for mergesort * m for comparing strings), and rather creates a sort of unique hashing for which all anagrams will return identical values, but any words that are not anagrams will have different values. It does this by using the property of prime factorization. If we only multiply prime numbers, every distinct combination of primes leads to a distinct integer. Therefore we represent each letter A-Z as a prime from 2 to 101 (the 2nd through 27th primes, we ignore 1 because if A were 1 then any words with A would be identical to that word without the As). We then go through the list, and for each word, go through it and convert to a unique integer. We place this integer in a new list. This takes n*m time (n traversals through the large list, m traversals through each word). Then once we have the new list, we place each item in a Map from the identifier to the number of times we have seen that identifier. If it was already there exactly once, increment the anagram count by 2, one for the original and one for the new item. If it was there 0 times, put it there. If it was there more than once, increment the counter by one. This takes n time, because all of the Map functionality is constant time.

Therefore, this function is in O(n + nm) = O(nm). If the length of the list is much larger than the length of any of the words, we can even think of it as being linear time, or O(n).

NOTE: This was an actual interview question I received and solved on March 6, 2017.
