"""
208. Implement Trie (Prefix Tree) 实现 Trie (前缀树)

实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。

示例:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");
trie.search("app");     // 返回 true
说明:

你可以假设所有的输入都是由小写字母 a-z 构成的。
保证所有输入均为非空字符串。
"""
# 前缀树结构
# 第一种是树结构存储单词 a -> p -> p
# 第二种是字典存储单词 {a : {p : { p } } }


class Trie(object):
    class TrieNode(object):
        def __init__(self):
            self.is_word = False
            self.children = [None] * 26

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Trie.TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        p = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not p.children[index]:
                p.children[index] = Trie.TrieNode()
            p = p.children[index]
        p.is_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.find(word)
        return node is not None and node.is_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return self.find(prefix) is not None

    def find(self, prefix):
        p = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if not p.children[index]:
                return None
            p = p.children[index]
        return p

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


class Trie_2(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        p = self.root
        for c in word:
            if c not in p:
                p[c] = {}
            p = p[c]
        p["#"] = True       # 连续嵌套结构, 并在word末尾即叶子结点用"#"标记

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.find(word)
        return node is not None and "#" in node

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return self.find(prefix) is not None

    def find(self, prefix):
        p = self.root
        for c in prefix:
            if c not in p: return None
            p = p[c]                    # 结合insert可看出是连续嵌套字典结构
        return p
