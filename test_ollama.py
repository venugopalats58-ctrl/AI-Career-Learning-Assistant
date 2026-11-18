
import requests

url = "http://localhost:11434/api/generate"

data = {
    "model": "qwen2.5:3b",
    "prompt": "Explain Machine Learning in simple English.",
    "stream": False
}

response = requests.post(url, json=data, timeout=180)

if response.status_code == 200:
    result = response.json()
    print("\nAI RESPONSE:\n")
    print(result["response"])
else:
    print("Error:", response.text)
