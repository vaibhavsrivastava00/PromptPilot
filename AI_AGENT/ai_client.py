import requests
from config import API_KEY, API_URL

def get_plan_for_task(task_description: str) -> str:
    prompt = f"""
You are an AI agent that generates a sequence of shell commands to accomplish the following task:
Task: {task_description}
Provide a step-by-step plan as bullet points with each command in backticks (``).
"""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 150,
        "temperature": 0.3
    }
    try:
        response = requests.post(API_URL, headers=headers, json=data, timeout=30)
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content'].strip()
        else:
            return f"Error generating plan: {response.status_code} {response.text}"
    except Exception as e:
        return f"Error generating plan: {e}"

def refine_plan(task_description: str, error_message: str) -> str:
    prompt = f"""
You are an AI agent tasked with refining a shell command sequence. A previous attempt failed with the following error:
Error: {error_message}
Task: {task_description}
Generate a revised plan with step-by-step bullet points. Each shell command should be in backticks (``).
"""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 150,
        "temperature": 0.3
    }
    try:
        response = requests.post(API_URL, headers=headers, json=data, timeout=30)
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content'].strip()
        else:
            return f"Error refining plan: {response.status_code} {response.text}"
    except Exception as e:
        return f"Error refining plan: {e}"
