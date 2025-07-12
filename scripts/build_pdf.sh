#!/bin/bash

# 编译tex文件生成PDF
# 作者: AI Assistant
# 日期: $(date)

echo "开始编译PDF..."

# 进入tex输出目录
cd docs/tex_output

# 检查是否存在main.tex文件
if [ ! -f "main.tex" ]; then
    echo "错误: 找不到main.tex文件"
    exit 1
fi

# 使用xelatex编译（支持中文）
echo "使用xelatex编译PDF..."
xelatex -interaction=nonstopmode main.tex

# 再次编译以确保目录正确
echo "第二次编译以确保目录正确..."
xelatex -interaction=nonstopmode main.tex

# 检查是否成功生成PDF
if [ -f "main.pdf" ]; then
    echo "PDF编译成功！"
    echo "PDF文件位置: docs/tex_output/main.pdf"
    echo "文件大小: $(du -h main.pdf | cut -f1)"
else
    echo "PDF编译失败，请检查错误信息"
    exit 1
fi

# 返回原目录
cd ../..

echo "编译完成！" 