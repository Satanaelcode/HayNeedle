import random

def generate_ipv4():
    return f"{random.randrange(1,255)}.{random.randrange(1,255)}.{random.randrange(1,255)}.{random.randrange(1,255)}"
