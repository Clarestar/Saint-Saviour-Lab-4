# Flask Combat App

This Flask application simulates combat scenarios with dice rolls.

## Getting Started

1. Clone this repository.
2. Install dependencies: pip install -r requirements.txt
3. Run the app: python app.py

## Endpoints

- /roll: Roll a twenty-sided die.
  - Example Result: Combat details for /roll: Rolled a 15. The attack lands, dealing a solid blow to the opponent.
  ![Roll Image](images/roll.png)

- /roll.advantage: Roll two twenty-sided dice and return the greater result.
  - Example Result: Combat details for /roll.advantage: Rolled 10 and 18. The advantage of the attacker shines as the higher roll of 18 determines the success of the attack.
  ![Roll Advantage Image](images/roll_advantage.png)

- /roll.disadvantage: Roll two twenty-sided dice and return the lesser result.
  - Example Result: Combat details for /roll.disadvantage: Rolled 14 and 7. Despite the disadvantage, the attacker manages to land a hit with the lower roll of 7.
  ![Roll Disadvantage Image](images/roll_disadvantage.png)

...