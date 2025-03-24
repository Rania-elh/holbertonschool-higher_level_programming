#!/usr/bin/python3
import os

def generate_invitations(template, attendees):
    """
    Generates invitation files based on a template and list of attendees.

    Parameters:
    - template (str): The invitation template as a string.
    - attendees (list of dict): A list of dictionaries with attendee details. Each
      dictionary should contain 'name', 'event_title', 'event_date', and 'event_location'.
    """
    if not isinstance(template, str):
        print("Error: Template should be a string.")
        return
    
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return
    
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    for index, attendee in enumerate(attendees, start=1):
        output_content = template
        output_content = output_content.replace("{name}", str(attendee.get("name", "N/A")))
        output_content = output_content.replace("{event_title}", str(attendee.get("event_title", "N/A")))
        output_content = output_content.replace("{event_date}", str(attendee.get("event_date", "N/A")))
        output_content = output_content.replace("{event_location}", str(attendee.get("event_location", "N/A")))

        file_name = f"output_{index}.txt"

        try:
            with open(file_name, "w") as file:
                file.write(output_content)
            print(f"Generated {file_name}")
        except Exception as e:
            print(f"Error writing file {file_name}: {e}")
        
