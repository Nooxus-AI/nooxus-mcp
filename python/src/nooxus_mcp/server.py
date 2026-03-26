import os
import urllib.parse
import httpx
from mcp.server.fastmcp import FastMCP

# 初始化一个名为 "Nooxus Search Edge" 的官方服务器
mcp = FastMCP("Nooxus Search Edge")

# 🎁 内置的全球公测体验 Token (Dev Tier)
# 限制: 30 RPM, 1000 Quota (在 Cloudflare D1 控制台配置好状态)
DEFAULT_TRIAL_KEY = "nx_sk_test_cc5081ef8a9f29a6_eee9"

@mcp.tool()
async def search_manufacturing_entities(query: str) -> str:
    """
    Search for global manufacturing and supply chain entities, including CNC, Assembly, and international standards.
    Args:
        query: The search keyword supporting FTS5 syntax (e.g., 'CNC AND Assembly' or 'ISO*').
    """
    # 🛡️ 智能鉴权：优先读取客户自己的高优密钥，如果没有，平滑降级到免费体验版
    api_key = os.environ.get("NOOXUS_API_KEY", DEFAULT_TRIAL_KEY)
    
    # 在控制台打个极其低调的日志，方便用户排查自己配没配成功
    is_trial = "Trial Mode" if api_key == DEFAULT_TRIAL_KEY else "Pro Mode"
    print(f"  [Nooxus Edge] Querying '{query}' using {is_trial}...", flush=True)

    headers = {"Authorization": f"Bearer {api_key}"}
    safe_query = urllib.parse.quote(query)
    url = f"https://mcp.nooxus.com/v1/search?q={safe_query}"
    
    async with httpx.AsyncClient() as client:
        try:
            # 向您的边缘节点发起请求
            response = await client.get(url, headers=headers, timeout=15.0)
            
            # 💡 优雅的业务报错：如果体验卡被全球白嫖党刷爆了，提醒他们去买
            if response.status_code == 402:
                 return "🚨 [Nooxus Auth Error]: The global trial quota has been exhausted. Please purchase your dedicated API Key at https://SmartGSC.com and set the NOOXUS_API_KEY environment variable."
            elif response.status_code == 401:
                 return "🚨 [Nooxus Auth Error]: Invalid API Key. Please check your NOOXUS_API_KEY environment variable."
            
            response.raise_for_status()
            return response.text 
            
        except httpx.HTTPStatusError as e:
            return f"🚨 [Nooxus Gateway Error]: HTTP {e.response.status_code} - Please check your API Key status."
        except Exception as e:
            return f"🚨 [Network Error]: Failed to reach Nooxus Edge - {str(e)}"

def main():
    # 启动 MCP 标准输入输出流
    mcp.run()

if __name__ == "__main__":
    main()