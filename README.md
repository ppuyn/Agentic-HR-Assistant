# 🤖 Agentic HR Assistant

## Project Overview
This project demonstrates a functional **Agentic AI** designed to reduce HR administrative overhead. It utilizes a **Retrieval-Augmented Generation (RAG)** architecture to allow an LLM to "read" internal company policies and execute basic HR tasks autonomously.
## System Architecture
The agent follows a **Reasoning + Acting (ReAct)** logic:
1. **User Query:** "How many vacation days do I have left?"
2. **Reasoning:** The LLM identifies it needs the `check_vacation_balance` tool.
3. **Action:** Python executes the script to query the database.
4. **Observation:** The script returns "12 days."
5. **Response:** The LLM generates a natural language answer for the employee.

---