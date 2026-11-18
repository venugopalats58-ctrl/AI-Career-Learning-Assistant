
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2.5:3b"


def generate_interview_question(role, difficulty):

    prompt = f"""
You are an experienced technical interviewer.

Generate ONE technical interview question.

Job Role: {role}
Difficulty: {difficulty}

Instructions:
1. Ask a relevant technical question.
2. Match the selected difficulty.
3. Focus on real-world technical knowledge.
4. Do not provide the answer.
5. Return only the question.
"""

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.7
                }
            },
            timeout=180
        )

        response.raise_for_status()

        result = response.json()

        return result.get(
            "response",
            "No question generated."
        ).strip()

    except requests.exceptions.ConnectionError:
        return "Error: Ollama is not running."

    except requests.exceptions.Timeout:
        return "Error: Question generation timed out."

    except requests.exceptions.RequestException as error:
        return f"Generation error: {error}"
