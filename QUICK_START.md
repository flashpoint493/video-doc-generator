# 快速开始指南

## Video Doc Generator - 视频转文档生成器

### 项目概述

Video Doc Generator 是一个能够管理视频链接，调用视频解析 API 读取和解析视频，并将视频内容转换为专业文档和分析说明的 Python 包。

### 核心功能

1. **视频链接管理** (`VideoManager`)
   - 添加、删除、查询视频链接
   - 自动检测视频平台（YouTube、Bilibili、Vimeo 等）
   - 持久化存储到本地 JSON 文件

2. **视频解析** (`VideoParser`)
   - 调用视频解析 API 获取视频元数据
   - 提取视频转录文本
   - 支持同步和异步解析

3. **文档生成** (`DocumentGenerator`)
   - 将视频内容转换为 Markdown 文档
   - 自动生成内容分析和关键要点
   - 支持自定义输出目录

### 安装

```bash
# 从源码安装
git clone https://github.com/flashpoint493/video-doc-generator.git
cd video-doc-generator
pip install -e ".[dev]"
```

### 快速使用

#### 1. Python 代码使用

```python
from video_doc_generator import VideoManager, VideoParser, DocumentGenerator

# 管理视频链接
manager = VideoManager()
manager.add("https://www.youtube.com/watch?v=example", title="示例视频")

# 解析视频（需要配置 API）
parser = VideoParser(api_key="your-api-key", api_url="https://api.example.com/video/parse")
result = parser.parse("https://www.youtube.com/watch?v=example")

# 生成文档
generator = DocumentGenerator(output_dir="docs")
filepath = generator.generate_markdown(result)
```

#### 2. 命令行使用

```bash
# 添加视频链接
video-doc add "https://www.youtube.com/watch?v=example" --title "示例视频"

# 列出所有视频
video-doc list

# 解析视频并生成文档
video-doc parse "https://www.youtube.com/watch?v=example" --output-dir docs

# 处理所有已添加的视频
video-doc process-all --output-dir docs
```

### 配置

#### 环境变量

创建 `.env` 文件：

```env
VIDEO_PARSER_API_KEY=your-api-key
VIDEO_PARSER_API_URL=https://api.example.com/video/parse
```

#### 命令行参数

```bash
# 使用环境变量
export VIDEO_PARSER_API_KEY="your-api-key"
export VIDEO_PARSER_API_URL="https://api.example.com/video/parse"

# 或使用命令行参数
video-doc parse "https://www.youtube.com/watch?v=example" \
    --api-key "your-api-key" \
    --api-url "https://api.example.com/video/parse"
```

### 项目结构

```
video-doc-generator/
├── src/
│   └── video_doc_generator/
│       ├── __init__.py          # 包初始化
│       ├── manager.py           # 视频链接管理
│       ├── parser.py            # 视频解析
│       ├── generator.py         # 文档生成
│       ├── cli.py               # 命令行接口
│       └── config.py            # 配置管理
├── tests/                       # 测试文件
├── examples/                    # 使用示例
├── docs/                        # 生成的文档
├── pyproject.toml               # 项目配置
└── README.md                    # 项目说明
```

### 开发

```bash
# 安装开发依赖
pip install -e ".[dev]"

# 运行测试
pytest

# 代码格式化
ruff format .

# 代码检查
ruff check .

# 类型检查
mypy .
```

### 下一步

1. 配置视频解析 API（需要实际的 API 服务）
2. 添加更多视频平台支持
3. 扩展文档格式支持（PDF、Word 等）
4. 添加 AI 增强的内容分析

### 相关文档

- [README.md](./README.md) - 完整项目文档
- [PROJECT_IDEA.md](./PROJECT_IDEA.md) - 项目规划和想法
- [CONTRIBUTING.md](./CONTRIBUTING.md) - 贡献指南
