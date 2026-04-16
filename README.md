
# 🌍 Nooxus Edge Data - Official MCP Server

[](https://modelcontextprotocol.io)
[](https://www.python.org/)
[](https://www.google.com/search?q=https://pypi.org/project/nooxus-mcp/)
[](https://www.google.com/search?q=%23)

**Nooxus-MCP** is the official bridge connecting AI models (such as Claude, Gemini, Cursor, and Cherry Studio) to **real-time, verified global supply chain data**. Built on the [Model Context Protocol (MCP)](https://modelcontextprotocol.io), it completely eliminates B2B trade hallucinations by providing LLMs with granular factory capability profiles, manufacturing process details, and ISO/FDA certification statuses.

-----

## ✨ Key Features

  - **Zero-Hallucination Supply Chain Data:** Direct access to Nooxus Edge nodes for authentic factory capabilities, debunked business statuses, and micro-manufacturing details.
  - **FTS5 Semantic Radar:** Lightning-fast Full-Text Search optimized for complex manufacturing queries (e.g., `CNC AND Assembly`).
  - **Edge Native Architecture:** A pure Cloudflare Zero-Backend architecture featuring L1 memory caching and CRC32 payload security.
  - **Plug & Play:** Includes a built-in Global Public Trial Key with a 1,000,000-query quota — no configuration required to start.

-----

## 🚀 Quick Start (Zero Config)

The recommended way to run the server is via `uvx`. If no `NOOXUS_API_KEY` is provided, the system automatically falls back to the **Global Public Trial Key**.

### 1\. Command Line Testing (MCP Inspector)

Use the official inspector to visualize and test tools in your browser:

```bash
npx @modelcontextprotocol/inspector uvx --refresh nooxus-mcp
```

### 2\. Client Integration (Cherry Studio / Cursor / Claude)

Add the following JSON to your MCP server configuration:

```json
{
  "mcpServers": {
    "Nooxus-Global": {
      "command": "uvx",
      "args": ["--refresh", "nooxus-mcp"],
      "env": {
        "NOOXUS_API_KEY": "" 
      }
    }
  }
}
```

-----

## 🛠️ Troubleshooting & Environment Optimization

Based on real-world deployment experience on macOS and multi-language environments, here are the solutions to common issues:

### 1\. macOS Path Conflicts & Missing `realpath`

**Issue:** `realpath: command not found` or `ENOENT` error.
**Cause:** macOS (e.g., Monterey) does not include the standard Linux `realpath` utility by default.
**Solution:**

```bash
brew install coreutils
# Inject into PATH (Recommended to add this to your ~/.zshrc)
export PATH="/usr/local/opt/coreutils/libexec/gnubin:$PATH"
```

### 2\. Protocol Pollution & Connection Timeouts

**Issue:** Client shows `Internal Server Error (500)` or `Invalid JSON: EOF`.
**Cause:** Non-JSON logs were printed to `stdout`, interfering with the MCP data channel.
**Solution:** Nooxus-MCP V0.1.2+ forces all logs to `stderr`. Ensure you are using the latest version:

```bash
uvx --refresh nooxus-mcp
```

### 3\. Local Debug Mode

To generate a local log file `mcp-logs.txt` for deep troubleshooting, enable the Debug switch:

```bash
NOOXUS_DEBUG=true uvx nooxus-mcp
```

-----

## 🔧 Available Tools

1.  **`search_manufacturing_entities(query)`** Scan the Nooxus Global Verified Entities database using natural language or keywords.  
    *Example: "Find authentic CNC machining factories in the Yangtze River Delta."*

2.  **`get_enterprise_details(noo_id)`** Retrieve the full JSON verification profile using a unique `NOO-ID`. The AI is instructed to render this as a professional Markdown audit report.

3.  **`generate_auto_rfq(company_name, items)`** Draft a standardized Request for Quotation (RFQ) for selected suppliers and generate a secure payment link via SmartGSC.

-----

## 📈 Release History

  - **V0.1.2 (Latest)**: Fixed protocol pollution, enforced stderr logging, and enhanced macOS compatibility.
  - **V0.1.0**: Initial Global Release.

## 📄 License

This project is licensed under the [MIT License](https://www.google.com/search?q=LICENSE).
< mcp-name: io.github.Nooxus-AI/nooxus-mcp -->
