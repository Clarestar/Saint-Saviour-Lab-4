from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True, port=8081)
    
from flask import Flask
import random

app = Flask(__name__)

@app.route('/roll')
def roll():
    result = random.randint(1, 20)
    details = random.choice([
        "You swing your sword with precision, landing a solid hit!",
        "Your attack narrowly misses the target, grazing their armor.",
        "The enemy dodges your strike, narrowly avoiding harm."
    ])
    return f"Result for /roll: Rolled a {result}. Combat details: {details}"

@app.route('/roll/advantage')
def roll_advantage():
    result1 = random.randint(1, 20)
    result2 = random.randint(1, 20)
    greater_result = max(result1, result2)
    details = random.choice([
        "You channel your inner strength, delivering a powerful blow!",
        "Your attack lands, but the enemy seems unfazed.",
        "With a quick feint, you catch the enemy off balance, opening them up to further attacks."
    ])
    return f"Result for /roll.advantage: Rolled {result1} and {result2}. Greater result: {greater_result}. Combat details: {details}"

@app.route('/roll/disadvantage')
def roll_disadvantage():
    result1 = random.randint(1, 20)
    result2 = random.randint(1, 20)
    lesser_result = min(result1, result2)
    details = random.choice([
        "Your blow is deflected by the opponent's shield.",
        "In a surprising turn of events, your weapon slips from your grasp, leaving you momentarily vulnerable.",
        "The enemy counterattacks with swift ferocity, catching you off guard."
    ])
    return f"Result for /roll.disadvantage: Rolled {result1} and {result2}. Lesser result: {lesser_result}. Combat details: {details}"

if __name__ == '__main__':
    app.run(debug=True)

