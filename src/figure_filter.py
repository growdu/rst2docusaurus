#!/usr/bin/env python3

from pandocfilters import toJSONFilter, Para, RawInline

def figure_to_markdown(key, value, format, meta):
    if key == 'Figure':
        # 获取 Figure 内部的 Plain 节点
        plain_node = value[2][0]
        if plain_node['t'] == 'Plain':
            # 遍历 Plain 中的元素，找到 Image
            for item in plain_node['c']:
                if item['t'] == 'Image':
                    # 获取 Image 节点中的图片 URL
                    image_info = item['c']
                    image_url = image_info[2][0]  # 获取图片 URL
                    
                    # 使用 RawInline 插入原始 Markdown 代码，并将其放入 Para 块中
                    return Para([RawInline('markdown', f'![]({image_url})')])

if __name__ == "__main__":
    toJSONFilter(figure_to_markdown)
