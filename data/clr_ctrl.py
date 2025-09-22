import json
import re
from tqdm import tqdm

def count_lines(file_path: str, encoding='utf-8'):
    """高效统计文件总行数（流式处理，不占用大量内存）"""
    line_count = 0
    with open(file_path, 'r', encoding=encoding) as f:
        # 每次读取一块内容，按换行符分割计数（比逐行迭代更高效）
        buffer = f.read(1024 * 1024)  # 1MB缓冲区
        while buffer:
            line_count += buffer.count('\n')
            buffer = f.read(1024 * 1024)
        # 最后一行可能没有换行符，需额外判断
        if buffer[-1:] != '\n':
            line_count += 1
    return line_count

# 定义用于去除控制字符的正则表达式
control_chars = re.compile(r'[\x00-\x1F\x7F]')

# 定义函数用于清理控制字符
def remove_control_characters(s):
    return control_chars.sub('', s)

# 统计总行数
file_path = 'input.json'
total_lines = count_lines(file_path)
print(f"文件总行数：{total_lines}")

# 初始化空字符串存储清理后的内容
cleaned_content = ''

# 逐行读取并清理文件
with open('input.json', 'r', encoding='utf-8') as f:
    for line in tqdm(f, total=total_lines, desc='Processing'):
        cleaned_content += remove_control_characters(line)

# 打印部分内容进行调试
print(cleaned_content[1234170:1234200])  # 打印清理后的前1000个字符以检查是否有问题

# 解析为 JSON 对象
try:
    data = json.loads(cleaned_content)
    print("JSON 文件成功解析")
except json.JSONDecodeError as e:
    print(f"解析 JSON 时出错: {e}")
    exit(1)

# 定义递归函数清理数据中的控制字符
def clean_data(obj):
    if isinstance(obj, str):
        return remove_control_characters(obj)
    elif isinstance(obj, list):
        return [clean_data(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: clean_data(value) for key, value in obj.items()}
    else:
        return obj

# 清理 JSON 数据中的控制字符
cleaned_data = clean_data(data)

# 保存清理后的 JSON 文件
with open('train.json', 'w', encoding='utf-8') as f:
    json.dump(cleaned_data, f, ensure_ascii=False, indent=4)
