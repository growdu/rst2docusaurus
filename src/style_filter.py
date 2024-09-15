#!/usr/bin/env python3

import re
from pandocfilters import toJSONFilter, RawBlock, RawInline, Str, Para

# 正则表达式匹配 style 属性并替换为 {{...}} 的格式
def replace_style_attribute(text):
    return re.sub(r'style="(.*?)"', lambda m: f'style={{{{{m.group(1)}}}}}', text)

def process_html_styles(key, value, format, meta):
    # 处理内联 HTML (RawInline) 和块级 HTML (RawBlock)
    if key == 'RawInline' and value[0] == 'html':
        # 获取 HTML 内容并替换 style 属性
        html_content = value[1]
        replaced_html = replace_style_attribute(html_content)
        return RawInline('html', replaced_html)

    if key == 'RawBlock' and value[0] == 'html':
        # 获取 HTML 内容并替换 style 属性
        html_content = value[1]
        replaced_html = replace_style_attribute(html_content)
        return RawBlock('html', replaced_html)

if __name__ == "__main__":
    toJSONFilter(process_html_styles)
