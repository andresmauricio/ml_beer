import inquirer

from constans import Sabor, Color, Aroma


class Question:
    choice_sabor = []
    choice_aroma = []
    choice_color = []

    def __init__(self):
        for item in Sabor:
            self.choice_sabor.append(item.name)
        for item in Color:
            self.choice_color.append(item.name)
        for item in Aroma:
            self.choice_aroma.append(item.name)

    def create_questions(self):
        questions = [
            inquirer.List('sabor',
                          message="¿Qué sabor tiene tú cerveza?",
                          choices=self.choice_sabor,
                          ),
            inquirer.List('color',
                          message="¿Qué color tiene tú cerveza?",
                          choices=self.choice_color,
                          ),
            inquirer.List('aroma',
                          message="¿Qué aroma tiene tú cerveza?",
                          choices=self.choice_aroma,
                          ),
        ]
        return questions
