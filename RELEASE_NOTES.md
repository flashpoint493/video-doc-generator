# 发布说明

## 版本 0.1.0

### 功能特性

- ✅ **视频链接管理**: 支持添加、删除、查询和批量管理视频链接
- ✅ **视频解析**: 调用视频解析 API 提取视频元数据和转录文本
- ✅ **文档生成**: 将视频内容转换为专业的 Markdown 文档
- ✅ **内容分析**: 自动生成视频分析说明和关键要点
- ✅ **命令行工具**: 提供便捷的 CLI 接口
- ✅ **多提供商支持**: 支持多个 API 提供商（当前支持 BigGPT）

### 架构优化

- **提供商模式**: 采用提供商模式设计，便于扩展支持更多 API 提供商
- **模块化设计**: 清晰的模块划分，易于维护和扩展
- **向后兼容**: 保持 API 向后兼容，现有代码无需修改

### 技术栈

- Python 3.8+
- Pydantic 2.0+（数据模型验证）
- Click（命令行接口）
- Requests & aiohttp（HTTP 客户端）

### 发布方式

#### PyPI 发布

1. **使用 Makefile**:
   ```bash
   make publish
   ```

2. **使用 GitHub Actions**:
   - 创建 Release 后自动触发发布
   - 使用 PyPI Trusted Publishing（无需 API Token）

3. **手动发布**:
   ```bash
   python -m build
   python -m twine upload dist/*
   ```

### 下一步

- 支持更多视频解析 API 提供商
- 支持更多文档格式（PDF、Word 等）
- 添加 Web UI 界面
- 支持视频内容搜索功能
