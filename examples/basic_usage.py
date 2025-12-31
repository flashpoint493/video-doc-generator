"""
基本使用示例

演示如何使用 Video Doc Generator 的基本功能。
"""

from video_doc_generator import DocumentGenerator, VideoManager, VideoParser


def main():
    """基本使用示例"""
    # 1. 管理视频链接
    print("=== 视频链接管理 ===")
    manager = VideoManager()
    manager.add("https://www.youtube.com/watch?v=example", title="示例视频")
    manager.add("https://www.bilibili.com/video/BV123456", title="B站视频示例")
    print(f"已添加 {manager.count()} 个视频")

    # 列出所有视频
    videos = manager.list_all()
    for video in videos:
        print(f"  - {video.title}: {video.url} ({video.platform})")

    # 2. 解析视频（需要配置 API）
    print("\n=== 视频解析 ===")
    parser = VideoParser(
        api_key="your-api-key",  # 替换为实际的 API 密钥
        api_url="https://api.example.com/video/parse",  # 替换为实际的 API 地址
    )

    # 注意：这里需要实际的视频解析 API
    # result = parser.parse("https://www.youtube.com/watch?v=example")
    # print(f"解析成功: {result.metadata.title}")

    # 3. 生成文档
    print("\n=== 文档生成 ===")
    generator = DocumentGenerator(output_dir="docs")
    print("文档生成器已初始化，输出目录: docs")

    # 注意：需要先解析视频才能生成文档
    # filepath = generator.generate_markdown(result)
    # print(f"文档已生成: {filepath}")


if __name__ == "__main__":
    main()
