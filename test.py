from Question import Question
question_prompts = [
    "Переведите десятичное число 2784 в восьмеричную сс\n(a)5340\n(b)5330\n(c)4340\n(d)5240\n\n",
    "Переведите восьмеричное число 7426 в десятеричную сс\n(a)3763\n(b)3861\n(c)2862\n(d)3862\n\n",
    "Переведите дробное десятичное число 946,3 в восьмеричной сс\n(a)1762,33\n(b)1672,33\n(c)1662,23\n(d)1672,23\n\n",
    "Переведите дробное восьмеричное число 365,1 в десятичную сс\n(a)245,125\n(b)246.125\n(c)246.126\n(d)255,126\n\n",
    "Найдите сумму восмеричных чисел 635 и 745\n(a)1502\n(b)1672\n(c)1572\n(d)1602\n\n",
    "Найдите разность восьмеричных чисел 5600 и 3457\n(a)2121\n(b)2120\n(c)2020\n(d)2021\n\n",
    "Найдите произведение восьмеричных чисел 75 и 14\n(a)1324\n(b)1334\n(c)1333\n(d)1234\n\n",
    "Разделить восьмеричное число 725 на 7\n(a)113\n(b)112\n(c)103\n(d)102\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "d"),
    Question(question_prompts[2], "c"),
    Question(question_prompts[3], "a"),
    Question(question_prompts[4], "d"),
    Question(question_prompts[5], "a"),
    Question(question_prompts[6], "b"),
    Question(question_prompts[7], "c")
]

def run_test(questions):
    score = 0
    for question in questions:
        otvet = input(question.vopros)
        if otvet == question.otvet:
            score += 1
print ("У вас" + str(score) + " ответов из" + str(len(questions)) + "верны")
run_test(questions)