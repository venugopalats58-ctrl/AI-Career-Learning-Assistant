
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2.5:3b"


def generate_answer(question, context):

    if not context:
        return "I could not find relevant information in your uploaded documents."

    # Convert retrieved document chunks into text
    if isinstance(context, list):

        context_text = "\n\n".join(
            item["text"] if isinstance(item, dict) else str(item)
            for item in context
        )

    else:
        context_text = str(context)

    prompt = f"""
You are an AI Learning Assistant.

Answer the student's question using ONLY the
provided study material.

Instructions:
1. Explain in simple English.
2. Give clear and accurate answers.
3. Use examples when helpful.
4. Do not invent information.
5. If the answer is not available in the
   study material, clearly say so.

Study Material:
{context_text}

Question:
{question}

Answer:
"""

    try:

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.2,
                    "num_ctx": 4096
                }
            },
            timeout=180
        )

        response.raise_for_status()

        result = response.json()

        answer = result.get("response", "").strip()

        if not answer:
            return "The AI model returned an empty answer."

        return answer

    except requests.exceptions.ConnectionError:

        return (
            "Cannot connect to Ollama. "
            "Please make sure Ollama is running."
        )

    except requests.exceptions.Timeout:

        return (
            "The AI model is taking too long. "
            "Please try again."
        )

    except requests.exceptions.RequestException as error:

        return f"Local AI model error: {error}"
