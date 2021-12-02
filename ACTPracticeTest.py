import os

class Answer:
    def __init__(self, input_letter, input_content):
        self.letter = input_letter
        self.content = input_content

class Passage:
    def __init__(self, input_name, input_question_nums, input_content, input_lines):
        self.name = input_name
        self.question_nums = input_question_nums
        self.content = input_content
        self.lines = input_lines

class PracticeTest:
    def __init__(self, input_name, input_time, input_num_questions, input_directions, input_questions, input_passages):
        self.name = input_name
        self.time = input_time
        self.num_questions = input_num_questions
        self.directions = input_directions
        self.questions = input_questions
        self.passages = input_passages

class Question:
    def __init__(self, input_number, input_answers, input_question_text, input_figure, input_correct_answer):
        self.number = input_number
        self.answers = input_answers
        self.question_text = input_question_text
        self.figure = input_figure
        self.correct_answer = input_correct_answer

class ACTPracticeTest:
    def __init__(self, input_tests):
        self.tests = input_tests

file_to_list = []
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'questions.txt')

with open(filename, encoding="utf8", mode='r') as a_file:
    for line in a_file:
        stripped_line = line.strip()
        file_to_list.append(stripped_line)

test_question_list = []
tracker = 0
while tracker < len(file_to_list)-1:
    file_question = Question(0,[],"","",'')
    file_question_answers = []
    file_question.number = int(file_to_list[tracker][0:2])
    file_question.question_text = file_to_list[tracker+1]
    file_question_answers.append(Answer(file_to_list[tracker+2][0],file_to_list[tracker+2][2:len(file_to_list[tracker+2])]))
    file_question_answers.append(Answer(file_to_list[tracker+3][0],file_to_list[tracker+3][2:len(file_to_list[tracker+3])]))
    file_question_answers.append(Answer(file_to_list[tracker+4][0],file_to_list[tracker+4][2:len(file_to_list[tracker+4])]))
    file_question_answers.append(Answer(file_to_list[tracker+5][0],file_to_list[tracker+5][2:len(file_to_list[tracker+5])]))
    file_question.answers = file_question_answers
    file_question.correct_answer = file_to_list[tracker+6]
    test_question_list.append(file_question)
    tracker = tracker + 8

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'instructions.txt')

with open(filename, encoding="utf8", mode='r') as f:
    file_instructions = f.read()

file_to_list = []
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'passages.txt')

with open(filename, encoding="utf8", mode='r') as a_file:
    for line in a_file:
        file_to_list.append(line)

test_passage_list = []
tracker = 0
while tracker < len(file_to_list):
    file_passage = Passage("", [], "", 0)
    file_passage.name = file_to_list[tracker]
    file_passage.question_nums = [int(file_to_list[tracker+1][0:2]), int(file_to_list[tracker+1][3:5])]
    file_passage.lines = int(file_to_list[tracker+2])
    file_passage.content = ' '.join(file_to_list[tracker+3:file_passage.lines+4+tracker])
    test_passage_list.append(file_passage)
    tracker = tracker + file_passage.lines + 5

test_practice_test = PracticeTest("English Test", 45, 75, file_instructions, test_question_list, test_passage_list)
test_act_practice_test = ACTPracticeTest([test_practice_test])

print(test_act_practice_test.tests[0].name)
print(test_act_practice_test.tests[0].time, " Minutes")
print(test_act_practice_test.tests[0].num_questions, " Questions\n")
print(test_act_practice_test.tests[0].directions)
print("")

for current_question in test_act_practice_test.tests[0].questions:
    for current_passage in test_act_practice_test.tests[0].passages:
        if current_question.number <= current_passage.question_nums[1] and current_question.number >= current_passage.question_nums[0]:
            print(current_passage.name)
            print(current_passage.content)

    print(current_question.number, ".")
    print(current_question.question_text)
    for current_answer in current_question.answers:
        print(current_answer.letter, '.', current_answer.content)

    print("")
    user_input = input("Enter Letter Answer: ")
    if user_input == current_question.correct_answer:
        print("Correct")

    else:
        print("Incorrect")

print("Test Complete")
