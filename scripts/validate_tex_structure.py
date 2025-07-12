#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
验证TeX文件结构的脚本
检查main.tex中所有\input的文件是否存在
"""

import os
import re
import sys
from pathlib import Path

def extract_input_files(tex_file):
    """从tex文件中提取所有\\input命令的文件路径"""
    with open(tex_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 匹配\\input{文件路径}的模式
    pattern = r'\\input\{([^}]+)\}'
    matches = re.findall(pattern, content)
    
    return matches

def check_file_exists(base_dir, file_path):
    """检查文件是否存在"""
    full_path = os.path.join(base_dir, file_path + '.tex')
    return os.path.exists(full_path), full_path

def validate_tex_structure():
    """验证TeX文件结构"""
    base_dir = "docs/tex_output"
    main_tex = os.path.join(base_dir, "main.tex")
    
    if not os.path.exists(main_tex):
        print(f"❌ 主文件 {main_tex} 不存在")
        return False
    
    print(f"✅ 找到主文件: {main_tex}")
    
    # 提取所有input文件
    input_files = extract_input_files(main_tex)
    print(f"\n📋 发现 {len(input_files)} 个\\input文件:")
    
    all_exist = True
    for i, file_path in enumerate(input_files, 1):
        exists, full_path = check_file_exists(base_dir, file_path)
        status = "✅" if exists else "❌"
        print(f"  {i:2d}. {status} {file_path}.tex")
        if not exists:
            all_exist = False
    
    if all_exist:
        print(f"\n🎉 所有文件都存在！可以使用以下命令编译:")
        print(f"   cd {base_dir}")
        print(f"   pdflatex main.tex")
        print(f"   pdflatex main.tex  # 运行两次以确保目录正确")
    else:
        print(f"\n⚠️  部分文件缺失，请检查上述标记为❌的文件")
    
    return all_exist

def generate_epub_command():
    """生成EPUB编译命令"""
    print(f"\n📚 生成EPUB的命令:")
    print(f"   cd docs/tex_output")
    print(f"   pandoc main.tex -o happy-llm.epub --pdf-engine=xelatex")
    print(f"   或者使用pandoc直接处理:")
    print(f"   pandoc main.tex -o happy-llm.epub --from=latex --to=epub")

if __name__ == "__main__":
    print("🔍 验证TeX文件结构...")
    success = validate_tex_structure()
    
    if success:
        generate_epub_command()
    
    sys.exit(0 if success else 1) 