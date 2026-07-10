# FL-05: Agent Concepts and MCP Basics

## 1. Workflow vs. Agent
The term "Agent" is heavily abused in AI marketing to describe simple automated tasks. Based on Anthropic's "Building Effective Agents," the distinction comes down to autonomy and path-finding. 

A **Workflow** is a deterministic, LLM-orchestrated pipeline where the steps are hardcoded by a human. For example, my FL-04 Literature Review pipeline is a **Workflow** (specifically, a *Prompt Chaining* workflow). I define exactly what happens: Step 1 is Gather, Step 2 is Synthesize, Step 3 is Draft. The AI does not decide *how* to accomplish the goal; it just executes the predefined steps on the data I feed it.

An **Agent**, conversely, is a system where the LLM is given a high-level goal and has the autonomy to dynamically choose which tools to use and what path to take. If it hits an error, it decides how to recover. 

### Upgrading FL-04 to an Agent
To turn my FL-04 workflow into a true agent, I would stop feeding it raw notes manually. Instead, I would give it a goal: *"Draft a literature review on Federated Learning in Medical Imaging."* The agent would autonomously use a Web Search tool to find papers, a PDF Parsing tool to read them, evaluate whether it has enough data, and then draft the review.

## 2. Model Context Protocol (MCP)
MCP (Model Context Protocol) is essentially a universal "USB-C port" for AI. Historically, if I wanted an LLM to read my local codebase or query my database, I had to write custom API wrappers for every single data source. MCP standardizes this. It provides three primitives:
- **Prompts:** Pre-defined instruction templates.
- **Resources:** Static data the AI can read (like local files).
- **Tools:** Executable functions the AI can trigger (like running terminal commands).

## 3. Proof of MCP Execution
*(Note for Reviewer: See the attached screenshots in my submission showing Claude using an MCP server connected to my local machine).*

I connected my local IDE environment to Claude via MCP. Chat alone could not accomplish these three tasks, but with MCP tools, the AI successfully:
1. **Read Local Files (`view_file` / `list_dir`):** The LLM directly read my local `Task.txt` and CV summary files from my hard drive without me copy-pasting them.
2. **Executed Terminal Commands (`run_command`):** The LLM autonomously ran `git commit` and `git push` directly in my Windows PowerShell to update my GitHub repository.
3. **Generated and Saved Images (`generate_image`):** The LLM autonomously generated the AI hero textures for my portfolio (for FL-6) and saved the `.png` files directly into my local Windows directory.
