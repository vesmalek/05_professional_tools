import time

def timer_dec(base_fn):
    def enhanced_fn(*args, **kwargs):
        start_time = time.time()
        base_fn(*args, **kwargs)
        end_time = time.time()
        print(f'Task time: {(end_time - start_time):.4f}')
    return enhanced_fn

@timer_dec
def greetings(username, age):
    time.sleep(1)
    print(f"Hello my {username}, how're you? You're {age} years old")

@timer_dec
def travel_abroad():
    time.sleep(1)
    print(f"I am traveling abroad ...")

greetings('izzy', 20)
travel_abroad()

