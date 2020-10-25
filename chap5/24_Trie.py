class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.node = {}  # 初始化前缀树结构

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        root = self.node  # 前缀树总的头节点
        for char in word:  # 依次遍历字符串的每个单个字符
            # 当前字符在前缀树没有对应头节点，则新建对应头节点
            if char not in root:
                root[char] = {}

            # 无论原前缀树是否存在该字符的头节点，经过上一步操作后必定存在对应的头节点
            # 移动前缀树的节点
            root = root[char]
        # 字符串已经被遍历结束
        root["end"] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """

        root = self.node  # 前缀树总的头节点
        for char in word:  # 依次遍历字符串的每个单个字符
            # 当前字符在前缀树没有对应头节点，则必定不存在该字符串
            if char not in root:
                return False

            # 移动前缀树的节点
            root = root[char]

        # 字符串已经被遍历结束后，再来判断是否已经到达路径的尾部
        if "end" in root:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        root = self.node  # 前缀树总的头节点
        for char in prefix:  # 依次遍历字符串的每个单个字符
            # 当前字符在前缀树没有对应头节点，则必定不存在该字符串
            if char not in root:
                return False

            # 移动前缀树的节点
            root = root[char]
        # 字符串已经被遍历结束,都能在前缀树中找到对应的节点
        # 则证明前缀树中存在以该字符串为首的路径
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)