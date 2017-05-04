"""
Name: generate_ladder.py

Purpose: Find the shortest path for a word ladder from word A to word B
         e.g. FOOT -> FOOD -> GOOD -> GOLD -> BOLD -> BALD

Description: Given two four letter words as arguments, the program will
             output the shortest word ladder that can be made between
             the two words, if any ladder exists

Usage: Supply two 4 letter words as arguments in the command line,
       e.g. python generate_ladder.py BATH TUBS. Or call with no arguments to
       run through the examples
Author: Jack Hurst
"""

from common4s import words
import random
import sys
MAX_DEPTH = 8


def get_neighbours(word):
    """ Given a word, retun a list of words that are a single letter
        substitution away from it. For example GOLD and FOLD are a single
        substition away from each other.
        INPUT:
              - word: A string representing the word the we will find the
                      neighbours of
        OUTPUT:
               - ret: A list of words one substitution away from the
                      input word
    """
    word_set = set(words)
    ret = []
    assert(len(word) == 4)
    for n in range(0, 4):
        alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        alpha.remove(word[n])
        for letter in alpha:
            new_word = word[:n] + letter + word[n+1:]
            if new_word in word_set:
                ret.append(new_word)
    return ret


def crawl_tree(start_word, target, max_depth):
    """ Given a start word and a target word, build a pyramid-like
        structure of lists, starting with the start_word on it's own at
        the top, and with each successive layer being the list of words that
        are one substitution away from a word in the current list. Construction
        stops either when we reach a layer with the target word in, or when we
        reach the max_depth, in which case we stop and return None.
        INPUT:
                  - start_word: The start of the word ladder.
                  - target: The word we are aiming to reach
                  - max_depth: The number of layers at which we stop and give
                               up
        VARIABLES:
                  - word_groups: A dictionary containing the layers of words.
                                 Each key of the dict is an int in the range
                                 0 to max_depth. Each value is the list of
                                 words that are this many substitutions away
                                 from start_word
                  - word_group: The current list of words that is one
                                substitution away from a word in the previous
                                layer
        OUTPUT:
                  - If successful: A path or word linking start_word to target
                  - If unsuccessful: None
    """
    word_group = [start_word]
    word_groups = {}
    path = None
    for layer in range(0, max_depth):
        print "%d words %d away from %s" % (len(word_group),
                                            layer,
                                            start_word)
        word_groups[layer] = word_group
        new_words = []

        # Construct the next layer. Use the list(set(x)) method so any
        # duplicates are removed from the list
        for word in word_group:
            new_words.extend(get_neighbours(word))
        word_group = list(set(new_words))

        # Check to see if the target has been hit. It if has we can build the
        # path from what is in word_groups and return it. Otherwise, add
        # another layer of words
        if target in word_group:
            path = [target]
            node = target
            for path_idx in range(0, layer):
                neighbours = set(get_neighbours(node))
                nodes = neighbours.intersection(set(word_groups
                                                             [layer-path_idx]))
                # Choose any appropriate node. All will yield a path back to
                # the start, so we choose any to give us variety - If a path
                # is given as the output but it caontains words we don't like,
                # we can just run the program again to see if there are paths
                # which we do like
                node = random.choice(list(nodes))
                path = [node] + path
            path = [start_word] + path
            return path
    return path

if __name__ == "__main__":
    if len(sys.argv) > 1:
        pairs = [(sys.argv[1], sys.argv[2])]
    else:
        # Use example input if nothing is supplied in the command line
        pairs = [("WISH", "BONE"),
                 ("FISH", "CRAB"),
                 ("HEAD", "FOOT"),
                 ("BACK", "FLIP"),
                 ("NOSE", "EARS"),
                 ("BANK", "NOTE"),
                 ("BARN", "DOOR"),
                 ]
    for pair in pairs:
        start_word = pair[0]
        end_word = pair[1]
        path = crawl_tree(start_word, end_word, MAX_DEPTH)
        print path
