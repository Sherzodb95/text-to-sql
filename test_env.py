from dotenv import load_dotenv
import os

# Force load the .env file
result = load_dotenv(dotenv_path="E:/Projects/text-to-sql/.env")
print(f"🔍 DEBUG: Loaded .env file: {result}")  # True if successfully loaded

# List all environment variables for debugging
print("🔍 DEBUG: Environment Variables:")
for key, value in os.environ.items():
    print(f"{key}: {value}")

# Retrieve and print the specific API key
api_key = os.getenv('GOOGLE_API_KEY')
print(f"🔍 DEBUG: GOOGLE_API_KEY: {api_key}")

if not api_key:
    print("❌ API key not found. Ensure it's correctly set in the .env file.")
