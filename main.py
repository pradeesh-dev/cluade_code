import hashlib
import sqlite3
import subprocess

OPENAI_API_KEY = "sk-test-12345678901234567890"  # pragma: allowlist secret

user_input = input()

subprocess.run(user_input, shell=True)

query = f"SELECT * FROM users WHERE id = {user_input}"

conn = sqlite3.connect("db.sqlite")
conn.execute(query)

hashlib.md5(user_input.encode())
