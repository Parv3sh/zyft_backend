"""Main module."""
import html_to_xpath
import data_set_creation
import tag_model_number


class ZyftBackend:
    def __init__(self, html, path, model_tupple):
        self.html = html
        self.path = path
        self.model_tupple = model_tupple
        self.html_to_xpath = html_to_xpath.HtmlToXpath(self.html)
        self.data_set_creation = data_set_creation.DataSetCreation(self.path)
        self.tag_model_number = tag_model_number.Feature(self.model_tupple)

    def generate_xpath_query(self, zyft_node_id):
        return self.html_to_xpath.generate_xpath_query(zyft_node_id)

    def get_data_set(self):
        return self.data_set_creation.transform()

    def tag_html(self, html_to_tag):
        return self.tag_model_number.tag_html(html_to_tag)


if __name__ == "__main__":
    html = """
    <ul id='favouriteThings' class='myList' zyft_node_id='123456'> <li id='item1'> Thing 1</li>
    <li id='item2'> Thing 2</li>
    <li id='item3'> Thing 3</li>
    </ul>
    """
    path = "zyft_backend/data/data_analysis_test_data (2).csv"
    model_tupple = (
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
    html_to_tag = "<html> <body> ABC HU6630B XYZ HU6630B </body><html>"
    zyft_backend = ZyftBackend(html, path, model_tupple)
    print("*" * 80)
    print("HTML to XPATH")
    print("*" * 80)
    print(zyft_backend.generate_xpath_query("123456"))
    print("*" * 80)
    print("Data Set Creation")
    print("*" * 80)
    print(zyft_backend.get_data_set())
    print("*" * 80)
    print("Tag Model Number")
    print("*" * 80)
    print(zyft_backend.tag_html(html_to_tag))
