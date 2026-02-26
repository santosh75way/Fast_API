import requests
import json

BASE_URL = "http://127.0.0.1:8000/users"

def test_routes():
    with open("results.txt", "w") as f:
        f.write("--- 1. Testing POST /users/ (Create User) ---\n")
        new_user = {"username": "testuser", "email": "test@example.com", "password": "password123", "is_active": True}
        res = requests.post(BASE_URL + "/", json=new_user)
        f.write(f"Status: {res.status_code}, Response: {res.text}\n\n")
        
        if res.status_code != 201:
            f.write("Failed to create user. Exiting tests.\n")
            return
            
        user_id = res.json()["id"]

        f.write("--- 2. Testing GET /users/ (Get all users) ---\n")
        res = requests.get(BASE_URL + "/")
        f.write(f"Status: {res.status_code}, Response: {res.text}\n\n")

        f.write(f"--- 3. Testing GET /users/{user_id} (Get single user) ---\n")
        res = requests.get(f"{BASE_URL}/{user_id}")
        f.write(f"Status: {res.status_code}, Response: {res.text}\n\n")

        f.write(f"--- 4. Testing PATCH /users/{user_id} (Update user) ---\n")
        update_data = {"is_active": False}
        res = requests.patch(f"{BASE_URL}/{user_id}", json=update_data)
        f.write(f"Status: {res.status_code}, Response: {res.text}\n\n")
        
        f.write(f"--- 5. Testing DELETE /users/{user_id} (Delete user) ---\n")
        res = requests.delete(f"{BASE_URL}/{user_id}")
        f.write(f"Status: {res.status_code}, Response: {res.text}\n\n")

        f.write(f"--- 6. Verify Deletion GET /users/{user_id} ---\n")
        res = requests.get(f"{BASE_URL}/{user_id}")
        f.write(f"Status: {res.status_code}, Response: {res.text}\n\n")

if __name__ == "__main__":
    test_routes()
