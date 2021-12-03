from constans import Color, Sabor, Aroma
from question import Question
from sklearn import tree
from data import X, Y
import inquirer

question = Question()
questions = question.create_questions()
answers = inquirer.prompt(questions)


# DecisionTreeClassifier
def exec_classifier(data):
    dtc_clf = tree.DecisionTreeClassifier()
    dtc_clf = dtc_clf.fit(X, Y)
    dtc_prediction = dtc_clf.predict(data)
    return dtc_prediction


def get_values_response():
    sabor = answers['sabor']
    aroma = answers['aroma']
    color = answers['color']
    return sabor, aroma, color


def create_data_response():
    sabor, aroma, color = get_values_response()
    one = Sabor[sabor].value
    two = Color[color].value
    three = Aroma[aroma].value
    data_set = [one, two, three]
    return [data_set]


data_classifier = create_data_response()
result_prediction = exec_classifier(data_classifier)
print(f'El resultado de la predicción es que tu cerveza es una: {result_prediction[0]}')
