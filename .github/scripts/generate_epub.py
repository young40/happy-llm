#!/usr/bin/env python3
"""
Generate EPUB from XHTML files for Happy-LLM project
"""

import os
import sys
from ebooklib import epub
from pathlib import Path
import re

def create_epub():
    """Create EPUB book from XHTML files"""
    
    # Create EPUB book
    book = epub.EpubBook()
    
    # Set metadata
    book.set_identifier('happy-llm-2025')
    book.set_title('Happy LLM - 从0开始构建大语言模型')
    book.set_language('zh')
    
    book.add_author('DataWhale团队')
    book.add_author('Happy-LLM贡献者')
    
    book.add_metadata('DC', 'description', 
                     'Happy LLM是一本面向中文社区的大语言模型学习指南，从基础概念到实战应用，帮助读者深入理解并实践构建大语言模型。')
    book.add_metadata('DC', 'subject', 'Large Language Models')
    book.add_metadata('DC', 'subject', 'Machine Learning')
    book.add_metadata('DC', 'subject', 'Natural Language Processing')
    book.add_metadata('DC', 'subject', 'Deep Learning')
    
    # Add CSS stylesheet
    css_path = Path('docs/epub-style.css')
    if css_path.exists():
        with open(css_path, 'r', encoding='utf-8') as f:
            css_content = f.read()
        
        # Ensure relative paths in CSS
        css_content = css_content.replace('../', '')
        css_content = css_content.replace('./', '')
        
        default_css = epub.EpubItem(
            uid="style_default",
            file_name="style/epub-style.css",
            media_type="text/css",
            content=css_content
        )
        book.add_item(default_css)
    
    # Define chapters in order
    chapters = [
        {
            'title': '前言',
            'file': 'docs/preface.xhtml',
            'id': 'preface'
        },
        {
            'title': '第一章 NLP基础概念',
            'file': 'docs/chapter1.xhtml',
            'id': 'chapter1'
        },
        {
            'title': '第二章 Transformer架构',
            'file': 'docs/chapter2_transformer_architecture.xhtml',
            'id': 'chapter2'
        },
        {
            'title': '第三章 预训练语言模型',
            'file': 'docs/chapter3_pretrained_language_models.xhtml',
            'id': 'chapter3'
        },
        {
            'title': '第四章 大语言模型',
            'file': 'docs/chapter4_large_language_models.xhtml',
            'id': 'chapter4'
        },
        {
            'title': '第五章 动手搭建大模型',
            'file': 'docs/chapter5_building_large_models.xhtml',
            'id': 'chapter5'
        },
        {
            'title': '第六章 大模型训练流程实践',
            'file': 'docs/chapter6/第六章 大模型训练流程实践.xhtml',
            'id': 'chapter6'
        },
        {
            'title': '第七章 大模型应用',
            'file': 'docs/chapter7/第七章 大模型应用.xhtml',
            'id': 'chapter7'
        },
        {
            'title': '4.1 偏好对齐',
            'file': 'docs/chapter6/6.4[WIP] 偏好对齐.xhtml',
            'id': 'preference_alignment'
        },
        {
            'title': '为什么微调小型大语言模型',
            'file': 'Extra-Chapter/why-fine-tune-small-large-language-models/readme.xhtml',
            'id': 'why-fine-tune'
        },
        {
            'title': 'Transformer架构详解',
            'file': 'Extra-Chapter/transformer-architecture/readme.xhtml',
            'id': 'transformer-architecture'
        }
    ]
    
    epub_chapters = []
    spine_items = ['nav']
    
    for idx, chapter in enumerate(chapters, 1):
        file_path = Path(chapter['file'])
        
        if not file_path.exists():
            print(f"Warning: {file_path} not found, skipping...")
            continue
            
        # Read and process XHTML content
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Fix relative paths for EPUB
        content = content.replace('../epub-style.css', 'style/epub-style.css')
        content = content.replace('../../docs/epub-style.css', 'style/epub-style.css')
        
        # Ensure proper XHTML structure
        if '<!DOCTYPE' not in content:
            content = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>{chapter['title']}</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <link rel="stylesheet" type="text/css" href="style/epub-style.css"/>
</head>
<body>
{content}
</body>
</html>'''
        
        # Create EPUB chapter
        epub_chapter = epub.EpubHtml(
            title=chapter['title'],
            file_name=f"{chapter['id']}.xhtml",
            lang='zh',
            content=content
        )
        
        book.add_item(epub_chapter)
        epub_chapters.append(epub_chapter)
        spine_items.append(epub_chapter)
    
    # Create table of contents
    book.toc = tuple(epub_chapters)
    
    # Add navigation files
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    
    # Create spine
    book.spine = spine_items
    
    # Generate EPUB file
    epub_path = 'happy-llm.epub'
    epub.write_epub(epub_path, book)
    
    print(f"EPUB generated successfully: {epub_path}")
    print(f"Total chapters included: {len(epub_chapters)}")
    
    return epub_path

if __name__ == '__main__':
    try:
        create_epub()
    except Exception as e:
        print(f"Error generating EPUB: {e}")
        sys.exit(1)
