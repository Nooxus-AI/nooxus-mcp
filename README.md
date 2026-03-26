# 🌍 Nooxus Edge Data - Official MCP Server

[![MCP Protocol](https://img.shields.io/badge/Model_Context_Protocol-Ready-blue.svg)](https://modelcontextprotocol.io)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![Zero Backend](https://img.shields.io/badge/Architecture-Zero_Backend_Edge-success)](#)

The official [Model Context Protocol (MCP)](https://modelcontextprotocol.io) server for **Nooxus Edge Data**. 

Nooxus empowers AI models (like Claude, Gemini, and Cursor) with **real-time, verified global supply chain and manufacturing entity data**. Instantly ground your LLM's reasoning with highly accurate profiles of CNC machining workshops, assembly lines, R&D capabilities, and international standards (ISO/FDA) — completely eliminating B2B data hallucinations.

---

## ✨ Key Features

- **Zero-Hallucination Supply Chain Data:** Direct access to verified factory capabilities, debunked statuses, and granular micro-manufacturing details.
- **FTS5 Semantic Radar:** Lightning-fast Full-Text Search optimized for complex manufacturing queries (e.g., `CNC AND Assembly`).
- **Edge Native:** Powered by a pure Cloudflare zero-backend architecture with L1 memory caching and CRC32 payload security.
- **Built-in Global Trial:** Zero configuration required to start. A generous 1,000,000-query global trial key is built right into the package.

## 🚀 Quick Start (Zero Config)

You can run the Nooxus MCP server immediately. If you don't provide an API Key, it will automatically fall back to the **Global Public Trial Key**.

To test it visually using the official MCP Inspector:
```bash
npx @modelcontextprotocol/inspector uvx nooxus-mcp
