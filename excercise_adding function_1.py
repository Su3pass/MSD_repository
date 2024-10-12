# 定义课程列表和相关信息
courses = {
    'fitness': {'name': '健身课程', 'goals': ['增肌', '减脂', '塑形']},
    'yoga': {'name': '瑜伽课程', 'goals': ['柔韧性', '放松', '减压']},
    'running': {'name': '跑步课程', 'goals': ['心肺功能', '耐力', '减脂']},
    'cycling': {'name': '骑行课程', 'goals': ['心肺功能', '耐力', '户外']},
    'street_dance': {'name': '街舞课程', 'goals': ['协调性', '乐趣', '社交']},
    'rehabilitation': {'name': '康复课程', 'goals': ['恢复', '伤痛管理', '灵活性']}
}


# 定义一个函数来根据用户输入生成训练计划
def generate_training_plan(goals, environment, preferences):
    plan = []
    for course_key, course_info in courses.items():
        if set(goals).intersection(course_info['goals']):  # 检查目标是否匹配
            if environment in ['室内', '室外'] or '环境' not in course_info:  # 检查环境（如果课程没有指定环境，则忽略此条件）
                if preferences.get(course_key, False):  # 检查喜好（如果用户没有明确表示喜欢或不喜欢，则默认为可能喜欢）
                    plan.append(course_info['name'])
    return plan


# 获取用户输入
def get_user_input():
    goals = input("请输入您的健身目标（用逗号分隔，如增肌,减脂）：").split(',')
    goals = [goal.strip() for goal in goals]

    environment = input("请选择您的训练环境（室内/室外）：").strip().lower()

    preferences = {}
    for course_key in courses:
        like = input(f"您是否喜欢{courses[course_key]['name']}？（是/否）：").strip().lower()
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
    else:
        print("没有找到适合您的训练计划。请尝试调整您的输入。")

