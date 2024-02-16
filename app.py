from flask import Flask
import random

app = Flask(__name__)

if __name__ == '__main__':
    app.run(host='localhost', port=8081)

app = Flask(__name__)

@app.route('/roll')
def dice_roll():
    result = random.randint(1, 20)
    return f'Rolled a 20-sided die: {result}'

@app.route('/roll/advantage')
def roll_advantage():
    result1 = random.randint(1, 20)
    result2 = random.randint(1, 20)
    greater_result = max(result1, result2)
    return f'Rolled two 20-sided dice with advantage: {result1}, {result2}. Greater result: {greater_result}'

@app.route('/roll/disadvantage')
def roll_disadvantage():
    result1 = random.randint(1, 20)
    result2 = random.randint(1, 20)
    lesser_result = min(result1, result2)
    return f'Rolled two 20-sided dice with disadvantage: {result1}, {result2}. Lesser result: {lesser_result}'
