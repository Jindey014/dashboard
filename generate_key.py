import pickle
from pathlib import Path
import streamlit_authenticator as stauth

# User details
names = ["Jinish Shrestha", "Admin"]
usernames = ["jshrestha", "admin"]
passwords = ["test123", "admin"]

# Hash passwords using the new hash method
hasher = stauth.Hasher(passwords)
hashed_passwords = hasher.hash()

# Save the hashed passwords to a file
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)

print("Passwords hashed and saved successfully!")
