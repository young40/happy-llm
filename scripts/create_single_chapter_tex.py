#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
创建每个章节的独立tex文件，用于调试编译错误
"""

import os
import shutil

def create_single_chapter_tex(chapter_name, chapter_path, output_file):
    """为单个章节创建独立的tex文件"""
    
    # 读取main.tex的头部内容（到\begin{document}之前）
    with open("docs/tex_output/main.tex", 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 找到\begin{document}的位置
    doc_start = content.find("\\begin{document}")
    if doc_start == -1:
        print(f"❌ 在main.tex中找不到\\begin{{document}}")
        return False
    
    # 提取头部内容（包括导言区和\begin{document}）
    header = content[:doc_start + len("\\begin{document}")]
    
    # 读取章节内容
    chapter_file = f"docs/tex_output/{chapter_path}.tex"
    if not os.path.exists(chapter_file):
        print(f"❌ 章节文件不存在: {chapter_file}")
        return False
    
    with open(chapter_file, 'r', encoding='utf-8') as f:
        chapter_content = f.read()
    
    # 组合完整的tex文件
    full_content = f"""{header}

% 标题页
\\begin{{titlepage}}
    \\centering
    \\vspace*{{2cm}}
    
    {{\\Huge\\bfseries 动手学大语言模型}}\\\\[2cm]
    
    {{\\Large 从理论到实践}}\\\\[1cm]
    
    {{\\large Datawhale 开源学习社区}}\\\\[2cm]
    
    \\vfill
    
    {{\\large \\today}}
\\end{{titlepage}}

% 版权页
\\newpage
\\thispagestyle{{empty}}
\\vspace*{{2cm}}
\\begin{{center}}
    \\textbf{{版权声明}}
    
    \\vspace{{1cm}}
    
    本书由 Datawhale 开源学习社区编写，采用开源协议发布。
    
    欢迎读者在遵守开源协议的前提下自由使用、修改和分发本书内容。
    
    \\vspace{{1cm}}
    
    GitHub: https://github.com/datawhalechina/happy-llm
\\end{{center}}

% 目录
\\tableofcontents
\\newpage

% {chapter_name}
\\chapter{{{chapter_name}}}
{chapter_content}

\\end{{document}}
"""
    
    # 写入文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(full_content)
    
    print(f"✅ 已创建: {output_file}")
    return True

def main():
    """主函数"""
    chapters = [
        ("前言", "前言", "docs/tex_output/main_前言.tex"),
        ("NLP基础概念", "chapter1/第一章 NLP基础概念", "docs/tex_output/main_第一章.tex"),
        ("Transformer架构", "chapter2/第二章 Transformer架构", "docs/tex_output/main_第二章.tex"),
        ("预训练语言模型", "chapter3/第三章 预训练语言模型", "docs/tex_output/main_第三章.tex"),
        ("大语言模型", "chapter4/第四章 大语言模型", "docs/tex_output/main_第四章.tex"),
        ("动手搭建大模型", "chapter5/第五章 动手搭建大模型", "docs/tex_output/main_第五章.tex"),
        ("大模型训练流程实践", "chapter6/第六章 大模型训练流程实践", "docs/tex_output/main_第六章.tex"),
        ("大模型应用", "chapter7/第七章 大模型应用", "docs/tex_output/main_第七章.tex"),
    ]
    
    print("🔧 开始创建各章节的独立tex文件...")
    
    success_count = 0
    for chapter_name, chapter_path, output_file in chapters:
        if create_single_chapter_tex(chapter_name, chapter_path, output_file):
            success_count += 1
    
    print(f"\n📊 完成！成功创建 {success_count}/{len(chapters)} 个文件")
    
    if success_count == len(chapters):
        print("🎉 所有章节文件创建成功！")
    else:
        print("⚠️  部分文件创建失败，请检查上述错误信息")

if __name__ == "__main__":
    main() 