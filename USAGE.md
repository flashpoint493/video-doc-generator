# 使用指南

## 安装

```bash
pip install video-doc-generator
```

## 命令行使用

### 查看帮助

```bash
video-doc --help
```

### 视频链接管理

#### 添加视频链接

```bash
video-doc add "https://www.youtube.com/watch?v=example" --title "示例视频"
```

#### 列出所有视频

```bash
video-doc list
```

输出示例：
```
共 2 个视频:

1. 示例视频
   URL: https://www.youtube.com/watch?v=example
   平台: youtube

2. B站视频示例
   URL: https://www.bilibili.com/video/BV123456
   平台: bilibili
```

#### 删除视频链接

```bash
video-doc remove "https://www.youtube.com/watch?v=example"
```

### 视频解析和文档生成

#### 解析单个视频

```bash
# 使用环境变量中的 API Key
export VIDEO_PARSER_API_KEY="your-bigpt-api-key"
video-doc parse "https://www.youtube.com/watch?v=example" --output-dir docs

# 或使用命令行参数
video-doc parse "https://www.youtube.com/watch?v=example" \
    --api-key "your-bigpt-api-key" \
    --output-dir docs
```

#### 批量处理视频

```bash
# 处理所有已添加的视频
video-doc process-all --output-dir docs --api-key "your-bigpt-api-key"
```

### CLI 命令完整列表

| 命令 | 说明 | 示例 |
|------|------|------|
| `video-doc add <url>` | 添加视频链接 | `video-doc add "https://youtube.com/watch?v=xxx" --title "标题"` |
| `video-doc remove <url>` | 删除视频链接 | `video-doc remove "https://youtube.com/watch?v=xxx"` |
| `video-doc list` | 列出所有视频 | `video-doc list` |
| `video-doc parse <url>` | 解析视频并生成文档 | `video-doc parse "https://youtube.com/watch?v=xxx" --output-dir docs` |
| `video-doc process-all` | 批量处理所有视频 | `video-doc process-all --output-dir docs` |

### CLI 选项

#### `parse` 命令选项

- `--output-dir`: 输出目录（默认: `docs`）
- `--api-key`: API 密钥（也可通过环境变量 `VIDEO_PARSER_API_KEY` 设置）
- `--api-url`: API 地址（可选，默认使用 BigGPT API）
- `--use-get`: 使用 GET 方法（默认启用，BigGPT 推荐）

#### `process-all` 命令选项

- `--output-dir`: 输出目录（默认: `docs`）
- `--api-key`: API 密钥（也可通过环境变量 `VIDEO_PARSER_API_KEY` 设置）
- `--api-url`: API 地址（可选，默认使用 BigGPT API）
- `--use-get`: 使用 GET 方法（默认启用，BigGPT 推荐）

## Python API 使用

### 基本示例

```python
from video_doc_generator import VideoManager, VideoParser, DocumentGenerator

# 1. 管理视频链接
manager = VideoManager()
video = manager.add("https://www.youtube.com/watch?v=example", title="示例视频")
print(f"已添加: {video.title}, 平台: {video.platform}")

# 2. 解析视频
parser = VideoParser(api_key="your-bigpt-api-key", use_get_method=True)
result = parser.parse("https://www.youtube.com/watch?v=example")
print(f"标题: {result.metadata.title}")
print(f"平台: {result.metadata.platform}")

# 3. 生成文档
generator = DocumentGenerator(output_dir="docs")
filepath = generator.generate_markdown(result)
print(f"文档已生成: {filepath}")
```

### 批量处理

```python
from video_doc_generator import VideoManager, VideoParser, DocumentGenerator

manager = VideoManager()
parser = VideoParser(api_key="your-bigpt-api-key", use_get_method=True)
generator = DocumentGenerator(output_dir="docs")

# 处理所有视频
for video in manager.list_all():
    try:
        result = parser.parse(str(video.url))
        filepath = generator.generate_markdown(result)
        print(f"✓ {video.title}: {filepath}")
    except Exception as e:
        print(f"✗ {video.title}: {e}")
```

### 异步处理

```python
import asyncio
from video_doc_generator import VideoParser

async def parse_videos(urls):
    parser = VideoParser(api_key="your-bigpt-api-key", use_get_method=True)
    tasks = [parser.parse_async(url) for url in urls]
    results = await asyncio.gather(*tasks)
    return results

urls = [
    "https://www.youtube.com/watch?v=xxxxxxxxxxx",
    "https://www.bilibili.com/video/BVxxxxxxxxxx",
]
results = asyncio.run(parse_videos(urls))
```

## 支持的视频平台

- ✅ YouTube
- ✅ Bilibili
- ✅ TikTok
- ✅ Vimeo
- ✅ 其他 BigGPT API 支持的平台

## 常见问题

### Q: 如何获取 API Key？

A: 访问 [BigGPT](https://bibigpt.co) 注册账号并获取 API Token。

### Q: 使用哪个 API 方法？

A: 推荐使用 GET 方法（`--use-get`），免费且稳定。这是默认选项。

### Q: 生成的文档在哪里？

A: 默认保存在当前目录下的 `docs` 文件夹中。可以通过 `--output-dir` 选项自定义。

### Q: 视频链接存储在哪里？

A: 存储在 `~/.video_doc_generator/videos.json`。可以通过 `VideoManager(storage_path="custom/path.json")` 自定义路径。

### Q: 支持哪些文档格式？

A: 当前版本支持 Markdown 格式。未来版本将支持 PDF、Word 等格式。

## 更多示例

查看 `examples/` 目录下的示例代码。
