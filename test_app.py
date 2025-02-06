from app import hello_world, add_numbers

def test_hello_world():
    assert hello_world() == "Hello from Version Control Jenkins Pipeline!"

def test_add_numbers():
    assert add_numbers(2, 3) == 5

def test_multiply_numbers():
    assert multiply_numbers(2, 3) == 6
