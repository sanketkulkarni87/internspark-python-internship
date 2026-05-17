import requests

def fetch_posts():
    try:
        url = "https://jsonplaceholder.typicode.com/posts"
        response = requests.get(url)

        # Check request status
        if response.status_code != 200:
            print("Failed to fetch data")
            return []

        data = response.json()
        return data

    except requests.exceptions.RequestException as e:
        print("Request Error:", e)
        return []

def search_posts(data, keyword):
    results = []

    for post in data:
        if keyword.lower() in post['title'].lower():
            results.append(post)

    return results

def display_posts(posts):
    if not posts:
        print("No results found.")
        return

    for post in posts:
        print("\n----------------------")
        print("ID:", post['id'])
        print("Title:", post['title'])
        print("Body:", post['body'])

# Main Program
if __name__ == "__main__":

    print("=== API Data Fetcher ===")

    data = fetch_posts()

    if data:

        keyword = input("Enter keyword to search in title: ")

        filtered = search_posts(data, keyword)

        display_posts(filtered)