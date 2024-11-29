import tkinter as tk
from tkinter import messagebox
import json
import os

# 获取当前脚本文件的目录
script_dir = os.path.dirname(os.path.abspath(__file__))  # 获取脚本的绝对路径

# JSON 文件路径（与脚本文件同目录）
json_file_path = os.path.join(script_dir, 'menu-data.json')

# 加载 JSON 数据
def load_json():
    # 如果文件存在则从文件加载数据
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    else:
        # 如果文件不存在，则返回默认数据
        return {
            "skincare-science": [
                {
                    "title": "冬季肌肤救援指南",
                    "description": "全面解决干燥、敏感、缺水等冬季肌肤难题",
                    "path": "/posts/skincare-science/winter-skin-rescue.md",
                    "category": "skincare-science",
                    "image": "/api/placeholder/400/250"
                },
                {
                    "title": "夏季防晒全攻略",
                    "description": "深入了解防晒科学，全方位保护肌肤",
                    "path": "/posts/skincare-science/summer-sunscreen-guide.md",
                    "category": "skincare-science",
                    "image": "/api/placeholder/400/250"
                }
            ],
            "beauty-trends": [
                {
                    "title": "新一代精华成分解析",
                    "description": "揭秘最前沿的护肤科技和突破性成分",
                    "path": "/posts/beauty-trends/essence-ingredients.md",
                    "category": "beauty-trends",
                    "image": "/api/placeholder/400/250"
                },
                {
                    "title": "2024全球美容趋势",
                    "description": "解读当下最热门的美容科技和理念",
                    "path": "/posts/beauty-trends/global-beauty-trends.md",
                    "category": "beauty-trends",
                    "image": "/api/placeholder/400/250"
                }
            ],
            "practical-guides": [
                {
                    "title": "敏感肌终极调理",
                    "description": "专业解读敏感肌肤的修复与呵护秘诀",
                    "path": "/posts/practical-guides/sensitive-skin-care.md",
                    "category": "practical-guides",
                    "image": "/api/placeholder/400/250"
                },
                {
                    "title": "每日护肤routine指南",
                    "description": "科学制定适合自己的护肤程序",
                    "path": "/posts/practical-guides/daily-skincare-routine.md",
                    "category": "practical-guides",
                    "image": "/api/placeholder/400/250"
                }
            ]
        }

# 保存 JSON 数据到文件
def save_json(data):
    with open(json_file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

class JsonEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("JSON Editor")
        self.root.geometry("600x400")

        self.data = load_json()  # 从文件加载 JSON 数据
        
        self.category_var = tk.StringVar()
        self.title_var = tk.StringVar()
        self.description_var = tk.StringVar()
        self.path_var = tk.StringVar()
        self.image_var = tk.StringVar()

        # Category selection dropdown
        self.category_label = tk.Label(root, text="选择分类")
        self.category_label.pack(pady=5)
        
        self.category_menu = tk.OptionMenu(root, self.category_var, *self.data.keys())
        self.category_menu.pack(pady=5)

        # Article title input
        self.title_label = tk.Label(root, text="文章标题")
        self.title_label.pack(pady=5)
        self.title_entry = tk.Entry(root, textvariable=self.title_var, width=50)
        self.title_entry.pack(pady=5)

        # Article description input
        self.description_label = tk.Label(root, text="文章描述")
        self.description_label.pack(pady=5)
        self.description_entry = tk.Entry(root, textvariable=self.description_var, width=50)
        self.description_entry.pack(pady=5)

        # Article path input
        self.path_label = tk.Label(root, text="文章路径")
        self.path_label.pack(pady=5)
        self.path_entry = tk.Entry(root, textvariable=self.path_var, width=50)
        self.path_entry.pack(pady=5)

        # Article image input
        self.image_label = tk.Label(root, text="文章配图URL")
        self.image_label.pack(pady=5)
        self.image_entry = tk.Entry(root, textvariable=self.image_var, width=50)
        self.image_entry.pack(pady=5)

        # Buttons
        self.add_button = tk.Button(root, text="添加文章", command=self.add_article)
        self.add_button.pack(pady=10)

        self.show_button = tk.Button(root, text="显示当前 JSON 内容", command=self.show_json)
        self.show_button.pack(pady=5)

    def add_article(self):
        # 获取输入数据
        category = self.category_var.get()
        title = self.title_var.get()
        description = self.description_var.get()
        path = self.path_var.get()
        image = self.image_var.get()

        # 验证输入
        if not category or not title or not description or not path or not image:
            messagebox.showerror("错误", "所有字段都是必填项")
            return

        # 新文章内容
        new_article = {
            "title": title,
            "description": description,
            "path": path,
            "category": category,
            "image": image
        }

        # 将新文章添加到对应的分类
        self.data[category].append(new_article)

        # 保存更新后的 JSON 数据
        save_json(self.data)

        # 清空输入框
        self.title_var.set("")
        self.description_var.set("")
        self.path_var.set("")
        self.image_var.set("")

        messagebox.showinfo("成功", "文章已成功添加")

    def show_json(self):
        # 显示当前 JSON 数据
        json_str = json.dumps(self.data, ensure_ascii=False, indent=4)
        messagebox.showinfo("当前 JSON 数据", json_str)

if __name__ == "__main__":
    root = tk.Tk()
    app = JsonEditorApp(root)
    root.mainloop()
