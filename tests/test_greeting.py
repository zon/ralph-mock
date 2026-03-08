import os

def test_greeting_file_exists():
    assert os.path.exists('greeting.txt'), "greeting.txt should exist in repository root"

def test_greeting_file_content():
    with open('greeting.txt', 'r') as f:
        content = f.read()
    assert content == "Hello from ralph!", f"Expected 'Hello from ralph!' but got '{content}'"

if __name__ == "__main__":
    test_greeting_file_exists()
    test_greeting_file_content()
    print("All tests passed!")
