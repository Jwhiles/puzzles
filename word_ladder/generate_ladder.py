from common4s import words
import random
import sys
word_set = set(words)
def get_neighbours(word):
    ret = []
    if len(word)!=4:
        import pdb;pdb.set_trace()
    assert(len(word)==4)
    for n in range(0,4):
        alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        alpha.remove(word[n])
        for letter in alpha:
            new_word = word[:n] + letter + word[n+1:]
            if new_word in word_set:
                ret.append(new_word)
    return ret
def crawl_tree(start_word,target,max_depth):
    word_group = [start_word]
    word_groups = {}
    for n in range(0,max_depth):
        print "%d words %d away from %s" % (len(word_group),n,start_word)
        word_groups[n] = word_group
        new_words = []
        for word in word_group:
            new_words.extend(get_neighbours(word))
        word_group = list(set(new_words))
        if target in word_group:
            path = [target]
            node = target
            for m in range(0,n):
                neighbours = set(get_neighbours(node))
                nodes = neighbours.intersection(set(word_groups[n-m]))
                node = random.choice(list(nodes))
                path = [node] + path
            path = [start_word] + path
            return path
    return None
if len(sys.argv)>1:
    pairs = [(sys.argv[1],sys.argv[2])]
else:
    pairs = [("WISH","BONE"),
         ("FISH", "CRAB"),
         ("HEAD", "FOOT"),
         ("BACK","FLIP"),
         ("NOSE","EARS"),
         ("BANK","NOTE"),
         ("LAVA","FIRE"),
         ("BEAK","WING"),
         ("BARN","DOOR"),
        ]
for pair in pairs:
    r = crawl_tree(pair[0],pair[1],9)
    print r

