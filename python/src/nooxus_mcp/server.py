import os
import sys
import urllib.parse
import httpx
import logging
import json
from datetime import datetime
from pathlib import Path
from mcp.server.fastmcp import FastMCP

# =====================================================================
# 🛠️ 1. 调试与日志配置 (Debug Switch)
# =====================================================================
# 通过环境变量或直接修改此布尔值来控制
DEBUG_MODE = os.environ.get("NOOXUS_DEBUG", "false").lower() == "true"

logger = logging.getLogger("NooxusFlow")
logger.setLevel(logging.DEBUG)

# 清除所有现有的 Handler，防止重复输出
logger.handlers = []

if DEBUG_MODE:
    # --- 本地调试模式：开启文件记录 ---
    CURRENT_DIR = Path(__file__).parent.absolute()
    LOG_FILE = CURRENT_DIR / "mcp-logs.txt"
    file_handler = logging.FileHandler(LOG_FILE, encoding='utf-8')
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
else:
    # --- 生产分发模式：仅向 stderr 输出 (MCP 标准做法) ---
    # 这样日志不会污染 stdout 协议通道，但能在客户端的日志窗口看到
    stderr_handler = logging.StreamHandler(sys.stderr)
    stderr_handler.setFormatter(logging.Formatter('[%(levelname)s] %(message)s'))
    logger.addHandler(stderr_handler)

def log_debug(tag, tool, message, detail=None):
    """
    统一日志入口
    MCP 规范：所有非 JSON-RPC 数据必须进入 stderr
    """
    entry = {
        "tag": tag,
        "tool": tool,
        "msg": message,
        "detail": detail
    }
    # 转换为 JSON 字符串方便阅读
    log_msg = json.dumps(entry, ensure_ascii=False)
    
    if DEBUG_MODE:
        logger.info(log_msg)
    else:
        # 生产模式下，直接打印到 stderr 即可
        print(f"[{tag}] {message}", file=sys.stderr, flush=True)

# =====================================================================
# 🚀 2. MCP 服务器初始化与鉴权
# =====================================================================
mcp = FastMCP("Nooxus Search Edge")

# 🎁 全球开发者公测 Token
DEFAULT_TRIAL_KEY = "nx_sk_test_cc5081ef8a9f29a6_eee9"

def get_headers():
    api_key = os.environ.get("NOOXUS_API_KEY", DEFAULT_TRIAL_KEY)
    return {
        "Authorization": f"Bearer {api_key}", 
        "Content-Type": "application/json",
        "User-Agent": "Nooxus-MCP-Client/1.0"
    }

# =====================================================================
# 🔍 3. 工具集：保持业务逻辑不变
# =====================================================================
@mcp.tool()
async def search_manufacturing_entities(query: str) -> str:
    """搜索全球制造实体 (Nooxus Verified Global Entities)"""
    log_debug("REQ_START", "search", f"Query: {query}")
    
    headers = get_headers()
    safe_query = urllib.parse.quote(query)
    url = f"https://mcp.nooxus.com/v1/search?q={safe_query}"
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=15.0)
            log_debug("HTTP_RECV", "search", f"Status: {response.status_code}")
            
            if response.status_code == 402:
                return "🚨 [Quota Error]: 全球体验额度已用完，请前往 SmartGSC.com 获取专属 API Key。"
            elif response.status_code != 200:
                return f"🚨 [Search Error {response.status_code}]"
            
            footer = "\n\n---\n💡 [Prompt]: 使用 `get_enterprise_details` 获取该企业的 `noo_id` 完整档案。"
            return response.text + footer
        except Exception as e:
            log_debug("EXCEPTION", "search", str(e))
            return f"🚨 [Network Error]: {str(e)}"

@mcp.tool()
async def get_enterprise_details(noo_id: str) -> str:
    """通过 noo_id 获取企业的完整商业验证档案"""
    clean_id = noo_id.strip().upper()
    log_debug("REQ_START", "details", f"ID: {clean_id}")
    
    headers = get_headers()
    url = f"https://mcp.nooxus.com/noo/{urllib.parse.quote(clean_id)}"
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=15.0)
            log_debug("HTTP_RECV", "details", f"Status: {response.status_code}")
            
            if response.status_code != 200:
                return f"🚨 [Detail Error {response.status_code}]"
            
            footer = "\n\n---\n💡 [Prompt]: 请以严谨的 Markdown 格式为其渲染一份《验证报告》。"
            return response.text + footer
        except Exception as e:
            log_debug("EXCEPTION", "details", str(e))
            return f"🚨 [System Error]: {str(e)}"

# =====================================================================
# 🎬 4. 启动入口
# =====================================================================
def main():
    # 注意：启动时的第一个 log 也要进 stderr
    log_debug("SYSTEM", "main", "Nooxus MCP Server Initialized (Version: 0.1.2)")
    mcp.run()

if __name__ == "__main__":
    main()