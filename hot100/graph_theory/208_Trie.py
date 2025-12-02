# 实现Trie 前缀树
# 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补全和拼写检查。
# 前缀树的核心思想是用空间换时间，利用字符串的公共前缀来降低查询时间的复杂度。

class TrieNode:
    # 节点
    def __init__(self):
        # 子节点字典，key是字符，value是TrieNode
        self.children = {}
        # 标记从根到当前节点是否构成一个完整的单词
        self.is_end_of_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode() 

    def insert(self, word: str) -> None:
        '''
        插入单词
        '''
        curr = self.root

        for char in word:
            if char not in curr.children: # 检查的是所有子节点key
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end_of_word=True
        

    def search(self, word: str) -> bool:
        '''
        搜索单词
        '''
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        '''
        检查是否存在前缀
        '''
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr= curr.children[char]
        return True



def test():
    # Your Trie object will be instantiated and called as such:
    trie = Trie()
    trie.insert("apple")
    print(f"Search 'apple': {trie.search('apple')}")   # 返回 True
    print(f"Search 'app': {trie.search('app')}")     # 返回 False
    print(f"StartsWith 'app': {trie.startsWith('app')}") # 返回 True
    trie.insert("app")
    print(f"Search 'app' after insert: {trie.search('app')}")   # 返回 True

if __name__ == '__main__':
    test()