import requests
from bs4 import BeautifulSoup

# Specify the URL of the Wikipedia page you want to scrape
url = "https://monsterhunter.fandom.com/wiki/MH1:_Lance_Weapon_Tree"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Find the element containing the content you want
# In this example, we'll extract the main content of the article
content_div = soup.find(id='content')

# Extract the text from the content element
content_text = content_div.get_text()

# Print the content
print(content_text)