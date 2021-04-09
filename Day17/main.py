from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


# Initialize the object first
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
else:
    print("You've completed the quiz.")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")














# class User:
#     def __init__(self, user_id, username):
#         # attributes
#         # something the object has
#         self.id = user_id
#         self.username = username
#         self.followers = 0
#         self.following = 0
#
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1
#
#
# # Initialize user_1 object with with a User class
# # 2 parameters required as listed above in attributes
# user_1 = User("001", "Julian")
# user_2 = User("002", "Ari")
#
# user_1.follow(user_2)
#
# print(user_1.followers)
# print(user_1.following)
# print(user_2.followers)
# print(user_2.following)
