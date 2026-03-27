# 🌍 Nooxus Edge Data - Official MCP Server

[![MCP Protocol](https://img.shields.io/badge/Model_Context_Protocol-Ready-blue.svg)](https://modelcontextprotocol.io)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![Zero Backend](https://img.shields.io/badge/Architecture-Zero_Backend_Edge-success)](#)
[![License](https://img.shields.io/badge/License-MIT-gray.svg)](#)

The official [Model Context Protocol (MCP)](https://modelcontextprotocol.io) server for **Nooxus Edge Data**. 

Nooxus empowers AI models (like Claude, Gemini, Cherry Studio, and Cursor) with **real-time, verified global supply chain and manufacturing entity data**. Instantly ground your LLM's reasoning with highly accurate profiles of CNC machining workshops, assembly lines, R&D capabilities, and international standards (ISO/FDA) — completely eliminating B2B data hallucinations.

---

## ✨ Key Features

- **Zero-Hallucination Supply Chain Data:** Direct access to verified factory capabilities, debunked statuses, and granular micro-manufacturing details.
- **FTS5 Semantic Radar:** Lightning-fast Full-Text Search optimized for complex manufacturing queries (e.g., `CNC AND Assembly`).
- **Automated RFQ Engine:** Built-in capability to generate and dispatch commercial quotation requests directly from your chat interface.
- **Edge Native:** Powered by a pure Cloudflare zero-backend architecture with L1 memory caching and CRC32 payload security.
- **Built-in Global Trial:** Zero configuration required to start. A generous public trial key is built right into the package.

---

## 🛠️ Available AI Tools

When connected, your AI assistant gains the following capabilities:

1. `search_manufacturing_entities`
   - **Description:** Scans the Nooxus Global Verified Entities database using natural language or keywords. 
   - **Use Case:** *"Find authentic CNC machining factories in the Yangtze River Delta with R&D teams."*
2. `get_enterprise_details`
   - **Description:** Retrieves the full, unadulterated JSON verification profile using a unique `NOO-ID`. The AI is instructed to render this as a professional Markdown audit report.
   - **Use Case:** *"Analyze the manufacturing capabilities and verify the legal status of NOO-H5LSP53ZNGH54DIP."*
3. `generate_auto_rfq`
   - **Description:** Drafts a standardized Request for Quotation (RFQ) for selected suppliers and generates a secure $2.99 checkout link via SmartGSC to automate the dispatch process.

---

## 🚀 Quick Start & Client Configuration

You don't need to write any code or manually install packages to use Nooxus. Just copy and paste the JSON configuration below into your favorite AI client. The system will automatically fetch and run the server using `uvx`.

### Option A: Cherry Studio / Cursor
Go to your MCP settings and add a new server using the JSON import or manual entry:

```json
{
  "mcpServers": {
    "Nooxus-Global-Supply-Chain": {
      "command": "uvx",
      "args": ["nooxus-mcp"],
      "env": {
        "NOOXUS_API_KEY": "" 
      }
    }
  }
}
````

*(Note: If the `NOOXUS_API_KEY` is left empty, the server will automatically use the built-in Global Public Trial Key.)*

### Option B: Claude Desktop

Open your `claude_desktop_config.json` file (usually located in your app data folder) and append the following configuration:

```json
{
  "mcpServers": {
    "nooxus-mcp": {
      "command": "uvx",
      "args": ["nooxus-mcp"],
      "env": {
        "NOOXUS_API_KEY": "YOUR_PREMIUM_KEY_HERE"
      }
    }
  }
}
```

-----

## 👨‍💻 Developer & Local Testing

If you want to test the server visually using the official MCP Inspector before integrating it into a client:

```bash
# Run via npx using the uvx runner
npx @modelcontextprotocol/inspector uvx nooxus-mcp
```

## 🔗 Links

  - **SmartGSC Official:** [https://smartgsc.com](https://smartgsc.com)
  - **Nooxus Protocol:** [https://nooxus.com](https://nooxus.com)
  - **Issue Tracker:** [GitHub Issues](https://www.google.com/search?q=https://github.com/Nooxus-AI/nooxus-mcp/issues)

