#!/bin/bash

# 使用Docker中的LaTeX环境编译PDF
# 作者: AI Assistant
# 日期: $(date)

echo "开始使用Docker中的LaTeX环境编译PDF..."

# 检查是否存在main.tex文件
if [ ! -f "docs/tex_output/main.tex" ]; then
    echo "错误: 找不到main.tex文件"
    exit 1
fi

# 使用Docker中的LaTeX环境编译
echo "使用Docker中的LaTeX环境编译PDF..."
docker run --rm -v "$(pwd)/docs/tex_output:/workspace" -w /workspace \
    registry.gitlab.com/islandoftex/images/texlive:latest \
    xelatex -interaction=nonstopmode main.tex

# 再次编译以确保目录正确
echo "第二次编译以确保目录正确..."
docker run --rm -v "$(pwd)/docs/tex_output:/workspace" -w /workspace \
    registry.gitlab.com/islandoftex/images/texlive:latest \
    xelatex -interaction=nonstopmode main.tex

# 检查是否成功生成PDF
if [ -f "docs/tex_output/main.pdf" ]; then
    echo "PDF编译成功！"
    echo "PDF文件位置: docs/tex_output/main.pdf"
    echo "文件大小: $(du -h docs/tex_output/main.pdf | cut -f1)"
else
    echo "PDF编译失败，请检查错误信息"
    exit 1
fi

echo "编译完成！" 