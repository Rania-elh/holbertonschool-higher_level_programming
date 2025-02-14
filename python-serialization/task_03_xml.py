#!/usr/bin/env python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serializes a dictionary to an XML file.
    :param dictionary: Dictionary to serialize
    :param filename: Name of the output XML file
    """
    try:
        root = ET.Element("data")

        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)
    except Exception as e:
        print(f"Serialization failed: {e}")

def deserialize_from_xml(filename):
    """
    Deserializes an XML file into a dictionary.
    :param filename: Name of the input XML file
    :return: Dictionary containing the XML data
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        return {child.tag: child.text for child in root}
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return None
    except Exception as e:
        print(f"Deserialization failed: {e}")
        return None

