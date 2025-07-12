#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
合并README和第一章tex文件到一个大的tex文件中
"""

import os
import re
from pathlib import Path

def extract_content_from_tex(tex_file_path):
    """从tex文件中提取内容部分，去除文档结构"""
    with open(tex_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 查找\begin{document}和\end{document}之间的内容
    start_pattern = r'\\begin\{document\}'
    end_pattern = r'\\end\{document\}'
    
    start_match = re.search(start_pattern, content)
    end_match = re.search(end_pattern, content)
    
    if start_match and end_match:
        start_pos = start_match.end()
        end_pos = end_match.start()
        return content[start_pos:end_pos].strip()
    else:
        # 如果没有找到document环境，返回整个内容
        return content

def create_combined_tex():
    """创建合并的tex文件"""
    
    # 主文档模板
    main_template = r"""\documentclass[12pt,a4paper]{book}
\usepackage[UTF8]{ctex}
\usepackage{geometry}
\usepackage{graphicx}
\usepackage{hyperref}
\usepackage{bookmark}
\usepackage{amsmath,amssymb}
\usepackage{listings}
\usepackage{xcolor}
\usepackage{fancyhdr}
\usepackage{titlesec}
\usepackage{tocloft}

% 页面设置
\geometry{left=2.5cm,right=2.5cm,top=2.5cm,bottom=2.5cm}

% 代码块设置
\lstset{
    basicstyle=\ttfamily\small,
    breaklines=true,
    frame=single,
    numbers=left,
    numberstyle=\tiny,
    keywordstyle=\color{blue},
    commentstyle=\color{green!60!black},
    stringstyle=\color{red},
    backgroundcolor=\color{gray!10},
    showspaces=false,
    showstringspaces=false,
    showtabs=false,
    tabsize=2
}

% 超链接设置
\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    filecolor=magenta,
    urlcolor=cyan,
    citecolor=green,
    bookmarks=true,
    bookmarksopen=true,
    pdfstartview=FitH
}

% 页眉页脚设置
\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE,RO]{\thepage}
\fancyhead[RE]{\leftmark}
\fancyhead[LO]{\rightmark}
\renewcommand{\headrulewidth}{0.4pt}

% 章节标题格式
\titleformat{\chapter}{\Large\bfseries}{\thechapter}{1em}{}
\titleformat{\section}{\large\bfseries}{\thesection}{1em}{}
\titleformat{\subsection}{\normalsize\bfseries}{\thesubsection}{1em}{}

% 目录格式
\renewcommand{\cftchapfont}{\bfseries}
\renewcommand{\cftsecfont}{\normalsize}

\begin{document}

% 标题页
\begin{titlepage}
    \centering
    \vspace*{2cm}
    
    {\Huge\bfseries Happy-LLM 大语言模型教程}\\[2cm]
    
    {\Large 从零开始的大语言模型原理与实践教程}\\[1cm]
    
    {\large Datawhale 开源学习社区}\\[2cm]
    
    \vfill
    
    {\large \today}
\end{titlepage}

% 版权页
\newpage
\thispagestyle{empty}
\vspace*{2cm}
\begin{center}
    \textbf{版权声明}
    
    \vspace{1cm}
    
    本书由 Datawhale 开源学习社区编写，采用开源协议发布。
    
    欢迎读者在遵守开源协议的前提下自由使用、修改和分发本书内容。
    
    \vspace{1cm}
    
    GitHub: https://github.com/datawhalechina/happy-llm
\end{center}

% 目录
\tableofcontents
\newpage

{content}

\end{document}
"""
    
    # 包含README和第一章
    chapters = [
        ("README", "docs/tex_output/README.tex"),
        ("第一章 NLP基础概念", "docs/tex_output/chapter1/第一章 NLP基础概念.tex"),
    ]
    
    # 合并内容
    combined_content = ""
    
    for i, (title, file_path) in enumerate(chapters, 1):
        if os.path.exists(file_path):
            print(f"处理文件 {i}: {title}")
            content = extract_content_from_tex(file_path)
            
            # 为第一章添加章节标题
            if i == 2:  # 第一章
                combined_content += f"\\chapter{{{title}}}\n"
            
            # 添加内容
            combined_content += content + "\n\n"
        else:
            print(f"警告: 文件不存在 {file_path}")
    
    # 创建最终的tex文件
    final_content = main_template.replace("{content}", combined_content)
    
    # 写入文件
    output_file = "docs/tex_output/main_combined.tex"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(final_content)
    
    print(f"合并完成！输出文件: {output_file}")
    print(f"文件大小: {os.path.getsize(output_file)} 字节")

if __name__ == "__main__":
    create_combined_tex() 