import random


print("欢迎使用随机数学口算题生成器！")

num = int(input("请输入题目数量: "))
for i in range(num):
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    operator = random.choice(['+', '-', '*', '/'])
    
    if operator == '+':
        answer = a + b
    elif operator == '-':
        answer = a - b
    elif operator == '*':
        answer = a * b
    else:
        answer = a / b
    
    user_answer = input(f"题目 {i+1}: {a} {operator} {b} = ")
    
    if int(user_answer) == answer:
        print("回答正确！")
    else:
        print(f"回答错误，正确答案是: {answer}")
