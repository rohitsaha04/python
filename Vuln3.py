import requests
import json

class UserManager:
    def __init__(self):
        self.users = []  # Stores users in memory (not ideal for large applications)

    def add_user(self, username, password):
        # Code smell: Password is stored in plain text
        self.users.append({"username": username, "password": password})

    def get_user(self, username):
        # Code smell: Inefficient way to find a user (could be optimized)
        for user in self.users:
            if user["username"] == username:
                return user
        return None

def fetch_data_from_url(url):
    # Code smell: Not handling exceptions, could crash on network errors
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return None

def process_data(data):
    # Code smell: Not checking if data is None or empty
    if data["name"] == "Alice":  # Risk of KeyError if "name" is not in data
        print("Found Alice!")

def insecure_logging(password):
    # Vulnerability: Logging sensitive information (password) in plain text
    print(f"User password: {password}")

if __name__ == "__main__":
    manager = UserManager()
    manager.add_user("Alice", "password123")
    user = manager.get_user("Alice")

    data = fetch_data_from_url("https://api.example.com/data")
    if data:
        process_data(data)

    insecure_logging("password123")
