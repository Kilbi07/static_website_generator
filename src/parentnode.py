from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list, props: dict = None) -> None:
        super().__init__(tag, children, props = None)

    def to_html(self):
        if not self.tag:
            raise ValueError("No Tag found!")
        if not self.children:
            raise ValueError("NO Child found!")