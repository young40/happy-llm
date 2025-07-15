#!/usr/bin/env python3
"""
基于原始head.jpg改进电子书封面
保持原设计的精髓，但优化为更适合电子书
"""

from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter
import numpy as np

def improve_head_cover():
    try:
        # 读取原始head.jpg (实际上是webp格式)
        original = Image.open("/home/young40/Work/AI/happy-llm/images/head.jpg")
        print(f"原始图片尺寸: {original.size}")
        print(f"原始图片格式: {original.format}")
    except Exception as e:
        print(f"读取原始图片失败: {e}")
        return None
    
    # 创建新的改进版本
    width, height = 1600, 1200  # 电子书标准比例
    
    # 调整原始图片大小并保持比例
    original_resized = original.resize((1600, 900), Image.Resampling.LANCZOS)
    
    # 创建带黑边的画布
    canvas = Image.new('RGB', (width, height), (0, 0, 0))
    
    # 将调整后的图片居中放置
    y_offset = (height - 900) // 2
    canvas.paste(original_resized, (0, y_offset))
    
    # 增强图片
    enhancer = ImageEnhance.Brightness(canvas)
    canvas = enhancer.enhance(1.1)  # 轻微增亮
    
    enhancer = ImageEnhance.Contrast(canvas)
    canvas = enhancer.enhance(1.2)  # 增加对比度
    
    enhancer = ImageEnhance.Color(canvas)
    canvas = enhancer.enhance(1.3)  # 增加饱和度
    
    # 添加渐变叠加层
    overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)
    
    # 从底部到顶部的渐变叠加
    for y in range(height):
        alpha = int(100 * (1 - y/height))  # 底部更暗
        overlay_draw.line([(0, y), (width, y)], fill=(0, 0, 0, alpha))
    
    canvas = Image.alpha_composite(canvas.convert('RGBA'), overlay).convert('RGB')
    
    # 添加文字
    draw = ImageDraw.Draw(canvas)
    
    try:
        # 使用系统字体
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 80)
        subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 36)
        author_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        author_font = ImageFont.load_default()
    
    # 文字内容
    title_text = "Happy-LLM"
    subtitle_text = "从零开始学习大语言模型"
    author_text = "DataWhale 学习社区"
    
    # 计算文本位置（居中）
    title_bbox = draw.textbbox((0, 0), title_text, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    title_height = title_bbox[3] - title_bbox[1]
    
    # 绘制标题（居中在底部区域）
    title_x = (width - title_width) // 2
    title_y = height - 300
    
    # 标题阴影
    draw.text((title_x+3, title_y+3), title_text, fill=(0, 0, 0, 180), font=title_font)
    draw.text((title_x, title_y), title_text, fill=(255, 255, 255), font=title_font)
    
    # 副标题
    subtitle_bbox = draw.textbbox((0, 0), subtitle_text, font=subtitle_font)
    subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
    subtitle_x = (width - subtitle_width) // 2
    subtitle_y = title_y + title_height + 20
    
    draw.text((subtitle_x+2, subtitle_y+2), subtitle_text, fill=(0, 0, 0, 180), font=subtitle_font)
    draw.text((subtitle_x, subtitle_y), subtitle_text, fill=(220, 220, 255), font=subtitle_font)
    
    # 作者
    author_bbox = draw.textbbox((0, 0), author_text, font=author_font)
    author_width = author_bbox[2] - author_bbox[0]
    author_x = (width - author_width) // 2
    author_y = subtitle_y + 50
    
    draw.text((author_x+1, author_y+1), author_text, fill=(0, 0, 0, 180), font=author_font)
    draw.text((author_x, author_y), author_text, fill=(180, 180, 255), font=author_font)
    
    return canvas

def create_variants(original_improved):
    """创建不同尺寸的变体"""
    variants = {}
    
    # 主封面 (1600x1200 - 已创建)
    variants['main'] = original_improved
    
    # EPUB专用 (600x800)
    epub = original_improved.resize((600, 800), Image.Resampling.LANCZOS)
    variants['epub'] = epub
    
    # 缩略图 (300x225)
    thumb = original_improved.resize((300, 225), Image.Resampling.LANCZOS)
    variants['thumb'] = thumb
    
    # Kindle封面 (800x1280)
    kindle = original_improved.resize((800, 1280), Image.Resampling.LANCZOS)
    variants['kindle'] = kindle
    
    return variants

if __name__ == "__main__":
    print("🎨 基于原始head.jpg创建改进版封面...")
    
    # 创建改进版
    improved = improve_head_cover()
    
    if improved:
        # 创建不同尺寸的变体
        variants = create_variants(improved)
        
        # 保存所有版本
        improved.save("/home/young40/Work/AI/happy-llm/images/head-improved.jpg", "JPEG", quality=95)
        variants['epub'].save("/home/young40/Work/AI/happy-llm/docs/images/epub-cover-head.jpg", "JPEG", quality=95)
        variants['thumb'].save("/home/young40/Work/AI/happy-llm/docs/images/epub-cover-head-thumb.jpg", "JPEG", quality=90)
        variants['kindle'].save("/home/young40/Work/AI/happy-llm/docs/images/kindle-cover-head.jpg", "JPEG", quality=95)
        
        print("✅ 基于head.jpg的改进版封面已创建完成!")
        print("📁 文件:")
        print("   🖼️  images/head-improved.jpg (改进版，基于原图)")
        print("   📱 docs/images/epub-cover-head.jpg (EPUB专用)")
        print("   📱 docs/images/kindle-cover-head.jpg (Kindle专用)")
        print("   🖼️  docs/images/epub-cover-head-thumb.jpg (缩略图)")
    else:
        print("❌ 创建失败")