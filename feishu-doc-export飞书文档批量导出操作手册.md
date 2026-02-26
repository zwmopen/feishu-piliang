# 飞书文档批量导出操作手册

> 本手册详细说明如何批量导出飞书知识库文档到本地

---

## 目录

1. [准备工作](#一准备工作)
2. [创建飞书应用](#二创建飞书应用)
3. [配置应用权限](#三配置应用权限)
4. [发布应用版本](#四发布应用版本)
5. [下载并运行导出工具](#五下载并运行导出工具)
6. [配置重定向URL](#六配置重定向url)
7. [授权并下载文档](#七授权并下载文档)
8. [常见问题](#八常见问题)

---

## 一、准备工作

### 1.1 所需材料

- 飞书账号（需有企业管理员权限）
- 电脑（Windows/Mac/Linux均可）
- 网络环境正常

### 1.2 工具下载

从以下地址下载最新版本的工具：

| 工具名称 | 下载地址 | 用途 |
|---------|---------|------|
| feishu-backup | https://github.com/dicarne/feishu-backup/releases | 导出Markdown格式文档 |
| feishu-doc-export | https://github.com/xhnbzdl/feishu-doc-export/releases | 导出docx/pdf格式文档 |

---

## 二、创建飞书应用

### 2.1 进入开发者后台

1. 访问飞书开放平台：https://open.feishu.cn/
2. 点击右上角「开发者后台」
3. 使用飞书账号扫码登录

### 2.2 创建企业自建应用

1. 点击「创建企业自建应用」
2. 填写应用信息：
   - **应用名称**：随意填写（如：飞书文档导出工具）
   - **应用描述**：随意填写
   - **应用图标**：可选
3. 点击「创建」

### 2.3 获取应用凭证

1. 进入应用详情页
2. 点击左侧「凭证与基础信息」
3. 记录以下信息：
   - **App ID**：如 `cli_xxxxxxxxxxxxxxxx`
   - **App Secret**：如 `xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

> ⚠️ **重要**：请妥善保管App ID和App Secret，不要泄露给他人！

---

## 三、配置应用权限

### 3.1 进入权限管理

1. 在应用详情页，点击左侧「权限管理」
2. 确保切换到正确的权限范围（租户/用户）

### 3.2 开通必要权限

#### 方式一：手动开通

在权限管理页面搜索并开通以下权限：

**云空间权限（必须）：**
| 权限名称 | 权限标识 | 范围 |
|---------|---------|------|
| 查看、评论、编辑和管理云空间中所有文件 | `drive:drive` | 租户+用户 |
| 查看、评论和下载云空间中所有文件 | `drive:drive:readonly` | 租户+用户 |
| 查看和下载云空间中的文件 | `drive:file:readonly` | 租户+用户 |

**知识库权限（必须）：**
| 权限名称 | 权限标识 | 范围 |
|---------|---------|------|
| 查看、编辑和管理知识库 | `wiki:wiki` | 租户+用户 |
| 查看知识库 | `wiki:wiki:readonly` | 租户+用户 |

**文档权限：**
| 权限名称 | 权限标识 | 范围 |
|---------|---------|------|
| 查看新版文档 | `docx:document:readonly` | 租户+用户 |
| 导出云文档 | `docs:document:export` | 租户+用户 |
| 下载文档中的媒体文件 | `docs:document.media:download` | 租户+用户 |

**用户信息权限：**
| 权限名称 | 权限标识 | 范围 |
|---------|---------|------|
| 获取用户基本信息 | `contact:user.base:readonly` | 租户+用户 |

#### 方式二：批量导入

1. 点击「批量导入/导出权限」按钮
2. 选择「导入权限」
3. 粘贴以下JSON内容：

```json
{
  "scopes": {
    "tenant": [
      "drive:drive",
      "drive:drive:readonly",
      "drive:file:readonly",
      "wiki:wiki",
      "wiki:wiki:readonly",
      "docx:document:readonly",
      "docs:document:export",
      "docs:document.media:download",
      "contact:user.base:readonly"
    ],
    "user": [
      "drive:drive",
      "drive:drive:readonly",
      "drive:file:readonly",
      "wiki:wiki",
      "wiki:wiki:readonly",
      "docx:document:readonly",
      "docs:document:export",
      "docs:document.media:download",
      "contact:user.base:readonly"
    ]
  }
}
```

4. 点击确认

### 3.3 添加机器人能力

1. 点击左侧「添加应用能力」
2. 找到「机器人」卡片，点击「添加」

---

## 四、发布应用版本

### 4.1 创建版本

1. 点击左侧「版本管理与发布」
2. 点击「创建版本」
3. 填写版本信息：
   - **版本号**：如 `1.0.0`
   - **更新说明**：如「初始化版本，开通文档导出权限」
4. 点击「保存」

### 4.2 申请发布

1. 点击「申请线上发布」
2. 等待企业管理员审核

> 💡 **提示**：如果您是企业管理员，可以直接审核通过

### 4.3 确认发布状态

发布成功后，应用状态会显示为「已上线」

---

## 五、下载并运行导出工具

### 5.1 下载工具

根据您的操作系统下载对应版本：

| 操作系统 | 文件名 |
|---------|--------|
| Windows | `feishu-backup.exe` |
| Mac | `feishu-backup` |
| Linux | `feishu-backup` |

### 5.2 运行工具

#### Windows系统

1. 双击运行 `feishu-backup.exe`
2. 或在命令行中运行：
   ```powershell
   .\feishu-backup.exe
   ```

#### Mac/Linux系统

1. 添加执行权限：
   ```bash
   chmod +x feishu-backup
   ```
2. 运行程序：
   ```bash
   ./feishu-backup
   ```

### 5.3 确认程序启动

程序启动后会显示类似以下信息：

```
[GIN-debug] Listening and serving HTTP on 0.0.0.0:18900
```

这表示程序正在监听端口 **18900**

---

## 六、配置重定向URL

### 6.1 打开配置页面

在浏览器中访问：
```
http://localhost:18900/feishu-backup/
```

### 6.2 填写应用凭证

1. 在页面中填写：
   - **App ID**：您的应用App ID
   - **App Secret**：您的应用App Secret
2. 点击「计算」按钮

### 6.3 添加重定向URL

1. 复制生成的重定向URL（格式类似：`http://localhost:18900/feishu-backup/#/backup/...`）
2. 返回飞书开发者后台
3. 进入「安全设置」→「重定向URL」
4. 点击「添加重定向URL」
5. 粘贴刚才复制的URL
6. 点击「保存」

---

## 七、授权并下载文档

### 7.1 进行授权

1. 在配置页面点击「完成」按钮
2. 系统会自动跳转到飞书授权页面
3. 点击「同意授权」

### 7.2 选择下载内容

授权成功后，页面会显示两个选项：

#### 选项一：下载云空间文档

1. 点击「备份下载云空间文档」
2. 选择要下载的文件
3. 点击「下载选中文件」或「下载所有文件」

#### 选项二：下载知识库文档

1. 点击「下载知识库文档」
2. 选择要下载的知识库
3. 可以选择下载整个知识库或部分页面
4. 点击「下载」

### 7.3 等待下载完成

- 下载过程中请保持程序运行
- 不要关闭浏览器和命令行窗口
- 下载完成后，文件会保存在浏览器默认下载目录

---

## 八、常见问题

### Q1: 提示「权限不足」怎么办？

**原因**：应用权限未开通或未生效

**解决方案**：
1. 检查权限管理中是否开通了所有必要权限
2. 确认权限范围包含「租户」和「用户」
3. 确认应用版本已发布上线
4. 重新进行授权

### Q2: API返回400错误怎么办？

**原因**：缺少关键权限

**解决方案**：
1. 确保开通了 `drive:drive:readonly` 权限
2. 确保开通了 `wiki:wiki:readonly` 权限
3. 发布新版本后重新授权

### Q3: 下载速度很慢怎么办？

**原因**：网络环境或飞书服务器响应慢

**解决方案**：
1. 检查网络连接
2. 尝试分批次下载
3. 避开网络高峰期

### Q4: 部分文档无法下载？

**原因**：文档类型不支持或权限不足

**解决方案**：
- 多维表格（Bitable）：暂不支持，需手动导出
- 电子表格（Sheet）：暂不支持，需手动导出
- OKR文档：不支持API导出

### Q5: 如何导出docx或pdf格式？

使用 `feishu-doc-export` 工具：

```powershell
.\feishu-doc-export.exe --appId=您的AppId --appSecret=您的AppSecret --saveType=docx --exportPath=D:\导出目录
```

参数说明：
- `--saveType=docx`：导出为docx格式
- `--saveType=md`：导出为Markdown格式
- `--saveType=pdf`：导出为PDF格式

### Q6: 如何获取云端文档目录结构？

运行Python脚本获取：

```powershell
python get_cloud_structure.py
```

生成的文件：
- `云端文档目录结构.md`：Markdown格式目录
- `云端文档目录结构.json`：JSON格式原始数据

---

## 附录

### A. 权限对照表

| 功能 | 所需权限 |
|-----|---------|
| 查看知识库列表 | `wiki:wiki:readonly` |
| 下载知识库文档 | `wiki:wiki` + `docs:document:export` |
| 查看云空间文件 | `drive:drive:readonly` |
| 下载云空间文件 | `drive:drive` + `docs:document:export` |
| 下载文档图片 | `docs:document.media:download` |

### B. 相关链接

- 飞书开放平台：https://open.feishu.cn/
- feishu-backup项目：https://github.com/dicarne/feishu-backup
- feishu-doc-export项目：https://github.com/xhnbzdl/feishu-doc-export

### C. 文件清单

```
飞书批量导出/
├── feishu-backup.exe              # 导出工具（Markdown格式）
├── feishu-doc-export.exe          # 导出工具（docx/pdf格式）
├── feishu_backup_permissions.json # 权限配置文件
├── get_cloud_structure.py         # 获取目录结构脚本
├── 应用凭证配置.md                 # 应用凭证记录
├── 使用教程.md                     # 使用教程
└── 飞书文档批量导出操作手册.md      # 本手册
```

---

*本手册最后更新：2026年2月26日*
