def greeting(name):
    msg = f"Hello {name}"
    return msg

def add_numbers(a: int, b: int) -> int:
    c = a+b
    return c

if __name__=="__main__":
    print(greeting("Rahul"))
    print(add_numbers(5, 10))
