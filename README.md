# JSAI OS

JSAI OS is an experimental AI-native operating system built on Linux that I'm building as my first real project, where an AI assistant helps manage tasks, files, and workflows through a set of defined tools rather than acting as a free-roaming agent. My goal is to learn Python, system design, and security fundamentals hands-on by integrating AI into the operating system while maintaining a secure permission model that prevents AI from having unrestricted control over the system, and then use JSAI OS as my own test target, building future projects that probe it with the cybersecurity concepts I'm studying for Security+. I chose a controlled-tool approach over giving the AI unrestricted shell access because it applies least privilege from day one: every action the AI can take is explicit and scoped, with the architecture designed to support logging and auditing in future updates, which shrinks the attack surface and makes risks much easier to contain. Coming from training dogs, it's a familiar idea to me: you don't hand over full freedom until you've built structure, boundaries, and trust, one step at a time.

## Running the tests

From the repo root, with the project's `.venv`:

```bash
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python -m pytest -v
```
