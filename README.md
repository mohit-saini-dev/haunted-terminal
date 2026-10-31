```markdown
# 👻 Haunted Terminal

> A spooky, local AI CLI tool that possesses your terminal and gives sarcastic commentary on your shell commands using Ollama.

Built for the **Hacktoberfest 2026 Week 4: Ghost in the Machine** challenge.

---

## 🎃 Features
- **Local AI Inference:** Powered completely offline by [Ollama](https://ollama.com) running open-weight models (`qwen2.5-coder:7b`).
- **Terminal Possession:** Intercepts commands, error logs, and git snippets, turning boring terminal outputs into an eerie experience.
- **Zero Heavy Dependencies:** Built with pure Python standard libraries (`urllib`, `json`, `sys`).

---

## 🛠️ Installation & Setup

1. Make sure **Ollama** is installed and running locally on your machine:
   ```bash
   ollama run qwen2.5-coder:7b

```

2. Clone the repository:
```bash
git clone [https://github.com/mohit-saini-dev/haunted-terminal.git](https://github.com/mohit-saini-dev/haunted-terminal.git)
cd haunted-terminal

```


3. Run the tool with any command or error:
```bash
python haunted_terminal.py "rm -rf node_modules"

```



---

## 🛡️ Why Open Innovation Matters

By running locally via Ollama, your terminal inputs and code snippets remain entirely private on your machine—ensuring complete offline capability, zero cloud API costs, and absolute data ownership.

```

<FollowUp label="Ready for the DEV.to submission post markdown?" query="Give me the clean raw markdown for the DEV.to submission post now."/>

```
