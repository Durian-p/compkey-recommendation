import os

# 定义文件夹路径
folder_path = "D:\\program\\machine\\compkey\\dataset\\result\\worddict"

# 获取文件夹中以"THUOCL"开头的文件
files = [file for file in os.listdir(folder_path) if file.startswith("THUOCL")]

# 遍历每个文件并处理
for file in files:
    file_path = os.path.join(folder_path, file)

    # 读取文件内容
    with open(file_path, "r", encoding="utf8") as f:
        lines = f.readlines()

    # 处理每行内容并保存回文件
    with open(file_path, "w", encoding="utf8") as f:
        for line in lines:
            # 分割每行内容，以空格为分隔符
            parts = line.strip().split()
            # 如果行内容不为空且包含数字，则取除最后一个元素（数字）
            if parts and any(part.isdigit() for part in parts):
                parts = parts[:-1]
            # 将处理后的内容写回文件
            f.write(" ".join(parts) + "\n")
