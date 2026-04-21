# 🛡️ Nooxus-AI: Sourcing Edge for Claude Desktop (MCP)

[](https://modelcontextprotocol.io)
[](https://pypi.org/project/nooxus-mcp/)
[](https://opensource.org/licenses/MIT)

**Nooxus-MCP** is the official [Model Context Protocol (MCP)](https://modelcontextprotocol.io) gateway connecting AI models (Claude, Gemini, Cursor, Cherry Studio) to **real-time, verified global supply chain data**. 

By installing this, you instantly upgrade your AI from a conversational chatbot into a **Forensic Sourcing Analyst**. It cross-references the AII-NOO verified database to expose shell companies, verify real manufacturers, and completely eliminate B2B trade hallucinations.

---

## ✨ The "Aha Moment" (Key Features)

- **Zero-Hallucination Sourcing:** Direct access to Nooxus Edge nodes. If a factory is a fake trading proxy, the AI will know.
- **Forensic UI Rendering:** Forces the LLM to generate professional UI dashboards (Trust Scores, Red Flags, Capacity) instead of boring text.
- **Edge Native Architecture:** Pure Cloudflare Zero-Backend architecture featuring L1 memory caching and CRC32 payload security.
- **Out-of-the-Box Trial:** Includes a built-in global public trial key (1,000,000-query quota). **No sign-up required to start!**

---

## 🚀 Quick Start (Zero Config)

You DO NOT need an API key to start. The system will automatically use the built-in trial token. We use `uvx` for a lightning-fast, zero-install experience.

### For Claude Desktop (Recommended)
Add the following to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "nooxus-edge": {
      "command": "uvx",
      "args": ["nooxus-mcp@latest"]
    }
  }
}
```
*(Restart Claude Desktop. You will see the 🔨 hammer icon indicating Nooxus tools are loaded.)*

---

## 🔄 How to Force Upgrade

Because the `uv` package manager uses aggressive local caching for speed, you might not get the newest update immediately even with the `@latest` tag. To force an upgrade to the newest version, open your terminal and run:

```bash
uvx --refresh nooxus-mcp@latest --version
```

---

## 🎯 The Playbook (How to trigger the Sourcing Agent)

To guarantee the AI uses the verified database and renders the professional UI, always start your prompts with our cheat code: **`Use Nooxus | `**

**1. Market Scanning & Discovery**
> *"Use Nooxus | I am looking for verified suppliers of 'terminal testing equipment' in Nanjing. Please search your network."*

**2. The Deep-Dive Forensic Audit (Killer Feature 🔥)**
> *"Use Nooxus | Give me a deep-dive forensic audit on this node: NOO-PFJ77WGLNYHRXDZE. Show me the red flags and trust scores."*

---

## 🔑 Advanced: Upgrading Your Quota

Once you exhaust the generous daily limits of the global trial key, you can seamlessly plug in your own developer API key for unlimited deep-dive audits.

1. Register for free at [SmartGSC.com](https://smartgsc.com) or [Nooxus.com](https://nooxus.com).
2. Generate your `NOOXUS_API_KEY`.
3. Update your MCP config by adding the `env` block:

```json
{
  "mcpServers": {
    "nooxus-edge": {
      "command": "uvx",
      "args": ["nooxus-mcp@latest"],
      "env": {
        "NOOXUS_API_KEY": "your_personal_key_here"
      }
    }
  }
}
```

---

## 🔍 Available AI Tools (Under the hood)

1. **`semantic_search_nooxus(query)`**: Lightning-fast semantic search optimized for manufacturing entities. Returns potential partners and their NOO-IDs.
2. **`get_nooxus_node(noo_id)`**: Retrieves the full verification profile. Triggers Strategy D to force the AI to act as a Risk Analyst and render a visual warning dashboard.

---

## 👨‍💻 Developer & Troubleshooting

### 1. Command Line Testing (MCP Inspector)
Use the official inspector to visualize and test tools in your browser without Claude:
```bash
npx @modelcontextprotocol/inspector uvx --refresh nooxus-mcp
```

### 2. Local Debug Mode
To generate a local log file `mcp-logs.txt` for deep troubleshooting:
```bash
NOOXUS_DEBUG=true uvx nooxus-mcp
```

### 3. macOS Path Conflicts (`realpath` missing)
If you encounter `realpath: command not found` on older macOS versions:
```bash
brew install coreutils
export PATH="/usr/local/opt/coreutils/libexec/gnubin:$PATH"
```

---

## 📈 Release History
- **V0.1.6**: Documentation overhaul, introduced "Cheat Code" prompting strategies, explicit upgrade commands, and API Quota instructions.
- **V0.1.5**: Updated semantic search and node retrieval logic for higher UI conversion.
- **V0.1.2**: Fixed protocol pollution, enforced stderr logging.

---
**Official Portal:** [SmartGSC.com](https://smartgsc.com) | **Protocol Details:** [Nooxus.com](https://nooxus.com)