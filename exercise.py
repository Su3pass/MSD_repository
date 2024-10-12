# 定义课程列表（同上）
courses = {
    'fitness': '健身课程',
    'yoga': '瑜伽课程',
    'running': '跑步课程',
    'cycling': '骑行课程',
    'street_dance': '街舞课程',
    'rehabilitation': '康复课程'
}

# 显示课程列表并提示用户选择
print("请选择一个课程：")
for key, value in courses.items():
    print(f"{key}: {value}")

# 获取用户输入
choice = input("输入课程类型（如fitness, yoga等）：").strip().lower()

# 检查输入是否有效
if choice in courses:
    print(f'您选择了：{courses[choice]}')
else:
    print("无效的选择，请重试。")