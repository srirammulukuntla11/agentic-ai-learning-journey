# 🚀 Agentic AI Learning Journey

A comprehensive, hands-on journey from foundational Large Language Model (LLM) interactions to building an enterprise-grade, production-ready Agentic AI platform. This repository documents a complete 60-project curriculum spanning 11 progressive levels, exploring autonomous decision-making, tool execution, multi-agent collaboration, memory architectures, retrieval-augmented generation (RAG), the Model Context Protocol (MCP), and production reliability engineering.

Rather than relying purely on theoretical abstractions, every project is built and validated through real-world implementations using **n8n workflow automation**, **Python**, **LangChain**, **LangGraph**, and **FastMCP**, powered by **Google Gemini**, vector databases, and enterprise data integrations.

---

# 📚 Workflow Collection

## 🟢 Level 1 — Agent & LLM Foundations
### Projects 01–07

Foundational concepts of agentic systems, prompt engineering, structured outputs, and context preservation using Google Gemini and n8n.

| **#** | **Project** | **Description** |
| :---: | ----------- | --------------- |
| 01 | **First Simple AI Agent** | Built a baseline conversational AI agent connected to Google Gemini to understand core agent-LLM execution loops. |
| 02 | **Prompt-Based Decision Agent** | Designed rule-guided prompt templates to classify customer inquiries into priority tiers (High, Medium, Low). |
| 03 | **Structured Output Agent** | Constrained LLM outputs into strict JSON schemas for deterministic downstream application consumption. |
| 04 | **AI Text Classification Agent** | Automated classification of incoming user queries and support messages into predefined categories. |
| 05 | **AI Information Extraction Agent** | Parsed unstructured natural-language text to extract entities, dates, and attributes into structured key-value pairs. |
| 06 | **AI Text Summarization Agent** | Synthesized long-form textual documents into concise, structured summaries capturing key takeaways. |
| 07 | **Context-Aware AI Agent** | Implemented multi-turn conversational context retention to handle nuanced follow-up inquiries. |

---

## 🔵 Level 2 — Tool & Function Calling
### Projects 08–15

Equipping LLM agents with deterministic computation, live web retrieval, and external API tool-calling capabilities.

| **#** | **Project** | **Description** |
| :---: | ----------- | --------------- |
| 08 | **Calculator Agent** | Integrated an arithmetic calculator tool allowing the agent to perform accurate mathematical computations. |
| 09 | **Date & Time Agent** | Bound temporal manipulation tools to resolve relative, absolute, and cross-timezone date/time queries. |
| 10 | **Unit Conversion Agent** | Built custom computation tooling to accurately convert metric, imperial, and physical units. |
| 11 | **Web Search Agent** | Integrated Brave Search API to augment the LLM with real-time web search capabilities for current events. |
| 12 | **API Calling Agent** | Implemented an HTTP request tool enabling the agent to retrieve live remote resources from external REST APIs. |
| 13 | **Weather Information Agent** | Bound OpenWeatherMap API tools to retrieve real-time weather and forecast data for any location. |
| 14 | **Multi-Tool Agent** | Coordinated multiple specialized tools (calculator, date/time, weather) within a unified agent loop. |
| 15 | **Dynamic Tool Selection Agent** | Implemented dynamic reasoning to evaluate queries and select appropriate tools only when necessary. |

---

## 🟣 Level 3 — Practical Single Agents
### Projects 16–23

Task-oriented autonomous agents designed for research, document parsing, database querying, and personal productivity.

| **#** | **Project** | **Description** |
| :---: | ----------- | --------------- |
| 16 | **Web Research Agent** | Engineered multi-step search orchestration to gather, analyze, and synthesize detailed web research briefs. |
| 17 | **News Research Agent** | Filtered real-time news articles to monitor recent developments and generate concise news summaries. |
| 18 | **Document Reading Agent** | Ingested uploaded corporate text documents to deliver grounded question answering with direct citations. |
| 19 | **PDF Question-Answering Agent** | Parsed binary PDF documents and extracted text context for accurate conversational question answering. |
| 20 | **Database Query Agent** | Connected to MongoDB collections to translate natural-language prompts into NoSQL database queries. |
| 21 | **SQL Assistant Agent** | Generated and executed SQL queries against Supabase PostgreSQL from natural language input. |
| 22 | **Personal Assistant Agent** | Orchestrated scheduling, calculation, and weather queries into a unified everyday assistant. |
| 23 | **Task Management Agent** | Performed CRUD operations on task records in Supabase PostgreSQL via conversational interaction. |

---

## 🟡 Level 4 — Agent Memory and State
### Projects 24–28

Architecting session memory, short-term scratchpads, persistent long-term storage, and personalized preference models.

| **#** | **Project** | **Description** |
| :---: | ----------- | --------------- |
| 24 | **Conversation Memory Agent** | Implemented window buffer memory to recall prior conversational turns within active sessions. |
| 25 | **Short-Term Memory Agent** | Maintained temporary session-scoped scratchpad state across complex multi-step reasoning tasks. |
| 26 | **Long-Term Memory Agent** | Persisted user facts and interaction history in Supabase PostgreSQL across independent sessions. |
| 27 | **User Preference Memory Agent** | Stored and retrieved user-specific preferences to dynamically tailor ongoing agent behaviors. |
| 28 | **Stateful Personal Assistant** | Synthesized short-term memory, persistent long-term storage, and user preferences into a stateful assistant. |

---

## 🟠 Level 5 — RAG & Agentic RAG
### Projects 29–35

Information retrieval systems, vector embeddings, semantic knowledge bases, and autonomous Agentic RAG pipelines.

| **#** | **Project** | **Description** |
| :---: | ----------- | --------------- |
| 29 | **Basic RAG System** | Implemented a baseline Retrieval-Augmented Generation pipeline answering queries from corporate policy files. |
| 30 | **Document Search Agent** | Built semantic document search using dense vector embeddings to locate relevant knowledge segments. |
| 31 | **Knowledge Base Agent** | Ingested multiple corporate policy documents (leave, benefits, WFH) into a unified domain knowledge base. |
| 32 | **Vector Database Agent** | Stored and queried vector embeddings using Supabase Vector (`pgvector`) for semantic retrieval. |
| 33 | **Multi-Document RAG Agent** | Synthesized answers across diverse enterprise documents and multi-source reference files. |
| 34 | **RAG + Tool-Using Agent** | Combined semantic document retrieval with tool execution (e.g. calculator) to solve complex policy queries. |
| 35 | **Agentic RAG System** | Built an autonomous RAG agent that dynamically decides when retrieval is needed and verifies relevance. |

---

## 🔴 Level 6 — Planning & Decision-Making
### Projects 36–40

Deliberative cognitive architectures: task decomposition, dynamic routing, self-reflection, and autonomous error recovery.

| **#** | **Project** | **Description** |
| :---: | ----------- | --------------- |
| 36 | **Task Planning Agent** | Designed an agent that generates structured multi-step execution plans before taking action. |
| 37 | **Task Decomposition Agent** | Decomposed complex goals into modular, dependent sub-tasks for structured execution. |
| 38 | **Routing Agent** | Evaluated user intents to dynamically route requests to domain-specialized execution pathways. |
| 39 | **Reflection Agent** | Built an iterative self-reflection loop where the agent critiques and refines its own generated outputs. |
| 40 | **Self-Correcting Agent** | Validated intermediate execution results and autonomously corrected errors before final delivery. |

---

## 🛡️ Level 7 — Human-in-the-Loop & Reliability
### Projects 41–45

Enterprise governance patterns, human review checkpoints, failure recovery strategies, and operational resilience.

| **#** | **Project** | **Description** |
| :---: | ----------- | --------------- |
| 41 | **Human Approval Agent** | Implemented interactive "Send and Wait" human approval gates before executing sensitive operations. |
| 42 | **Agent Retry System** | Configured automated retry policies with exponential backoff to handle transient tool and network failures. |
| 43 | **Agent Error Recovery System** | Built error interception workflows that catch execution exceptions and gracefully recover. |
| 44 | **Agent with Fallback Tools** | Implemented secondary backup tools to maintain system availability when primary tools fail. |
| 45 | **Reliable Business Process Agent** | Combined human approvals, input validation, automated retries, and fallbacks into an enterprise business workflow. |

---

## ⚡ Level 8 — Agent Frameworks
### Projects 46–50

Programmatic agent architectures built in Python utilizing LangChain and LangGraph state graphs.

| **#** | **Project** | **Description** |
| :---: | ----------- | --------------- |
| 46 | **LangChain Agent** | Implemented a Python-based autonomous agent using the LangChain framework and Google Gemini. |
| 47 | **LangChain Tool-Using Agent** | Bound custom Python function tools (`@tool`) to a LangChain agent for specialized mathematical operations. |
| 48 | **LangGraph Basic Agent** | Built a graph-based agent architecture using LangGraph `StateGraph`, defining nodes, edges, and transitions. |
| 49 | **LangGraph Stateful Agent** | Implemented typed state tracking (`AgentState`) to preserve conversational context across graph nodes. |
| 50 | **LangGraph Advanced Agent** | Engineered dynamic conditional routing (`add_conditional_edges`) to branch execution based on intent analysis. |

---

## 🔌 Level 9 — MCP & External Systems
### Projects 51–54

Client-server tool architectures implementing Anthropic's Model Context Protocol (MCP) using Python and FastMCP.

| **#** | **Project** | **Description** |
| :---: | ----------- | --------------- |
| 51 | **MCP Fundamentals Project** | Developed a Model Context Protocol (MCP) server and client using the official Python MCP SDK and FastMCP. |
| 52 | **MCP Tool Agent** | Built an AI agent that dynamically discovers and invokes tools exposed by an MCP server over stdio. |
| 53 | **MCP + Database Agent** | Integrated an MCP tool server exposing an SQLite database, allowing the agent to query student records. |
| 54 | **MCP + Multiple External Tools Agent** | Coordinated multiple external capabilities exposed across decoupled MCP server interfaces. |

---

## 👥 Level 10 — Multi-Agent System
### Projects 55–57

Decentralized and hierarchical multi-agent architectures for collaborative problem solving and role specialization.

| **#** | **Project** | **Description** |
| :---: | ----------- | --------------- |
| 55 | **Multi-Agent Research System** | Orchestrated independent agents collaborating to conduct research and compile comprehensive briefs. |
| 56 | **Supervisor + Worker Agents** | Implemented a hierarchical multi-agent pattern where a supervisor agent plans and delegates to worker agents. |
| 57 | **Researcher + Analyst + Writer System** | Built a specialized 3-agent pipeline: Researcher gathers raw data, Analyst evaluates insights, and Writer crafts reports. |

---

## 🚀 Level 11 — Production Agentic AI
### Projects 58–60

Production readiness engineering: observability, security guardrails, automated alerting, and full platform synthesis.

| **#** | **Project** | **Description** |
| :---: | ----------- | --------------- |
| 58 | **Agent Evaluation & Observability System** | Automated agent evaluation scoring (correctness, relevance, clarity) and logged telemetry to Google Sheets. |
| 59 | **Secure Production Agent** | Engineered a security guardrail layer with prompt injection detection to block malicious inputs before execution. |
| 60 | **Final End-to-End Agentic AI Platform** | Built a production-grade enterprise platform integrating routing, planning, execution, RAG, tools, memory, approvals, and error alerts. |

---

# 🛠️ Technologies & Tools

The implementations across all 11 levels utilize the following technologies, libraries, and services:

| Technology | Category | Role in Repository |
| ---------- | -------- | ------------------ |
| **n8n** | Workflow Automation | Core visual orchestrator used for building multi-step agent pipelines, triggers, routing, and tool connectors. |
| **Google Gemini** | Large Language Model | Primary foundation model (`gemini-3.8-flash`) providing reasoning, classification, planning, and synthesis. |
| **Python** | Programming Language | Core language for programmatic agent frameworks, MCP servers, and stateful graph pipelines (v3.10+). |
| **LangChain** | Agent Framework | Python framework for prompt abstraction, agent invocation (`create_agent`), and tool decorators (`@tool`). |
| **LangGraph** | Graph Orchestration | Framework for deterministic cyclic and acyclic agent graphs with typed state management (`StateGraph`). |
| **FastMCP / MCP SDK** | Model Context Protocol | Open standard for standardizing tool interfaces and client-server tool execution over stdio and SSE. |
| **Supabase & PostgreSQL** | Relational & Vector DB | Cloud database used for long-term memory persistence, relational SQL queries, and `pgvector` embeddings. |
| **MongoDB** | NoSQL Database | Document store used for customer data persistence and natural-language NoSQL querying. |
| **SQLite** | Embedded Database | Local database used for MCP database server demonstrations (`students.db`). |
| **OpenAI Embeddings** | Embeddings | Model used for vector embeddings in knowledge retrieval and semantic RAG indexing. |
| **Brave Search API** | Search Engine API | Real-time web retrieval tool for live research and current news summarization. |
| **OpenWeatherMap API** | Weather API | Meteorological data API used for dynamic environmental tool calling. |
| **Google Sheets** | Telemetry & Logging | Production observability destination for agent evaluation metrics, scores, and execution logs. |
| **Gmail** | Alerting & Notifications | Transactional alerting mechanism for production workflow failures and error monitoring. |

---

# 🧠 Key Concepts Practiced

### Agent Foundations
- **Autonomous Agent Loop:** Implementing perception-reasoning-action execution cycles.
- **Prompt Engineering:** Designing role definitions, guardrails, and decision guidelines.
- **Structured Outputs:** Enforcing schema-validated JSON outputs from probabilistic models.
- **Text Classification & Extraction:** Autonomous parsing of categories, parameters, and entities.

### Tools & Actions
- **Function Calling & Tool Binding:** Exposing deterministic functions to LLMs via standard schemas.
- **Dynamic Tool Selection:** Allowing models to evaluate whether tool execution is required.
- **Multi-Tool Orchestration:** Managing concurrent access to mathematical, temporal, search, and API tools.

### Memory & Context
- **Window Buffer Memory:** Retaining conversational turns across multi-turn chat sessions.
- **Short-Term Scratchpad:** Scoping intermediate reasoning state to specific task lifecycles.
- **Long-Term Persistence:** Storing user facts and conversational history in PostgreSQL.
- **User Preference Modeling:** Recalling personalized user preferences across sessions.

### RAG & Knowledge
- **Semantic Vector Search:** Indexing documents with dense embeddings for similarity retrieval.
- **Vector Databases:** Managing collections and vector indices in Supabase `pgvector`.
- **Hybrid RAG + Tool Execution:** Combining retrieved reference context with computational tools.
- **Agentic RAG:** Enabling agents to autonomously decide if, when, and what knowledge to retrieve.

### APIs & Databases
- **SQL Generation & Execution:** Translating natural language into valid SQL against relational databases.
- **NoSQL Document Retrieval:** Interfacing with MongoDB collections using structured queries.
- **REST Integrations:** Dynamic interaction with third-party web services via HTTP endpoints.

### Planning & Reasoning
- **Task Decomposition:** Breaking down complex goals into ordered, achievable sub-tasks.
- **Multi-Step Task Planning:** Formulating high-level execution plans prior to tool invocation.
- **Intent-Based Routing:** Dispatching queries to dedicated execution paths based on complexity.
- **Reflection & Self-Correction:** Iteratively evaluating intermediate results and correcting errors.

### Human-in-the-Loop & Reliability
- **Approval Checkpoints:** Pausing workflow execution with interactive human review forms ("Send and Wait").
- **Retry Mechanisms:** Handling transient service and tool errors with automated retry logic.
- **Fault Tolerance & Fallbacks:** Providing secondary tooling when primary endpoints experience downtime.

### Multi-Agent Systems
- **Agent Specialization:** Segregating responsibilities across dedicated Researcher, Analyst, and Writer roles.
- **Supervisor-Worker Pattern:** Implementing centralized coordinators that delegate to specialized workers.
- **Collaborative Synthesis:** Passing structured intermediate state across autonomous agents.

### Model Context Protocol (MCP)
- **FastMCP Server Architecture:** Building decoupled tool servers using the official MCP Python SDK.
- **Client Session Management:** Establishing stdio client connections and tool discovery protocols.
- **External Resource Exposure:** Standardizing database and tool access across disparate platforms.

### Production Agentic AI
- **Observability & Evaluation:** Scoring responses on correctness, relevance, and clarity, logged to Google Sheets.
- **Security Guardrails:** Pre-execution prompt injection detection and conditional gatekeeping.
- **Enterprise Error Handling:** Real-time error interception and automated administrative alerting via Gmail.

---

# 🏗️ Final Project Architecture

Project 60 represents the culmination of this learning journey: an **End-to-End Enterprise Agentic AI Platform** implemented in n8n. It brings together intelligent query classification, two-stage planning and execution, dynamic tool calling, knowledge retrieval, human governance, MCP integration, and automated failure alerting into a unified production architecture.

### Workflow Architecture Diagram

```
                                  ┌────────────────────────┐
                                  │      User Input        │
                                  │     (Chat Trigger)     │
                                  └───────────┬────────────┘
                                              │
                                              ▼
                                  ┌────────────────────────┐
                                  │      Router Agent      │◄─── [Router LLM: Gemini]
                                  └───────────┬────────────┘
                                              │
                                              ▼
                                  ┌────────────────────────┐
                                  │    Complexity Router   │
                                  │   (Conditional Gate)   │
                                  └─────┬────────────┬─────┘
                     [False / Simple]   │            │   [True / Complex]
             ┌──────────────────────────┘            └─────────────────────────┐
             ▼                                                                 ▼
┌─────────────────────────┐                                       ┌─────────────────────────┐
│  Simple Response Agent  │◄─── [Simple Response LLM: Gemini]     │     Planning Agent      │◄─── [Planning LLM: Gemini]
│                         │◄─── [Conversation Memory]             └────────────┬────────────┘
└────────────┬────────────┘                                                    │
             │                                                                 ▼
             ▼                                                    ┌─────────────────────────┐
┌─────────────────────────┐                                       │     Execution Agent     │◄─── [Execution LLM: Gemini]
│  Simple Response Output │                                       └────────────┬────────────┘
└─────────────────────────┘                                                    │
                                                      ┌────────────────────────┼────────────────────────┐
                                                      │                        │                        │
                                                      ▼                        ▼                        ▼
                                            ┌───────────────────┐    ┌───────────────────┐    ┌───────────────────┐
                                            │ MongoDB Database  │    │ External REST API │    │    MCP Client     │
                                            │  (Customer Data)  │    │ (JSONPlaceholder) │    │  (MCP Protocol)   │
                                            └───────────────────┘    └───────────────────┘    └─────────┬─────────┘
                                                                                                        │
                                                      ┌─────────────────────────────────────────────────┼───────────────────┐
                                                      │                                                 │                   │
                                                      ▼                                                 ▼                   ▼
                                            ┌───────────────────┐                             ┌───────────────────┐   ┌─────────────────────────┐
                                            │   RAG Knowledge   │                             │  Human Approval   │   │   MCP Server Workflow   │
                                            │     Retrieval     │                             │  (Send and Wait)  │   │  (Calculator Service)   │
                                            │ [OpenAI Embed.]   │                             └─────────┬─────────┘   └─────────────────────────┘
                                            └───────────────────┘                                       │
                                                                                                        ▼
                                                                                              ┌───────────────────┐
                                                                                              │Approved Calculator│
                                                                                              └───────────────────┘
                                                                                                        │
                                                                                                        ▼
                                                                                              ┌─────────────────────────┐
                                                                                              │  Final Response Output  │
                                                                                              └─────────────────────────┘
```

### Knowledge Ingestion Pipeline

```
┌──────────────────────────┐     ┌────────────────────────┐     ┌────────────────────────┐
│ Knowledge Document Upload│────►│ Knowledge Vector Store │◄────│    Document Loader     │
└──────────────────────────┘     │      (In-Memory)       │     └───────────▲────────────┘
                                 └───────────▲────────────┘                 │
                                             │                  ┌───────────┴────────────┐
                                 ┌───────────┴────────────┐     │     Text Chunking      │
                                 │  Document Embeddings   │     └────────────────────────┘
                                 │        (OpenAI)        │
                                 └────────────────────────┘
```

### Major Capabilities of Project 60

1. **Intelligent Query Routing:** The **Router Agent** analyzes incoming queries and uses a conditional gate to bypass heavy multi-step planning for straightforward conversational prompts.
2. **Fast Conversational Path:** Simple requests are handled immediately by the **Simple Response Agent**, maintaining context using **Window Buffer Conversation Memory**.
3. **Two-Stage Multi-Agent Reasoning:**
   - **Planning Agent:** Formulates a structured, step-by-step execution strategy for complex objectives.
   - **Execution Agent:** Operates as the runtime executor, dynamically selecting and invoking tools to fulfill each step of the plan.
4. **Database & API Connectivity:**
   - **MongoDB Database:** Executes queries against customer document collections for customer data retrieval.
   - **External REST API:** Performs live HTTP requests to retrieve third-party enterprise data.
5. **Domain Knowledge Retrieval (RAG):** Connects to a dedicated vector store populated by an automated document ingestion pipeline with text chunking and OpenAI embeddings.
6. **Human-in-the-Loop Governance:** High-stakes operations (such as computational execution) trigger an interactive **Human Approval** modal ("Send and wait"), requiring explicit user confirmation before the **Approved Calculator** executes.
7. **Model Context Protocol (MCP) Integration:** Features an **MCP Client** node communicating with a decoupled **MCP Server Workflow**, illustrating cross-system tool discovery and execution.

---

# ⚙️ Production Error Handling

In enterprise environments, silent agent failures or unhandled exceptions can break business operations. Project 60 implements a dedicated, decoupled **Error Handler Workflow** that monitors execution health across the platform.

```
┌─────────────────────────────────┐               ┌─────────────────────────────────┐
│          Error Trigger          │──────────────►│      Send a Message (Gmail)     │
│   (Captures Any Node Failure)   │               │   (Automated Incident Alert)    │
└─────────────────────────────────┘               └─────────────────────────────────┘
```

### How the Error Handling Works:
1. **Automated Interception:** If any node in the production workflow fails (e.g. max iteration limit exceeded, API timeout, or malformed tool payload), the failure is intercepted by the **Error Trigger**.
2. **Contextual Diagnostic Capture:** The error trigger extracts critical execution metadata, including:
   - **Workflow Name:** The affected workflow instance (`Final End-to-End Agentic AI Platform`).
   - **Failed Node:** The exact node where execution stopped (e.g., `Execution Agent`).
   - **Error Message:** The descriptive error reason (e.g., `Max iterations reached`).
   - **Execution ID:** The unique execution identifier for rapid debugging and trace audit.
3. **Real-Time Incident Alerting:** A structured email notification is automatically generated and dispatched via the **Gmail** integration to system administrators, ensuring immediate visibility into production anomalies.

---

# 📂 Repository Structure

```
AGENTIC_AI/
├── Level 1 — Agent & LLM Foundations/
│   ├── 1. First Simple AI Agent/
│   ├── 2. Prompt-Based Decision Agent/
│   ├── 3. Structured Output Agent/
│   ├── 4. AI Text Classification Agent/
│   ├── 5. AI Information Extraction Agent/
│   ├── 6. AI Text Summarization Agent/
│   └── 7. Context-Aware AI Agent/
├── Level 2 — Tool & Function Calling/
│   ├── 8. Calculator Agent/
│   ├── 9. Date & Time Agent/
│   ├── 10. Unit Conversion Agent/
│   ├── 11. Web Search Agent/
│   ├── 12. API Calling Agent/
│   ├── 13. Weather Information Agent/
│   ├── 14. Multi-Tool Agent/
│   └── 15. Dynamic Tool Selection Agent/
├── LEVEL 3 - Practical Single Agents/
│   ├── 16. Web Research Agent/
│   ├── 17. News Research Agent/
│   ├── 18. Document Reading Agent/
│   ├── 19. PDF Question-Answering Agent/
│   ├── 20. Database Query Agent/
│   ├── 21. SQL Assistant Agent/
│   ├── 22. Personal Assistant Agent/
│   └── 23. Task Management Agent/
├── LEVEL 4 - Agent Memory and State/
│   ├── 24. Conversation Memory Agent/
│   ├── 25. Short-Term Memory Agent/
│   ├── 26. Long-Term Memory Agent/
│   ├── 27. User Preference Memory Agent/
│   └── 28. Stateful Personal Assistant/
├── LEVEL 5 - RAG & AGENTIC RAG/
│   ├── 29. Basic RAG System/
│   ├── 30. Document Search Agent/
│   ├── 31. Knowledge Base Agent/
│   ├── 32. Vector Database Agent/
│   ├── 33. Multi-Document RAG Agent/
│   ├── 34. RAG + Tool-Using Agent/
│   └── 35. Agentic RAG System/
├── Level 6 — Planning & Decision-Making/
│   ├── 36. Task Planning Agent/
│   ├── 37. Task Decomposition Agent/
│   ├── 38. Routing Agent/
│   ├── 39. Reflection Agent/
│   └── 40. Self-Correcting Agent/
├── Level 7 — Human-in-the-Loop & Reliability/
│   ├── 41. Human Approval Agent/
│   ├── 42. Agent Retry System/
│   ├── 43. Agent Error Recovery System/
│   ├── 44. Agent with Fallback Tools/
│   └── 45. Reliable Business Process Agent/
├── Level 8 — Agent Frameworks/
│   ├── 46. LangChain Agent/
│   ├── 47. LangChain Tool-Using Agent/
│   ├── 48. LangGraph Basic Agent/
│   ├── 49. LangGraph Stateful Agent/
│   └── 50. LangGraph Advanced Agent/
├── Level 9 — MCP & External Systems/
│   ├── 51. MCP Fundamentals Project/
│   ├── 52. MCP Tool Agent/
│   ├── 53. MCP + Database Agent/
│   └── 54. MCP + Multiple External Tools Agent/
├── Level 10 — Multi-Agent System/
│   ├── 55. Multi-Agent Research System/
│   ├── 56. Supervisor + Worker Agents/
│   └── 57. Researcher + Analyst + Writer System/
├── Level 11 — Production Agentic AI/
│   ├── 58. Agent Evaluation & Observability System/
│   ├── 59. Secure Production Agent/
│   └── 60. Final End-to-End Agentic AI Platform/
└── README.md
```

---

# 🔥 Learning Approach

Every single project in this repository followed a strict, hands-on engineering cycle:

```
Theory
   ↓
Build
   ↓
Test
   ↓
Debug
   ↓
Understand
   ↓
Document
   ↓
Next Project
```

1. **Theory:** Understand the algorithmic or architectural paradigm (e.g., ReAct loop, state machines, vector embeddings, tool protocols).
2. **Build:** Implement the pipeline hands-on in n8n or write the Python agent from scratch.
3. **Test:** Execute realistic test cases across diverse user inputs and boundary conditions.
4. **Debug:** Inspect execution traces, fix reasoning loops, address schema mismatches, and handle timeouts.
5. **Understand:** Analyze why specific patterns succeeded or failed in production runtime.
6. **Document:** Capture architectural diagrams, execution logs, and key takeaways.
7. **Next Project:** Advance to the next level of complexity.

---

# 🏆 Journey Completed

```
60 Projects
11 Levels
Agentic AI → Production Agentic AI
```

### Architectural Progression

```
LLM
 ↓
AI Agent
 ↓
Tools
 ↓
Memory
 ↓
RAG
 ↓
APIs
 ↓
Database
 ↓
Planning
 ↓
Human Approval
 ↓
Multi-Agent Systems
 ↓
MCP
 ↓
Production Architecture
 ↓
End-to-End Agentic AI Platform
```

---

## 👨‍💻 Author

**Sriram Mulukuntla**  
B.Tech — Computer Science & Engineering (AI/ML)

---

⭐ If you find this journey useful, consider starring the repository!
