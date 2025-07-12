#!/bin/bash

# 使用Docker中的pandoc将markdown文件转换为tex文件
# 作者: AI Assistant
# 日期: $(date)

echo "开始使用Docker中的pandoc转换markdown文件为tex文件..."

# 创建输出目录
mkdir -p docs/tex_output

# 转换根目录下的markdown文件
echo "转换根目录下的markdown文件..."
for file in docs/*.md; do
    if [ -f "$file" ]; then
        filename=$(basename "$file" .md)
        echo "转换: $file -> docs/tex_output/${filename}.tex"
        docker run --rm -v "$(pwd):/data" pandoc/core:latest \
            "$file" \
            -o "docs/tex_output/${filename}.tex" \
            --from markdown \
            --to latex \
            --standalone \
            --toc \
            --number-sections
    fi
done

# 转换各章节目录下的markdown文件
echo "转换各章节目录下的markdown文件..."
for chapter_dir in docs/chapter*; do
    if [ -d "$chapter_dir" ]; then
        chapter_name=$(basename "$chapter_dir")
        echo "处理章节: $chapter_name"
        
        # 创建对应的输出目录
        mkdir -p "docs/tex_output/$chapter_name"
        
        # 转换该章节下的所有markdown文件
        for file in "$chapter_dir"/*.md; do
            if [ -f "$file" ]; then
                filename=$(basename "$file" .md)
                echo "转换: $file -> docs/tex_output/$chapter_name/${filename}.tex"
                docker run --rm -v "$(pwd):/data" pandoc/core:latest \
                    "$file" \
                    -o "docs/tex_output/$chapter_name/${filename}.tex" \
                    --from markdown \
                    --to latex \
                    --standalone \
                    --toc \
                    --number-sections
            fi
        done
    fi
done

# 转换Extra-Chapter目录下的markdown文件
if [ -d "Extra-Chapter" ]; then
    echo "转换Extra-Chapter目录下的markdown文件..."
    mkdir -p "docs/tex_output/Extra-Chapter"
    
    for file in Extra-Chapter/*.md; do
        if [ -f "$file" ]; then
            filename=$(basename "$file" .md)
            echo "转换: $file -> docs/tex_output/Extra-Chapter/${filename}.tex"
            docker run --rm -v "$(pwd):/data" pandoc/core:latest \
                "$file" \
                -o "docs/tex_output/Extra-Chapter/${filename}.tex" \
                --from markdown \
                --to latex \
                --standalone \
                --toc \
                --number-sections
        fi
    done
    
    # 处理子目录
    for subdir in Extra-Chapter/*/; do
        if [ -d "$subdir" ]; then
            subdir_name=$(basename "$subdir")
            echo "处理Extra-Chapter子目录: $subdir_name"
            mkdir -p "docs/tex_output/Extra-Chapter/$subdir_name"
            
            for file in "$subdir"/*.md; do
                if [ -f "$file" ]; then
                    filename=$(basename "$file" .md)
                    echo "转换: $file -> docs/tex_output/Extra-Chapter/$subdir_name/${filename}.tex"
                    docker run --rm -v "$(pwd):/data" pandoc/core:latest \
                        "$file" \
                        -o "docs/tex_output/Extra-Chapter/$subdir_name/${filename}.tex" \
                        --from markdown \
                        --to latex \
                        --standalone \
                        --toc \
                        --number-sections
                fi
            done
        fi
    done
fi

echo "转换完成！所有tex文件已保存到 docs/tex_output/ 目录下"
echo "转换的文件列表："
find docs/tex_output -name "*.tex" -type f 