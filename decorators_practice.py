import time

def timer_dec(base_fn):
    def enhanced_fn():
        start_time = time.time()
        base_fn()
        end_time = time.time()
        print(f'Task time: {(end_time - start_time):.4f}')
    return enhanced_fn

@timer_dec
def greetings():
    print("Hello my friend, how're you?")

greetings()

