# 定义课程列表和相关信息
courses = {
    'fitness': {'name': '健身课程', 'goals': ['增肌', '减脂', '塑形'], 'environment': '室内'},
    'yoga': {'name': '瑜伽课程', 'goals': ['柔韧性', '放松', '减压'], 'environment': '室内'},
    'running': {'name': '跑步课程', 'goals': ['心肺功能', '耐力', '减脂'], 'environment': '室外'},
    'cycling': {'name': '骑行课程', 'goals': ['心肺功能', '耐力', '户外'], 'environment': '室外'},
    'street_dance': {'name': '街舞课程', 'goals': ['协调性', '乐趣', '社交'], 'environment': '室内/室外'},
    'rehabilitation': {'name': '康复课程', 'goals': ['恢复', '伤痛管理', '灵活性'], 'environment': '室内'}
}


# 验证目标是否有效
def validate_goals(goals, valid_goals):
    return all(goal in valid_goals for goal in goals)


# 获取所有有效的目标
def get_all_goals():
    return set(goal for course in courses.values() for goal in course['goals'])


# 定义一个函数来根据用户输入生成训练计划
def generate_training_plan(goals, environment, preferences):
    plan = []
    valid_goals = get_all_goals()

    if not validate_goals(goals, valid_goals):
        print("警告：您输入了一些无效的目标。请确保您的目标在以下列表中：", ", ".join(valid_goals))
        return []

    for course_key, course_info in courses.items():
        if set(goals).intersection(course_info['goals']):  # 检查目标是否匹配
            if (environment in ['室内', '室外', '室内/室外'] and course_info['environment'].split('/')[
                0] in environment.split('/')) or '环境' not in course_info:  # 检查环境
                if preferences.get(course_key, False):  # 检查喜好
                    plan.append(course_info['name'])
    return plan


# 获取用户输入
def get_user_input():
    print("有效的目标包括：", ", ".join(get_all_goals()))

    goals = input("请输入您的健身目标（用逗号分隔，如增肌,减脂）：").split(',')
    goals = [goal.strip() for goal in goals]

    environment_options = ['室内', '室外']
    environment = input("请选择您的训练环境（室内/室外）：").strip().lower()
    while environment not in environment_options:
        print("无效的环境选择。请选择室内或室外。")
        environment = input("请选择您的训练环境（室内/室外）：").strip().lower()

    preferences = {}
    for course_key in courses:
        course_info = courses[course_key]
        print(f"{course_info['name']}（{course_info['environment']}）：")
        like = input(f"您是否喜欢{course_info['name']}？（是/否）：").strip().lower()
        while like not in ['是', '否']:
            print("无效的选择。请输入是或否。")
            like = input(f"您是否喜欢{course_info['name']}？（是/否）：").strip().lower()
        preferences[course_key] = (like == '是')

    return goals, environment, preferences


# 主程序
if __name__ == "__main__":
    goals, environment, preferences = get_user_input()
    training_plan = generate_training_plan(goals, environment, preferences)

    if training_plan:
        print("根据您的输入，以下是个性化的训练计划：")
        for course in training_plan:
            print(course)

        confirm = input("您对这个训练计划满意吗？（是/否）：").strip().lower()
        if confirm == '否':
            print("您可以重新运行程序来生成新的训练计划。")
        else:
            save = input("您想保存这个训练计划到文件吗？（是/否）：").strip().lower()
            if save == '是':
                file_name = input("请输入文件名（不带扩展名）：").strip()
                with open(f"{file_name}.txt", "w") as file:
                    for course in training_plan:
                        file.write(course + "\n")
                print(f"训练计划已保存到 {file_name}.txt")
    else:
        print("没有找到适合您的训练计划。请尝试调整您的输入，确保您的目标、环境和喜好与课程匹配。")