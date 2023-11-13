import requests

def get_random_quote():
    response = requests.get("https://api.quotable.io/random")
    quote_data = response.json()
    return quote_data["content"], quote_data["author"]

quote, author = get_random_quote()
print(f"Random Quote: '{quote}' - {author}")
