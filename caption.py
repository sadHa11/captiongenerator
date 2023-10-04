


import requests
from bs4 import BeautifulSoup
import random

def get_captions_from_search(word, num_captions=5):
    captions = []

    # Replace spaces with plus signs for the search query
    query = word.replace(" ", "+")

    # Perform a search using a search engine (Google in this case)
    search_url = f"https://www.google.com/search?q={query}"
    response = requests.get(search_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        # Find relevant elements that might contain captions
        caption_elements = soup.find_all("div", class_="BNeawe s3v9rd AP7Wnd")
        
        for element in caption_elements:
            caption = element.get_text()
            if caption:
                captions.append(caption)

    return random.sample(captions, min(num_captions, len(captions)))

# Input word
input_word = input("Enter a word: ")

# Get captions from the internet search
captions = get_captions_from_search(input_word)

# Display the captions
print("\nGenerated Captions:")
for index, caption in enumerate(captions, start=1):
    print(f"{index}. {caption}")
