# Liste d'invites
attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]

# Lire le fichier 
with open('template.txt', 'r') as file:
    template_content = file.read()

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error, this is not a string")
        return

    if not isinstance(attendees, list):
        print("Error : The attendees should be a list")
        return
    
    for a in attendees:
        if not isinstance(a, dict):
            print("Error: An attendees is not a dictionnary")
            return
        
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print('No data provided, no output files generated.')
        return
    
    for i, attendee in enumerate(attendees, 1):
        invitation = template
        invitation = invitation.replace("{name}", attendee.get("name", "N/A"))
        invitation = invitation.replace("{event_title}", attendee.get("event", "N/A"))
        invitation = invitation.replace("{event_date}", attendee.get("event_date", "N/A") if attendee.get("event_date") else "N/A")
        invitation = invitation.replace("{event_location}", attendee.get("event_location", "N/A"))

        filename = f"output_{i}.txt"

        with open(filename, 'w') as file:
            file.write(invitation)
        
        print(f"Fichier généré : {filename}")
