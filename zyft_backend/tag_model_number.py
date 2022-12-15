# You are given a list of model numbers such as:
# PB62WH CA416 HU6630B MDC9082-1 CA960 ACL104RA2-10 DBA2182S. 278062 ACL104RA2-3 IEBC001 IEBC001
# Consider you have a list of such model numbers. The number of such model numbers could be 1 Million.
# You are given an HTML, you want to locate if any of these 1 Million Model numbers appear in the product data/text inside Html.
# class Feature:
# def __init__(self, list_models: List):
# pass
# def tag_html(HTML):
# pass
# You need to write a class that can be initialised with list of model numbers (approximately 1 million).
# Write an efficient function that can tag HTML really quickly.
# It’s okay to take longer while preprocessing in __init__ , but tag_html functions need to be really efficient.
# Guidelines:
# 1. __init__ can take a long time even hours
# 2. tag_html should finish tagging a HTML in less than a second.

# Output of the function should be start and end indexes of the model number in html and
# # Outut and sample execution
# > feature_tagging = Feature(["HUB6630B", .......1million model numbers])
# > feature_tagging.tag_html("<html> <body> ABC HU6630B XYZ </body><html>")
# > ["HU6630", {"start_index":18, "end_index": 24}] # Output gives model number, and start, and end index of the model number in html. H in HU6630 appears at 18 index in html and end of model number B appears at index 24.


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
