# =====================================================================
# 📝 CHANGELOG (更新日志)
# - 2026-04-03 (v0.2.0): [语义与双轨架构升级] 
#   1. 适配 Worker v5.3，全面支持 16位(Root)与 32位(Leaf) 双轨 NOO-ID 解析。
#   2. 解除文本检索限制，全面拥抱语义向量 (Vectorize)，优化 AI 检索 Prompt。
#   3. 工具函数重命名以匹配全局全息寻址架构。
# - 2026-03-30 (v0.1.5): [深度调试版] 强制开启本地文件日志，植入 HTTP_PAYLOAD 探针。
# =====================================================================

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
DEBUG_MODE = os.environ.get("NOOXUS_DEBUG", "true").lower() == "true"

logger = logging.getLogger("NooxusFlow")
logger.setLevel(logging.DEBUG)
logger.handlers = []

if DEBUG_MODE:
    CURRENT_DIR = Path(__file__).parent.absolute()
    LOG_FILE = CURRENT_DIR / "mcp-logs.txt"
    file_handler = logging.FileHandler(LOG_FILE, encoding='utf-8')
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
else:
    stderr_handler = logging.StreamHandler(sys.stderr)
    stderr_handler.setFormatter(logging.Formatter('[%(levelname)s] %(message)s'))
    logger.addHandler(stderr_handler)

def log_debug(tag, tool, message, detail=None):
    """统一日志入口，带有防崩溃的安全 JSON 序列化"""
    entry = {
        "tag": tag,
        "tool": tool,
        "msg": message,
    }
    if detail:
        entry["detail"] = detail
        
    log_msg = json.dumps(entry, ensure_ascii=False)
    
    if DEBUG_MODE:
        logger.info(log_msg)
    else:
        print(f"[{tag}] {message}", file=sys.stderr, flush=True)

# =====================================================================
# 🚀 2. MCP 服务器初始化与鉴权
# =====================================================================
mcp = FastMCP("Nooxus Vector Edge")
DEFAULT_TRIAL_KEY = "nx_sk_test_cc5081ef8a9f29a6_eee9"

def get_headers():
    api_key = os.environ.get("NOOXUS_API_KEY", DEFAULT_TRIAL_KEY)
    return {
        "Authorization": f"Bearer {api_key}", 
        "Content-Type": "application/json",
        "User-Agent": "Nooxus-MCP-Client/2.0-Vector"
    }

# =====================================================================
# 🔍 3. 工具集：全息数据管道 (Vector & Routing)
# =====================================================================
@mcp.tool()
async def semantic_search_nooxus(query: str) -> str:
    """
    通过语义向量检索全球供应链实体与产品库 (Nooxus Vector Network)。
    ⚠️ [核心系统指令 - 必须遵守]: 
    底层已升级为高维向量检索 (BGE-Base)。请提供包含具体工程参数、材质或工艺的【语义短语】。
    例如，不要只搜 "Motor"，应该搜 "12V DC lumbar support motor IP54" 或 "Ford Bronco 压铸件平替"。
    云端将自动返回带有 semantic_score 和 tier (ROOT/LEAF) 的节点列表。
    """
    log_debug("REQ_START", "search", f"Semantic Query: {query}")
    
    headers = get_headers()
    safe_query = urllib.parse.quote(query)
    url = f"https://mcp.nooxus.com/v1/search?q={safe_query}"
    
    log_debug("HTTP_SEND", "search", f"Requesting URL: {url}")
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=15.0)
            log_debug("HTTP_RECV", "search", f"Status Code: {response.status_code}")
            
            if response.status_code == 402:
                return "🚨 [Quota Error]: 全局查询额度已耗尽，请补充 API Key。"
            elif response.status_code != 200:
                log_debug("HTTP_ERROR_PAYLOAD", "search", "Non-200 Response", detail=response.text)
                return f"🚨 [Semantic Search Error {response.status_code}]"
            
            # 探针注入：全量打印包含语义分值的 JSON 报文
            log_debug("HTTP_PAYLOAD", "search", "Success Response Payload", detail=response.text)
            return response.text
            
        except Exception as e:
            log_debug("EXCEPTION", "search", str(e))
            return f"🚨 [Network Error]: {str(e)}"

@mcp.tool()
async def get_nooxus_node(noo_id: str) -> str:
    """
    通过 NOO-ID 精确抓取目标的全息数据节点 (JSON/JSON5 格式)。
    支持双轨解析：
    1. 16位 Base36 (如 NOO-3J5E3OYMRMYXMVSJ): 返回企业/经营主体档案。
    2. 32位 Base36 (如 NOO-ZVQ77MBSCABGALW7A9Y8X7W6V5U4T3R): 返回具体产品/研发能力的数字孢子。
    """
    clean_id = noo_id.strip().upper()
    log_debug("REQ_START", "get_node", f"Target ID: {clean_id}")
    
    headers = get_headers()
    url = f"https://mcp.nooxus.com/noo/{urllib.parse.quote(clean_id)}"
    
    log_debug("HTTP_SEND", "get_node", f"Requesting URL: {url}")
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=15.0)
            log_debug("HTTP_RECV", "get_node", f"Status Code: {response.status_code}")
            
            if response.status_code != 200:
                log_debug("HTTP_ERROR_PAYLOAD", "get_node", "Non-200 Response", detail=response.text)
                return f"🚨 [Node Retrieval Error {response.status_code}]"
            
            # 探针注入：全量截获带协议指令的 NOO 孢子数据
            log_debug("HTTP_PAYLOAD", "get_node", "Success Response Payload", detail=response.text)
            return response.text
            
        except Exception as e:
            log_debug("EXCEPTION", "get_node", str(e))
            return f"🚨 [System Error]: {str(e)}"

# =====================================================================
# 🎬 4. 启动入口
# =====================================================================
def main():
    log_debug("SYSTEM", "main", "Nooxus MCP Server Initialized (Version: 0.2.0 - Vector & Dual-Track Edition)")
    mcp.run()

if __name__ == "__main__":
    main()