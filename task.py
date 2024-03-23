import time
from celery import Celery
from random import randint,uniform

app = Celery('task', broker='amqp://localhost')
MINIMUM_HITS_TO_WIN = 3

def simulate_result():
    return [2, 3, 9]

@app.task
def bet_process(user_name: str, user_bet_numbers: list):
    # Fake delay
    random_time = uniform(1.5, 2.5)
    time.sleep(random_time)

    try:
        result_numbers = simulate_result()
        user_hits_count = len([number for number in user_bet_numbers if number in result_numbers])

        if user_hits_count >= MINIMUM_HITS_TO_WIN:
            return f"User {user_name} won with {user_hits_count} hits!\nResult: {result_numbers}\nUser bet: {user_bet_numbers}"
        else:
            return f"User {user_name} lost the bet"
    except Exception as e:
        return f"Error processing bet: {e}"