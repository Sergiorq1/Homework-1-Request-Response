from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/penguins')
def penguins():
    return 'Penguins are cute!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    return f'How did you know I liked {users_dessert}?'

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    if number1.isdigit() and number2.isdigit():
        sum = int(number1) * int(number2)  
        return f'{number1} times {number2} equals {sum}'
    else:
        return 'invalid inputs. PLease try again by entering two numbers'
@app.route('/sayntimes/<word>/<n>')
##### This is the stretch Challenge ######
def sayntimes(word, n):
    if not word.isdigit() and n.isdigit():
        wordSpace = word + ' '
        n = int(n)
        return wordSpace * n
    else: 
        return 'invalid input. Please try again by entering a word and a number!'

@app.route('/reverse/<word>')
def reverse(word):
    rev_text = ""
    for char in word:
        rev_text = char + rev_text
    return rev_text

@app.route('strangecaps/<word>')
def strangecaps(word):
    for char in word:
        

if __name__ == '__main__':
    app.run(debug=True)