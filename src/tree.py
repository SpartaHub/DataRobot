class RootNode:
    __slots__ = ("_children", "word")

    def __init__(self):
        self.word = None
        self._children = {}

    def get_children(self, root_name):
        return self._children.get(root_name)

    def set_child(self, child_name, child):
        self._children[child_name] = child

    def get_word(self):
        return self.word

    def set_word(self, word):
        """
        Word should be set up only if the letter from which was created Node the last in the word
        :param str word: word from which was built all chain.
        """
        self.word = word


class Node(RootNode):

    def __init__(self, parent, letter):
        """
        :param RootNode or Node parent: Node or RootNode obj which created from previous letter
        :param str letter: letter from which creates Node
        """
        super().__init__()
        parent.set_child(letter, self)


class Tree:

    """
    roots it is first letters of all words which are stored in the 'words_file'.
    Tree creates from letters of the words from the 'words_file'.
    RootNode it is always first letter from the word and it has all possible children (Node-s)
    which create from the next letter.
    """

    __slots__ = ("root",)

    def __init__(self, words_file):
        """
        :param words_file: File with all words which will be used for building the Tree
        """
        self.root = RootNode()
        with open(words_file) as f:
            for word in f:
                root_letter = word[0]
                root_node = self.root.get_children(root_letter)
                if root_node is None:
                    root_node = RootNode()
                    self.root.set_child(root_letter, root_node)
                word = word.strip(" \n").lower()
                for letter in word[1:]:
                    next_node = root_node.get_children(letter)
                    if next_node is None:
                        next_node = Node(root_node, letter)
                    root_node = next_node
                root_node.set_word(word)
