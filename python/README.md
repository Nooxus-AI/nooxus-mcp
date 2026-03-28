
# 🌍 Nooxus Edge Data - Official MCP Server

[](https://modelcontextprotocol.io)
[](https://www.google.com/search?q=https://pypi.org/project/nooxus-mcp/)
[](https://www.python.org/)
[](https://opensource.org/licenses/MIT)

**Nooxus-MCP** is the official [Model Context Protocol (MCP)](https://modelcontextprotocol.io) gateway to **real-time, verified global supply chain data**.

By connecting Nooxus to AI agents like **Claude, Gemini, Cherry Studio, or Cursor**, you empower your LLM with "Ground Truth" manufacturing entity data. Instantly verify factory capabilities, R\&D profiles, and international certifications (ISO/FDA) while completely eliminating B2B data hallucinations.

-----

## ✨ Key Features

  - **Zero-Hallucination Data:** Direct access to Nooxus Edge nodes for verified factory details and debunked business statuses.
  - **FTS5 Semantic Search:** Lightning-fast Full-Text Search optimized for manufacturing (e.g., `CNC AND Assembly`).
  - **Silent Protocol (V0.1.2+):** Optimized I/O handling that prevents "Protocol Pollution" errors by forcing logs to `stderr`.
  - **Edge Native:** Powered by Cloudflare zero-backend architecture with L1 memory caching and CRC32 payload security.
  - **Global Public Trial:** Includes a built-in trial key with a 1,000,000-query quota—no sign-up required to start.

-----

## 🚀 Quick Start (Client Configuration)

The most efficient way to run Nooxus-MCP is using `uvx`. No manual installation is required.

### 1\. For Cherry Studio / Cursor

Add a new MCP server using the following JSON configuration:

```json
{
  "mcpServers": {
    "Nooxus-Global-Supply-Chain": {
      "command": "uvx",
      "args": ["--refresh", "nooxus-mcp"],
      "env": {
        "NOOXUS_API_KEY": "" 
      }
    }
  }
}
```

*(Note: If the `NOOXUS_API_KEY` is empty, the server defaults to the **Global Public Trial Key**.)*

### 2\. For Claude Desktop

Append this to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "nooxus-mcp": {
      "command": "uvx",
      "args": ["--refresh", "nooxus-mcp"],
      "env": {
        "NOOXUS_API_KEY": "YOUR_PREMIUM_KEY_HERE"
      }
    }
  }
}
```

-----

## 🛠️ Critical Troubleshooting (macOS 12+)

If you encounter connection errors or "Command not found" on macOS:

1.  **Fix Missing `realpath`:** macOS (especially Monterey and older) lacks the standard Linux `realpath`.
    ```bash
    brew install coreutils
    export PATH="/usr/local/opt/coreutils/libexec/gnubin:$PATH"
    ```
2.  **Force Update:** To ensure you are running the latest silent protocol version (V0.1.2):
    ```bash
    uvx --refresh nooxus-mcp
    ```

-----

## 🔍 Available AI Tools

1.  **`search_manufacturing_entities(query)`** Searches the Nooxus database using natural language.  
    *Use Case: "Find authentic CNC machining factories in the Yangtze River Delta."*

2.  **`get_enterprise_details(noo_id)`** Retrieves the full, unadulterated verification profile using a `NOO-ID`. The AI will render this as a professional Markdown audit report.

3.  **`generate_auto_rfq(company_name, items)`** Drafts a standardized RFQ and generates a secure $2.99 checkout link via **SmartGSC** to automate the commercial dispatch.

-----

## 👨‍💻 Developer & Debugging

Test the server visually using the official MCP Inspector:

```bash
npx @modelcontextprotocol/inspector uvx --refresh nooxus-mcp
```

To enable local file logging for troubleshooting:

```bash
NOOXUS_DEBUG=true uvx nooxus-mcp
```

-----

## 🔗 Links

  - **Official Portal:** [SmartGSC.com](https://smartgsc.com)
  - **Protocol Details:** [Nooxus.com](https://nooxus.com)
  - **Support:** [Issue Tracker](https://www.google.com/search?q=https://github.com/Nooxus-AI/nooxus-mcp/issues)
