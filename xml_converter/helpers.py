from typing import List
from xml.etree import ElementTree as ET


class XMLConverter:
    def __init__(self, file_instance) -> None:
        self.file_instance = file_instance

    def to_json(self):
        root = ET.ElementTree(ET.fromstring(self.file_instance)).getroot()
        response_data = {}

        if root is not None:
            response_data["Root"] = []

            children = list(root)

            if not children:
                response_data["Root"] = ""

            for child in children:
                self.handle_child_elements(child, response_data["Root"])

        return response_data

    def handle_child_elements(self, element, response_data: List):
        data = []

        for child in element:
            if list(child):
                self.handle_child_elements(child, data)
            else:
                data.append({f"{child.tag}": child.text})

        response_data.append({f"{element.tag}": data})
