#!/bin/bash

# 只修复包含图片的verbatim块，其他verbatim块保持原样

echo "只修复图片相关的verbatim块..."
cd docs/tex_output

find . -name "*.tex" -type f | while read -r tex_file; do
    echo "处理文件: $tex_file"
    temp_file="${tex_file}.tmp"
    awk '
    BEGIN { in_verbatim=0; has_img=0; verbatim_lines=""; }
    /^\\begin{verbatim}/ {
        in_verbatim=1; has_img=0; verbatim_lines=""; print ""; next;
    }
    in_verbatim && /<img src=/ { has_img=1; }
    in_verbatim && !/^\\end{verbatim}/ {
        verbatim_lines = verbatim_lines $0 "\n";
        next;
    }
    /^\\end{verbatim}/ && in_verbatim {
        if (has_img) {
            # 只处理图片相关的verbatim块
            # 使用正确的awk语法替换图片标签
            while (match(verbatim_lines, /<img src="([^"]*)" alt="[^"]*" width="([^"]*)" \/>/)) {
                url = substr(verbatim_lines, RSTART + 10, RLENGTH - 10)
                sub(/alt="[^"]*" width="([^"]*)" \/>/, "", url)
                width = substr(verbatim_lines, RSTART + RLENGTH - 15, 5)
                sub(/width="/, "", width)
                sub(/" \/>/, "", width)
                replacement = "\\\\includegraphics[width=" width "\\\\textwidth]{" url "}"
                sub(/<img src="([^"]*)" alt="[^"]*" width="([^"]*)" \/>/, replacement, verbatim_lines)
            }
            while (match(verbatim_lines, /<img src="([^"]*)" alt="[^"]*" \/>/)) {
                url = substr(verbatim_lines, RSTART + 10, RLENGTH - 10)
                sub(/alt="[^"]*" \/>/, "", url)
                replacement = "\\\\includegraphics[width=0.8\\\\textwidth]{" url "}"
                sub(/<img src="([^"]*)" alt="[^"]*" \/>/, replacement, verbatim_lines)
            }
            while (match(verbatim_lines, /<p>([^<]*)<\/p>/)) {
                caption = substr(verbatim_lines, RSTART + 3, RLENGTH - 7)
                replacement = "\\\\caption{" caption "}"
                sub(/<p>([^<]*)<\/p>/, replacement, verbatim_lines)
            }
            print "\\begin{figure}[htbp]\\centering";
            printf "%s", verbatim_lines;
            print "\\end{figure}";
        } else {
            # 非图片相关的verbatim块100%原样输出
            print "\\begin{verbatim}";
            printf "%s", verbatim_lines;
            print "\\end{verbatim}";
        }
        in_verbatim=0; has_img=0; verbatim_lines=""; next;
    }
    !in_verbatim { print $0; }
    ' "$tex_file" > "$temp_file"
    mv "$temp_file" "$tex_file"
    echo "完成: $tex_file"
done

echo "图片相关verbatim块修复完成，其他内容已恢复原样！" 