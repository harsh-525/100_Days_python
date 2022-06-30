class QuizBrain:
    def __init__(self, question_bank):
        self.question_no = 0
        self.question_bank = question_bank
        self.score = 0

    def still_has_questions(self):
        return self.question_no < len(self.question_bank)

    # TODO 1: Asking user questions
    def next_question(self):
        question = self.question_bank[self.question_no].text
        answer = self.question_bank[self.question_no].answer.lower()
        self.question_no += 1
        choice = input(f"Q.{self.question_no}: {question} (True/False) ").lower()
        self.check_answer(choice, answer)

    # TODO 2: Checking the user answer
    def check_answer(self, choice, answer):
        if choice == answer:
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong!")
        print(f"Your current score: {self.score}/{self.question_no}")
        print(f"The correct answer is {answer}\n")
