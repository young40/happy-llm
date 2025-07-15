#!/usr/bin/env python3
"""创建专业电子书封面图片 - Happy-LLM"""

from PIL import Image, ImageDraw, ImageFont
import numpy as np

def create_professional_cover():
    # 创建高分辨率封面 (1600x1200 适合电子书)
    width, height = 1600, 1200
    
    # 创建渐变背景
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    
    # 创建现代渐变背景从深蓝到紫色
    for y in range(height):
        # 渐变从深蓝 (#0a0a2e) 到紫色 (#4a148c)
        r = int(10 + (74 - 10) * y / height)
        g = int(10 + (20 - 10) * y / height)
        b = int(46 + (140 - 46) * y / height)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    # 添加神经网络图案覆盖层
    overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)
    
    # 绘制神经网络节点和连接
    np.random.seed(42)
    nodes = []
    for _ in range(200):
        x = np.random.randint(100, width-100)
        y = np.random.randint(100, height-100)
        nodes.append((x, y))
        # 小圆点作为节点
        size = np.random.randint(1, 3)
        overlay_draw.ellipse([x-size, y-size, x+size, y+size], fill=(255, 255, 255, 40))
    
    # 绘制一些连接
    for i in range(min(150, len(nodes))):
        for j in range(i+1, min(i+2, len(nodes))):
            x1, y1 = nodes[i]
            x2, y2 = nodes[j]
            distance = np.sqrt((x1-x2)**2 + (y1-y2)**2)
            if distance < 150:  # 只连接附近的节点
                alpha = int(255 * (1 - distance/150) * 0.3)
                overlay_draw.line([(x1, y1), (x2, y2)], fill=(255, 255, 255, alpha), width=1)
    
    # 合成覆盖层
    img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')
    draw = ImageDraw.Draw(img)
    
    try:
        # 使用系统字体
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 96)
        subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 48)
        english_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 32)
        author_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 36)
    except:
        # 回退到默认字体
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        english_font = ImageFont.load_default()
        author_font = ImageFont.load_default()
    
    # 主标题
    title_text = "Happy-LLM"
    subtitle_text = "从零开始学习大语言模型"
    subtitle2_text = "Learning Large Language Models from Scratch"
    author_text = "DataWhale 学习社区"
    
    # 计算文本位置
    title_bbox = draw.textbbox((0, 0), title_text, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    title_height = title_bbox[3] - title_bbox[1]
    
    # 绘制标题，带发光效果
    title_x = (width - title_width) // 2
    title_y = height // 3 - 50
    
    # 发光效果
    for offset in range(3, 0, -1):
        glow_color = (100, 150, 255, 255)
        draw.text((title_x-offset, title_y-offset), title_text, font=title_font, fill=glow_color)
        draw.text((title_x+offset, title_y-offset), title_text, font=title_font, fill=glow_color)
        draw.text((title_x-offset, title_y+offset), title_text, font=title_font, fill=glow_color)
        draw.text((title_x+offset, title_y+offset), title_text, font=title_font, fill=glow_color)
    
    # 主标题
    draw.text((title_x, title_y), title_text, fill=(255, 255, 255), font=title_font)
    
    # 中文副标题
    subtitle_bbox = draw.textbbox((0, 0), subtitle_text, font=subtitle_font)
    subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
    subtitle_x = (width - subtitle_width) // 2
    subtitle_y = title_y + title_height + 40
    
    # 中文副标题阴影
    draw.text((subtitle_x+2, subtitle_y+2), subtitle_text, fill=(0, 0, 0, 128), font=subtitle_font)
    draw.text((subtitle_x, subtitle_y), subtitle_text, fill=(220, 220, 255), font=subtitle_font)
    
    # 英文副标题
    subtitle2_bbox = draw.textbbox((0, 0), subtitle2_text, font=english_font)
    subtitle2_width = subtitle2_bbox[2] - subtitle2_bbox[0]
    subtitle2_x = (width - subtitle2_width) // 2
    subtitle2_y = subtitle_y + 60
    
    draw.text((subtitle2_x+1, subtitle2_y+1), subtitle2_text, fill=(0, 0, 0, 128), font=english_font)
    draw.text((subtitle2_x, subtitle2_y), subtitle2_text, fill=(180, 180, 220), font=english_font)
    
    # 作者信息
    author_bbox = draw.textbbox((0, 0), author_text, font=author_font)
    author_width = author_bbox[2] - author_bbox[0]
    author_x = (width - author_width) // 2
    author_y = height - 150
    
    # 作者信息阴影
    draw.text((author_x+1, author_y+1), author_text, fill=(0, 0, 0, 128), font=author_font)
    draw.text((author_x, author_y), author_text, fill=(200, 200, 255), font=author_font)
    
    # 添加装饰性边框
    border_width = 15
    draw.rectangle([border_width, border_width, width-border_width-1, height-border_width-1], 
                   outline=(255, 255, 255, 150), width=2)
    
    # 添加内部装饰框
    inner_border = 60
    draw.rectangle([inner_border, inner_border, width-inner_border-1, height-inner_border-1], 
                   outline=(255, 255, 255, 80), width=1)
    
    return img

if __name__ == "__main__":
    # 创建专业封面
    cover = create_professional_cover()
    
    # 保存多个版本
    cover.save("/home/young40/Work/AI/happy-llm/docs/images/epub-cover-new.jpg", "JPEG", quality=95)
    cover.save("/home/young40/Work/AI/happy-llm/docs/images/epub-cover-new.png", "PNG")
    cover.save("/home/young40/Work/AI/happy-llm/images/cover-new.jpg", "JPEG", quality=95)
    
    # 创建EPUB专用尺寸 (600x800)
    epub_cover = cover.resize((600, 800), Image.Resampling.LANCZOS)
    epub_cover.save("/home/young40/Work/AI/happy-llm/docs/images/epub-cover-600x800.jpg", "JPEG", quality=95)
    
    # 创建缩略图
    thumbnail = cover.resize((300, 225), Image.Resampling.LANCZOS)
    thumbnail.save("/home/young40/Work/AI/happy-llm/docs/images/epub-cover-thumb.jpg", "JPEG", quality=90)
    
    print("✅ 新的专业封面已创建完成!")
    print("📁 文件位置:")
    print("   📖 docs/images/epub-cover-new.jpg (主封面)")
    print("   📱 docs/images/epub-cover-600x800.jpg (EPUB专用)")
    print("   🖼️  docs/images/epub-cover-thumb.jpg (缩略图)")
    print("   📸 images/cover-new.jpg (备用)")