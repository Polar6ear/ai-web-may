# chains.py
import requests

def generate_pet_advice(prompt):
    expert_prompt = f"""
You are a highly skilled and experienced pet expert. Answer this user query in detail with logic, empathy, and useful tips.

Question: {prompt}

Answer:
""".strip()

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "tinyllama",
                "prompt": expert_prompt,
                "stream": False
            },
            timeout=60
        )
        data = response.json()
        return data.get("response", "No response from model.")
    except requests.exceptions.Timeout:
        return "Error: Timeout. Model is taking too long to respond."
    except Exception as e:
        return f"Error: {str(e)}"
