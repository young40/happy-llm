import re
import os

# 只修复包含图片的verbatim块，其他内容逐行原样输出

def process_tex_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    out_lines = []
    in_verbatim = False
    verbatim_lines = []
    for line in lines:
        if not in_verbatim:
            if line.strip() == r'\begin{verbatim}':
                in_verbatim = True
                verbatim_lines = [line]
            else:
                out_lines.append(line)
        else:
            verbatim_lines.append(line)
            if line.strip() == r'\end{verbatim}':
                # 判断verbatim块内是否有图片
                verbatim_content = ''.join(verbatim_lines)
                img_match = re.search(r'<img src="([^"]+)"[^>]*>', verbatim_content)
                if img_match:
                    # 提取图片和caption
                    img_tag = re.search(r'<img src="([^"]+)"(?: alt="[^"]*")?(?: width="([^"]*)")?(?: style="width: ([^;]+);")? ?/?>', verbatim_content)
                    img_url = img_tag.group(1) if img_tag else ''
                    width = img_tag.group(2) or img_tag.group(3) or '0.8' if img_tag else '0.8'
                    width = width.replace('%','').replace('px','')
                    try:
                        width_float = float(width)
                        if width_float > 2:  # 80, 100等百分比，转为0.8, 1.0
                            width = str(width_float/100)
                    except:
                        width = '0.8'
                    caption_match = re.search(r'<p>([^<]*)</p>', verbatim_content)
                    caption = caption_match.group(1) if caption_match else ''
                    out_lines.append('\\begin{figure}[htbp]\\centering\n')
                    out_lines.append(f'\\includegraphics[width={width}\\textwidth]{{{img_url}}}\n')
                    if caption:
                        out_lines.append(f'\\caption{{{caption}}}\n')
                    out_lines.append('\\end{figure}\n')
                else:
                    out_lines.extend(verbatim_lines)
                in_verbatim = False
                verbatim_lines = []
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(out_lines)


def process_all_tex_files():
    for root, dirs, files in os.walk('docs/tex_output'):
        for file in files:
            if file.endswith('.tex'):
                process_tex_file(os.path.join(root, file))

if __name__ == '__main__':
    process_all_tex_files()
    print('所有图片相关verbatim块已修复，其他内容保持原样！') 