class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_node = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        root = self.root
        for symbol in word:
            dict_to_search = root.children
            if symbol not in dict_to_search:
                dict_to_search[symbol] = TrieNode()
            root.children = dict_to_search
            root = root.children[symbol]
        root.end_node = 1


class Solution:
    def findWords(self, board, words):
        self.num_words = len(words)
        res, trie = [], Trie()
        for word in words:
            trie.insert(word)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, trie.root, i, j, '')
