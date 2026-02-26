"""
获取飞书云端文档目录结构
"""
import requests
import json
import time

APP_ID = "cli_a915938ac4f8dbcc"
APP_SECRET = "fsYO9Put6HDbPiP70IhVwdguW4M3krcw"
BASE_URL = "http://localhost:18900/api/feishu"

def get_tenant_access_token():
    """获取tenant_access_token"""
    url = f"{BASE_URL}/auth/v3/tenant_access_token/internal/"
    payload = {
        "app_id": APP_ID,
        "app_secret": APP_SECRET
    }
    response = requests.post(url, json=payload)
    result = response.json()
    if result.get("code") == 0:
        return result.get("tenant_access_token")
    else:
        print(f"获取token失败: {result}")
        return None

def get_wiki_spaces(token):
    """获取知识库列表"""
    url = f"{BASE_URL}/wiki/v2/spaces?page_size=50"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    result = response.json()
    if result.get("code") == 0:
        return result.get("data", {}).get("items", [])
    else:
        print(f"获取知识库列表失败: {result}")
        return []

def get_wiki_nodes(token, space_id, parent_node_token=None, page_token=None):
    """获取知识库节点列表"""
    url = f"{BASE_URL}/wiki/v2/spaces/{space_id}/nodes?parent_node_token={parent_node_token or ''}&page_size=50"
    if page_token:
        url += f"&page_token={page_token}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    result = response.json()
    if result.get("code") == 0:
        return result.get("data", {})
    else:
        print(f"获取知识库节点失败: {result}")
        return {}

def get_node_info(token, token_id, obj_type):
    """获取节点详细信息"""
    url = f"{BASE_URL}/wiki/v2/nodes/info?token={token_id}&obj_type={obj_type}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    result = response.json()
    if result.get("code") == 0:
        return result.get("data", {}).get("node", {})
    else:
        return {}

def build_tree(token, space_id, parent_node_token=None, depth=0, max_depth=10):
    """递归构建文档树"""
    if depth > max_depth:
        return []
    
    nodes = []
    page_token = None
    
    while True:
        data = get_wiki_nodes(token, space_id, parent_node_token, page_token)
        items = data.get("items", [])
        
        for item in items:
            node_info = {
                "title": item.get("title", "未命名"),
                "obj_type": item.get("obj_type", ""),
                "node_token": item.get("node_token", ""),
                "has_child": item.get("has_child", False)
            }
            
            # 如果有子节点，递归获取
            if item.get("has_child"):
                children = build_tree(token, space_id, item.get("node_token"), depth + 1, max_depth)
                node_info["children"] = children
            
            nodes.append(node_info)
        
        page_token = data.get("page_token")
        if not page_token:
            break
    
    return nodes

def generate_markdown(nodes, depth=0):
    """生成Markdown格式的目录"""
    md = ""
    indent = "  " * depth
    
    for node in nodes:
        icon = "📁" if node.get("has_child") or node.get("children") else "📄"
        md += f"{indent}- {icon} {node['title']}\n"
        
        if node.get("children"):
            md += generate_markdown(node["children"], depth + 1)
    
    return md

def main():
    print("正在获取飞书云端文档目录结构...")
    
    # 获取token
    token = get_tenant_access_token()
    if not token:
        print("获取token失败，请检查应用配置")
        return
    
    print(f"Token获取成功")
    
    # 获取知识库列表
    spaces = get_wiki_spaces(token)
    print(f"找到 {len(spaces)} 个知识库")
    
    result = {
        "spaces": [],
        "generated_at": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    
    all_markdown = f"# 飞书云端文档目录结构\n\n> 生成时间：{time.strftime('%Y-%m-%d %H:%M:%S')}\n\n---\n\n"
    
    for space in spaces:
        space_name = space.get("name", "未命名知识库")
        space_id = space.get("space_id", "")
        
        print(f"\n正在处理知识库: {space_name}")
        
        space_info = {
            "name": space_name,
            "space_id": space_id,
            "nodes": []
        }
        
        # 获取知识库节点树
        nodes = build_tree(token, space_id)
        space_info["nodes"] = nodes
        
        result["spaces"].append(space_info)
        
        # 生成Markdown
        all_markdown += f"## {space_name}\n\n"
        all_markdown += generate_markdown(nodes)
        all_markdown += "\n---\n\n"
    
    # 保存JSON结果
    with open("云端文档目录结构.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    # 保存Markdown结果
    with open("云端文档目录结构.md", "w", encoding="utf-8") as f:
        f.write(all_markdown)
    
    print("\n目录结构已保存到:")
    print("- 云端文档目录结构.json")
    print("- 云端文档目录结构.md")

if __name__ == "__main__":
    main()
