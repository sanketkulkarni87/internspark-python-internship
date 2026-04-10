import requests

class JokeAPI:
    def __init__(self):
        self.apis = [
            'https://official-joke-api.appspot.com/random_joke',
            'https://v2.jokeapi.dev/joke/Any',
        ]

    def fetch_joke(self):
        for api in self.apis:
            response = requests.get(api)
            if response.status_code == 200:
                return response.json()
        return None
    
    def get_joke(self):
        joke = self.fetch_joke()
        if joke:
            if 'setup' in joke and 'punchline' in joke:
                return f"{joke['setup']} - {joke['punchline']}"
            return joke['joke']
        return "No joke found!"
