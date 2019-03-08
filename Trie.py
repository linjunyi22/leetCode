"""
Implement a trie with insert, search, and startsWith methods.

实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。

示例:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");   
trie.search("app");     // 返回 true

说明:

1.你可以假设所有的输入都是由小写字母 a-z 构成的。
2.保证所有输入均为非空字符串。
"""


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.end_of_word = "##" # 用于标志一个单词是否结束

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        # 遍历单词，将每个字母按层级结构存进字典中，如果不存在该字母，则开辟一个空字典
        # 例如：{'t': {'e': {'s': {'t': {}}}}}

        for one in word:
            node = node.setdefault(one,{})
        node[self.end_of_word] = self.end_of_word

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        # 遍历单词，判断每个字母能够在字典树中找到，如果找不到，返回 False，如果找到且最后为结束标志符，则返回 True
        for one in word:
            if one not in node:
                return False
            node = node[one]
        return self.end_of_word in node
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        # 遍历前缀，判断每个字母是否在字典树中，如果不在，立即返回 False，否则，遍历完成后，返回 True。
        node = self.root
        for one in prefix:
            if one not in node:
                return False
            node = node[one]
        return True
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
