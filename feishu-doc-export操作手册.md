# feishu-doc-export 操作手册

> 本手册详细说明如何使用 feishu-doc-export 工具批量导出飞书文档为 docx、pdf 或 markdown 格式

---

## 目录

1. [工具介绍](#一工具介绍)
2. [准备工作](#二准备工作)
3. [创建飞书应用](#三创建飞书应用)
4. [配置应用权限](#四配置应用权限)
5. [发布应用版本](#五发布应用版本)
6. [运行导出工具](#六运行导出工具)
7. [导出命令说明](#七导出命令说明)
8. [常见问题](#八常见问题)

---

## 一、工具介绍

### 1.1 工具特点

- **支持多种格式**：docx、markdown、pdf
- **批量导出**：一次导出整个知识库的所有文档
- **保持目录结构**：导出的文档目录结构与飞书知识库一致
- **速度快**：700+文档约25分钟完成
- **后台运行**：不影响正常工作

### 1.2 支持的文档类型

- ✅ 飞书文档（docx）
- ✅ 飞书表格（xlsx）
- ✅ 知识库文档
- ✅ 个人空间文档
- ✅ 图片文件
- ✅ PDF文件

---

## 二、准备工作

### 2.1 所需材料

- 飞书账号（需有企业管理员权限）
- 电脑（Windows/Mac/Linux均可）
- 网络环境正常

### 2.2 工具下载

从 GitHub 下载最新版本：
- 项目地址：https://github.com/xhnbzdl/feishu-doc-export/releases

| 操作系统 | 下载文件 |
|---------|----------|
| Windows | feishu-doc-export-win-x64.zip |
| Mac | feishu-doc-export-mac-osx-x64.zip |
| Linux | feishu-doc-export-linux-x64.zip |

---

## 三、创建飞书应用

### 3.1 进入开发者后台

1. 访问飞书开放平台：https://open.feishu.cn/
2. 点击「开发者后台」
3. 使用飞书账号扫码登录

### 3.2 创建企业自建应用

1. 点击「创建企业自建应用」
2. 填写应用信息：
   - **应用名称**：如「飞书文档导出工具」
   - **应用描述**：如「用于批量导出飞书文档」
3. 点击「创建」

### 3.3 获取应用凭证

1. 进入应用详情页
2. 点击左侧「凭证与基础信息」
3. 记录以下信息：
   - **App ID**：如 `cli_xxxxxxxxxxxxxxxx`
   - **App Secret**：如 `xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

> ⚠️ **重要**：请妥善保管App ID和App Secret！

---

## 四、配置应用权限

### 4.1 进入权限管理

1. 在应用详情页，点击左侧「权限管理」

### 4.2 开通必要权限

在权限管理页面搜索并开通以下权限：

**云文档权限：**
- 查看新版文档
- 查看、评论和下载云空间中所有文件
- 查看、评论和导出文档
- 查看、评论、编辑和管理云空间中所有文件
- 查看、评论、编辑和管理多维表格
- 查看、编辑和管理知识库
- 查看、评论、编辑和管理电子表格
- 导出云文档

**机器人权限：**
- 消息与群组权限

### 4.3 添加机器人能力

1. 点击左侧「添加应用能力」
2. 找到「机器人」卡片，点击「添加」

---

## 五、发布应用版本

### 5.1 创建版本

1. 点击左侧「版本管理与发布」
2. 点击「创建版本」
3. 填写版本信息：
   - **版本号**：如 `1.0.0`
   - **更新说明**：如「初始化版本，开通文档导出权限」
4. 点击「保存」

### 5.2 申请发布

1. 点击「申请线上发布」
2. 等待企业管理员审核

> 💡 **提示**：如果您是企业管理员，可以直接审核通过

### 5.3 为机器人添加知识库权限

1. 在飞书客户端创建一个群组
2. 为群组添加群机器人，选择您创建的应用
3. 打开知识库 → 知识空间设置 → 成员管理 → 添加管理员，选择刚刚创建的群组

---

## 六、运行导出工具

### 6.1 打开命令行

在工具所在目录打开命令行（Windows：cmd或PowerShell）

### 6.2 执行导出命令

#### 基本导出（默认docx格式）

```powershell
.\feishu-doc-export.exe --appId=您的AppId --appSecret=您的AppSecret --exportPath=D:\导出目录
```

#### 导出为Markdown格式

```powershell
.\feishu-doc-export.exe --appId=您的AppId --appSecret=您的AppSecret --saveType=md --exportPath=D:\导出目录
```

#### 导出为PDF格式

```powershell
.\feishu-doc-export.exe --appId=您的AppId --appSecret=您的AppSecret --saveType=pdf --exportPath=D:\导出目录
```

### 6.3 交互式操作

1. 双击运行 `feishu-doc-export.exe`
2. 按照提示输入：
   - App ID
   - App Secret
   - 导出目录
3. 选择要导出的知识库
4. 程序会自动开始导出

---

## 七、导出命令说明

### 7.1 命令参数

| 参数 | 说明 | 是否必填 |
|------|------|---------|
| `--appId` | 飞书自建应用的AppId | 必填 |
| `--appSecret` | 飞书自建应用的AppSecret | 必填 |
| `--exportPath` | 文档导出的目录位置 | 必填 |
| `--spaceId` | 飞书导出的知识库ID | 可选 |
| `--type` | 导出类型：wiki（知识库）或 cloudDoc（个人空间） | 可选，默认wiki |
| `--saveType` | 导出格式：docx、md、pdf | 可选，默认docx |
| `--folderToken` | 个人空间文件夹Token（type=cloudDoc时必填） | 可选 |
| `--quit` | 程序运行结束后自动退出 | 可选 |

### 7.2 示例命令

| 场景 | 命令 |
|------|------|
| 导出知识库为docx | `./feishu-doc-export.exe --appId=xxx --appSecret=xxx --exportPath=D:\导出目录` |
| 导出知识库为markdown | `./feishu-doc-export.exe --appId=xxx --appSecret=xxx --saveType=md --exportPath=D:\导出目录` |
| 导出个人空间文档 | `./feishu-doc-export.exe --appId=xxx --appSecret=xxx --type=cloudDoc --folderToken=xxx --exportPath=D:\导出目录` |
| 自动退出 | `./feishu-doc-export.exe --appId=xxx --appSecret=xxx --exportPath=D:\导出目录 --quit` |

---

## 八、常见问题

### Q1: 提示权限不足怎么办？

**解决方案**：
1. 检查是否开通了所有必要权限
2. 确认机器人已添加为知识库管理员
3. 确认应用版本已发布上线

### Q2: 导出速度很慢怎么办？

**解决方案**：
- 导出为docx格式最快
- 导出为PDF格式最慢（因为图片需要内嵌）
- 确保网络环境稳定

### Q3: Markdown格式丢失怎么办？

**原因**：飞书API导出docx时会丢失部分格式

**解决方案**：
- 推荐使用docx格式导出
- 或使用feishu-backup工具导出Markdown

### Q4: 文件名包含特殊字符导致失败？

**解决方案**：
- 在飞书中修改文件名，移除特殊字符或多余空格
- 或使用批处理脚本重命名文件

### Q5: 如何获取知识库ID？

**方法**：
1. 打开飞书知识库
2. 查看浏览器地址栏
3. URL格式：`https://xxx.feishu.cn/wiki/space/xxxxxxxxxx`
4. 其中 `xxxxxxxxxx` 就是知识库ID

### Q6: 如何获取个人空间文件夹Token？

**方法**：
1. 打开飞书云文档
2. 进入目标文件夹
3. 查看浏览器地址栏
4. URL格式：`https://xxx.feishu.cn/drive/folder/xxxxxxxxxx`
5. 其中 `xxxxxxxxxx` 就是文件夹Token

### Q7: 部分文档无法导出？

**常见原因**：
- OKR文档：不支持API导出
- 文件名包含特殊字符
- 文档权限问题
- 网络超时

**解决方案**：
- 对于OKR文档，手动复制内容
- 重命名问题文件
- 检查文档权限
- 重新运行导出命令

### Q8: 导出的文档目录结构混乱？

**解决方案**：
- 确保飞书知识库的目录结构清晰
- 重新运行导出命令
- 检查导出目录是否有足够权限

---

## 附录

### A. 应用凭证示例

| 配置项 | 值 |
|--------|-----|
| App ID | cli_a915938ac4f8dbcc |
| App Secret | fsYO9Put6HDbPiP70IhVwdguW4M3krcw |

### B. 快速导出命令

```powershell
# 导出为docx
.\feishu-doc-export.exe --appId=cli_a915938ac4f8dbcc --appSecret=fsYO9Put6HDbPiP70IhVwdguW4M3krcw --exportPath=D:\飞书导出文档

# 导出为markdown
.\feishu-doc-export.exe --appId=cli_a915938ac4f8dbcc --appSecret=fsYO9Put6HDbPiP70IhVwdguW4M3krcw --saveType=md --exportPath=D:\飞书导出文档

# 导出为pdf
.\feishu-doc-export.exe --appId=cli_a915938ac4f8dbcc --appSecret=fsYO9Put6HDbPiP70IhVwdguW4M3krcw --saveType=pdf --exportPath=D:\飞书导出文档
```

### C. 注意事项

1. 导出过程中请勿关闭命令行窗口
2. 建议在网络稳定的环境下操作
3. 导出大量文档时，可能需要较长时间，请耐心等待
4. 导出的文档会保存在指定的导出目录中
5. 定期备份导出的文档，以防数据丢失

---

*本手册最后更新：2026年2月26日*
