from googleapiclient.discovery import build
from google.oauth2 import service_account
import re

# Define the scope for reading Google Docs
SCOPES = ['https://www.googleapis.com/auth/documents.readonly']


# Function to extract content from a Google Doc using the Google Docs API
def get_google_doc_content(url):
    # Extract the document ID from the URL
    document_id = url.split('/d/')[1].split('/')[0]

    # Authenticate using the service account credentials
    credentials = service_account.Credentials.from_service_account_file(
        'path_to_your_credentials.json', scopes=SCOPES)

    # Build the Docs API service
    service = build('docs', 'v1', credentials=credentials)

    # Get the content of the document
    document = service.documents().get(documentId=document_id).execute()

    # Extract and return the text from the document body
    doc_content = ""
    for element in document.get('body').get('content'):
        if 'paragraph' in element:
            for text_run in element.get('paragraph').get('elements'):
                if 'textRun' in text_run:
                    doc_content += text_run['textRun']['content']
    return doc_content


# Function to parse the document content and print the grid
def parse_and_print_grid(doc_content):
    # Regular expression to extract characters and coordinates
    pattern = r"(\S)\s+(\d+),\s*(\d+)"
    matches = re.findall(pattern, doc_content)

    if not matches:
        print("No valid data found in the document.")
        return

    # Find the maximum x and y coordinates to determine the grid size
    max_x = max(int(match[1]) for match in matches)
    max_y = max(int(match[2]) for match in matches)

    # Initialize an empty grid filled with spaces
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # Place the characters in their specified positions
    for char, x, y in matches:
        grid[int(y)][int(x)] = char

    # Print the grid row by row
    for row in grid:
        print(''.join(row))


# Main function to fetch the Google Doc and display the secret message
def print_unicode_grid_from_doc(url):
    # Retrieve the document content from the given URL
    doc_content = get_google_doc_content(url)

    # Parse and print the grid
    parse_and_print_grid(doc_content)


# Example usage
doc_url = 'https://docs.google.com/document/d/YOUR_DOCUMENT_ID/edit'
print_unicode_grid_from_doc(doc_url)
