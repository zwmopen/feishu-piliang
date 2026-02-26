# 飞书文档批量导出工具

> 一键批量导出飞书知识库文档为本地文件，支持多种格式

## 项目介绍

本项目提供了一套完整的飞书文档批量导出解决方案，支持将飞书知识库中的文档批量导出为docx、Markdown、PDF等格式，保持原始目录结构，方便本地备份和管理。

## 功能特点

- **多种格式支持**：支持导出为docx、Markdown、PDF格式
- **批量导出**：一次导出整个知识库的所有文档
- **保持目录结构**：导出的文档目录结构与飞书知识库一致
- **速度快**：700+文档约25分钟完成
- **后台运行**：不影响正常工作
- **支持多种文档类型**：飞书文档、表格、知识库文档等

## 工具清单

| 文件名 | 用途 |
|-------|------|
| `feishu-doc-export.exe` | 导出docx/pdf格式文档 |
| `feishu-backup.exe` | 导出Markdown格式文档 |
| `get_cloud_structure.py` | 获取飞书云端文档目录结构 |
| `使用教程.md` | 详细使用教程 |
| `应用凭证配置.md` | 应用凭证配置说明 |
| `feishu-doc-export操作手册.md` | feishu-doc-export工具操作手册 |
| `feishu-doc-export飞书文档批量导出操作手册.md` | 完整操作手册 |
| `飞书知识库文档目录结构.md` | 导出的知识库目录结构 |
| `云端文档目录结构.md` | 云端文档目录结构 |
| `云端文档目录结构.json` | 云端文档目录结构（JSON格式） |

## 快速开始

### 1. 准备工作

- 飞书账号（需有企业管理员权限）
- 电脑（Windows系统）
- 网络环境正常

### 2. 创建飞书应用

1. 访问 [飞书开放平台](https://open.feishu.cn/)
2. 点击「开发者后台」→「创建企业自建应用」
3. 填写应用名称和描述
4. 记录生成的App ID和App Secret

### 3. 配置应用权限

1. 进入应用详情页，点击左侧「权限管理」
2. 批量导入权限配置（参考 `使用教程.md`）
3. 添加机器人能力
4. 发布应用版本

### 4. 执行导出

#### 使用 feishu-doc-export（推荐）

```powershell
# 导出为docx格式
.\feishu-doc-export.exe --appId=您的AppId --appSecret=您的AppSecret --exportPath=D:\导出目录

# 导出为Markdown格式
.\feishu-doc-export.exe --appId=您的AppId --appSecret=您的AppSecret --saveType=md --exportPath=D:\导出目录

# 导出为PDF格式
.\feishu-doc-export.exe --appId=您的AppId --appSecret=您的AppSecret --saveType=pdf --exportPath=D:\导出目录
```

#### 使用 feishu-backup

1. 双击运行 `feishu-backup.exe`
2. 在浏览器中访问 `http://localhost:18900/feishu-backup/`
3. 填写App ID和App Secret
4. 授权并选择要下载的文档

### 5. 获取目录结构

```powershell
python get_cloud_structure.py
```

生成的文件：
- `云端文档目录结构.md`：Markdown格式目录
- `云端文档目录结构.json`：JSON格式原始数据

## 常见问题

### Q1: 提示权限不足怎么办？

- 检查是否开通了所有必要权限
- 确认机器人已添加为知识库管理员
- 确认应用版本已发布上线

### Q2: 导出速度很慢怎么办？

- 导出为docx格式最快
- 导出为PDF格式最慢（因为图片需要内嵌）
- 确保网络环境稳定

### Q3: Markdown格式丢失怎么办？

- 推荐使用docx格式导出
- 或使用feishu-backup工具导出Markdown

### Q4: 文件名包含特殊字符导致失败？

- 在飞书中修改文件名，移除特殊字符或多余空格
- 或使用批处理脚本重命名文件

## 注意事项

1. 导出过程中请勿关闭命令行窗口
2. 建议在网络稳定的环境下操作
3. 导出大量文档时，可能需要较长时间，请耐心等待
4. 导出的文档会保存在指定的导出目录中
5. 定期备份导出的文档，以防数据丢失
6. App ID和App Secret请妥善保管，不要泄露给他人

## 技术支持

如果遇到问题，可以参考以下资源：

- [飞书开放平台文档](https://open.feishu.cn/document)
- [feishu-doc-export项目](https://github.com/xhnbzdl/feishu-doc-export)
- [feishu-backup项目](https://github.com/dicarne/feishu-backup)

## 许可证

本项目仅供个人学习和使用，不得用于商业用途。

---

*最后更新：2026年2月