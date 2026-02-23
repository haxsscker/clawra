import os
import glob

directory = r"./"
pattern = os.path.join(directory, "*.jpg")

# 获取所有jpg文件，按修改时间降序排序（最新的在前）
files = glob.glob(pattern)
files.sort(key=os.path.getmtime, reverse=True)

if files:
    print(files[0])
    exit(0)
else:
    print("No images found")
    exit(1)
