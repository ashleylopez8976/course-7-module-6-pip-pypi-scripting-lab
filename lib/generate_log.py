from datetime import datetime

import requests


def generate_log(data):
    # Validate the input.
    if not isinstance(data, list):
        raise ValueError("data must be a list")

    # Create a filename using today's date.
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # Write each entry on its own line.
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # Display confirmation and return the filename.
    print(f"Log written to {filename}")
    return filename

def fetch_data():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1",
        timeout=10
    )
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    try:
        post = fetch_data()
        generate_log([
            "User logged in",
            "User updated profile",
            "Report exported",
            f"Fetched Post Title: {post.get('title', 'No title found')}"
        ])
    except requests.RequestException as error:
        print(f"Unable to fetch data: {error}")