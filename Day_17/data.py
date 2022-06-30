"""
Helpful website: https://opentdb.com
"""
# question_data = [
#     {"text": "A slug's blood is green.", "answer": "True"},
#     {"text": "The loudest animal is the African Elephant.", "answer": "False"},
#     {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
#     {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
#     {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, "
#              "you are free to take it home to eat.", "answer": "True"},
#     {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.",
#      "answer": "False"},
#     {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
#     {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
#     {"text": "Google was originally called 'Backrub'.", "answer": "True"},
#     {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
#     {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
#     {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
# ]
question_data = [
    {"category": "Sports",
     "type": "boolean",
     "difficulty": "easy",
     "question": "Manchester United won the 2013-14 English Premier League.",
     "correct_answer": "False",
     "incorrect_answers": ["True"]
     },
    {"category": "Sports",
     "type": "boolean",
     "difficulty": "easy",
     "question": "Peyton Manning retired after winning Super Bowl XLIX.",
     "correct_answer": "False",
     "incorrect_answers": ["True"]
     },
    {"category": "Sports", "type": "boolean", "difficulty": "medium",
     "question": "Skateboarding will be included in the 2020 Summer Olympics in Tokyo.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Sports", "type": "boolean", "difficulty": "medium",
     "question": "Tennis was once known as Racquetball.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Sports", "type": "boolean", "difficulty": "medium",
     "question": "The Olympics tennis court is a giant green screen.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Sports", "type": "boolean", "difficulty": "easy",
     "question": "Roger Federer is a famous soccer player.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Sports", "type": "boolean", "difficulty": "medium",
     "question": "Formula E is an auto racing series that uses hybrid electric race cars.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Sports", "type": "boolean", "difficulty": "easy",
     "question": "In Rugby League, performing a &quot;40-20&quot; is punished by a free kick for the opposing team.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Sports", "type": "boolean", "difficulty": "medium",
     "question": "Wilt Chamberlain scored his infamous 100-point-game against the New York Knicks in 1962.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Sports", "type": "boolean", "difficulty": "medium",
     "question": "During Wimbledon, spectators in the grounds can buy the tennis balls that have been used in matches.",
     "correct_answer": "True", "incorrect_answers": ["False"]}]
