class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True


class Feature:
    def __init__(self, list_models):
        self.trie = Trie()
        for model in list_models:
            self.trie.insert(model)

    def tag_html(self, html):
        result = []
        for i, char in enumerate(html):
            if char in self.trie.root.children:
                j = i
                node = self.trie.root
                while j < len(html) and html[j] in node.children:
                    node = node.children[html[j]]
                    if node.isEnd:
                        result.append(
                            [html[i : j + 1], {"start_index": i, "end_index": j}]
                        )
                    j += 1
        return result


if __name__ == "__main__":
    feature_tagging = Feature(
        (
            "HUB6630B",
            "CA416",
            "HU6630B",
            "MDC9082-1",
            "CA960",
            "ACL104RA2-10",
            "DBA2182S",
            "278062",
            "ACL104RA2-3",
            "IEBC001",
            "XYZ",
        )
    )
    print(
        feature_tagging.tag_html("<html> <body> ABC HU6630B XYZ HU6630B </body><html>")
    )

# Explanation:
# We use a trie to store all the model numbers. Then we iterate through the html string and check if the current character is in the trie. If it is, we keep going until we find a model number or we reach the end of the html string. If we find a model number, we add it to the result.

# Note: This solution assumes that the model numbers are not substrings of each other. If they are, we would need to add a check to make sure that the model number is not a substring of another model number.
