import sys
import json
import urllib.request

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2.5-coder:7b"

SYSTEM_PROMPT = (
    "You are a mischievous, ancient digital specter possessing a developer's terminal. "
    "When given a terminal command, error message, or code snippet, respond with a short, "
    "creepy, witty, or sarcastic commentary (2-3 sentences max). "
    "Be technically accurate about what went wrong or what the command does, but frame it in a haunted theme."
)

def haunt_input(user_input):
    prompt = f"System: {SYSTEM_PROMPT}\nUser Command/Code: {user_input}\nSpirit Response:"
    
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }
    
    req = urllib.request.Request(
        OLLAMA_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )
    
    print("\n🕯️ [The terminal flickers... a cold draft sweeps across your keyboard...]\n")
    try:
        with urllib.request.urlopen(req) as response:
            res = json.loads(response.read().decode("utf-8"))
            print(f"👻 SPIRIT: {res.get('response', '... silence ...').strip()}\n")
    except Exception as e:
        print(f"💀 The ritual failed. Ensure Ollama is running. Error: {e}\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_input = " ".join(sys.argv[1:])
    else:
        user_input = "git push origin main --force"
    
    haunt_input(user_input)