from bs4 import BeautifulSoup


class HtmlToXpath:
    def __init__(self, html):
        self.html = html
        self.soup = BeautifulSoup(html, "html.parser")

    def get_all_xpath_queries(self):
        elements = self.soup.find_all(attrs={"zyft_node_id": True})
        xpath_queries = []
        for element in elements:
            xpath_queries.append(self.get_xpath_query(element))
        return xpath_queries

    def get_xpath_query(self, element):
        zyft_node_id = element["zyft_node_id"]
        parent_element = element.parent
        index = self.get_index(element)
        tag_name = element.name
        xpath_query = f"//{tag_name}[{index}]"
        if zyft_node_id in parent_element.attrs:
            parent_xpath_query = self.get_xpath_query(parent_element)
            xpath_query = parent_xpath_query + xpath_query
        return xpath_query

    def get_xpath_with_attributes_syntax(self, element):
        tag_name = element.name
        attributes = element.attrs
        xpath_query = f"//{tag_name}"
        for attribute in attributes:
            xpath_query += f'[@{attribute}="{attributes[attribute]}"]'
        return xpath_query

    def get_index(self, element):
        parent_element = element.parent
        children_elements = parent_element.find_all(element.name)
        index = children_elements.index(element) + 1
        return index

    def generate_xpath_query(self, zyft_node_id):
        element = self.soup.find(attrs={"zyft_node_id": zyft_node_id})
        return self.get_xpath_query(element), self.get_xpath_with_attributes_syntax(
            element
        )


if __name__ == "__main__":
    html = """
    <ul id='favouriteThings' class='myList' zyft_node_id='123456'> <li id='item1'> Thing 1</li>
    <li id='item2'> Thing 2</li>
    <li id='item3'> Thing 3</li>
    </ul>
    """
    html_to_xpath = HtmlToXpath(html)
    print(html_to_xpath.generate_xpath_query("123456"))
