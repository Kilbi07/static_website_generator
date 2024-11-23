from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, value: str, tag: str = None, props: dict = None) -> None:
        super().__init__(tag, value, props)
        self.tag = tag
        self.value = value
    def to_html(self) -> str:
        if not self.value:
            raise ValueError
        if not self.tag:
            return f"{self.value}"
        props_string = self.props_to_html()
        return f"<{self.tag}{props_string}>{self.value}</{self.tag}>"
