import time, random
from task import bet_process

def generate_full_name():
    # Lista de nomes e sobrenomes
    nomes = ["alice", "bob", "carol", "david", "eva", "frank", "gina", "henry", "ivy", "jack",
             "kelly", "liam", "mia", "noah", "olivia", "peter", "quinn", "rachel", "sam", "taylor"]
    sobrenomes = ["smith", "johnson", "brown", "davis", "miller", "wilson", "moore", "taylor", "anderson", "thomas",
                  "jackson", "white", "harris", "martin", "thompson", "garcia", "martinez", "robinson", "clark", "lewis"]
    
    return f"{random.choice(nomes)} {random.choice(sobrenomes)}"

for i in range(10):
    user_name = generate_full_name()
    user_bet_numbers = random.sample(range(1, 11), 6)

    bet_process.delay(user_name, user_bet_numbers)

    print(f"Bet placed: {user_name} - {user_bet_numbers}")
    time.sleep(1)
