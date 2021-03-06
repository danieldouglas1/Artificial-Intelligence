import sys
# Author: Prof. Fitzsimmons
# Date: Fall 2020
# Filename: words.py
#
# Description: Implementation of a search algorithm to find a
# shortest path of words from a given start word to a given
# goal word. At each step, any single letter in the word
# can be changed to any other letter, provided
# that the resulting word is also in the dictionary.
#
# A dictionary of English words a text file, a start word,
# and a goal word are passed as command line arguments.
#
# Usage: python3 words.py dictionaryFile startWord endWord

# Python queue implementation (https://docs.python.org/3.5/library/collections.html?highlight=deque#collections.deque)
from collections import deque

#   Usage of deque:
#   q = deque()   # declare new deque
#   q.append('A') # append A to the rear of the queue.
#   q.popleft()   # pop from the front of the queue.

class Node:
    def __init__(self, state, parent):
        self.state = state
        self.parent = parent

    # Nodes with the same state are viewed as equal
    def __eq__(self, other_node):
        return isinstance(other_node, Node) and self.state == other_node.state

    # Nodes with the same state hash to the same value
    # (e.g., when storing them in a set or dictionary)
    def __hash__(self):
        return hash(self.state)

def read_file(filename):
    """Read in each word from a dictionary where each
    word is listed on a single line."""
    print("Reading dictionary: " +filename)
    word_dict = set()

    dictionary = open(filename)

    # Read each word from the dictionary
    for word in dictionary:
        # Remove the trailing newline character
        word = word.rstrip('\n')

        # Convert to lowercase
        word = word.lower()

        word_dict.add(word)

    dictionary.close()

    return word_dict

def find_path(startWord, goalWord, word_dict):
    """Returns a list of words in word_dict
    that form the shortest path from startWord to goalWord,
    and returns None if no such path exists."""

    # We can't return anything if our goalWord is not in the dictionary
    if goalWord not in word_dict:
        return []

    # Add initial elementto the queue with itself as its parent
    q = deque()
    q.append(Node(startWord,startWord))

    # Declare a endNode to store our goalWord
    endNode = Node(" "," ")

    # Boolean flag to break loops when we are finished
    done = False

    #DFS
    while q:
        size = len(q)
        #select each element at the current level
        for x in range(size):
            curr = q.popleft()
            #try diffent combinations
            for i in range(len(curr.state)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    new_word = curr.state[:i] + c + curr.state[i+1:]
                    # Break if we have found our goalWord
                    if new_word == goalWord:
                        endNode = Node(state=new_word,parent=curr)
                        done = True
                        break
                    # Add current combination to queue, and remove from dictionary
                    # to prevent looping
                    if new_word in word_dict:
                        q.append(Node(state=new_word,parent=curr))
                        word_dict.remove(new_word)

                if done: break
            if done: break
        if done: break

    ans = []
    currNode = endNode
    # Access the parentNode until we find the startWord
    while currNode.state is not startWord:
        ans.append(currNode.state)
        currNode = currNode.parent
    ans.append(startWord)
    ans.reverse()
    return ans


def main():
    if len(sys.argv) != 4:
        print("Usage: python3 words.py dictionaryFile startWord goalWord")
    else:
        dictionaryFile = sys.argv[1]
        startWord = sys.argv[2]
        goalWord = sys.argv[3]

        word_dict = set()
        word_dict = read_file(dictionaryFile)

        if startWord not in word_dict:
            print(startWord + " is not in the given dictionary.")
        else:
            print("-- Shortest path from " + startWord + " to " + goalWord + " --")

            solution = find_path(startWord, goalWord, word_dict)

            if(solution is None):
                print("None exists!")
            else:
                for word in solution:
                    print(word)

if __name__ == "__main__":
    main()
