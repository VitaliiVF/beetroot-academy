from task1 import File

file = File("demo.txt", "a")

def test_counter():
    with file as f:
        f.write('Hello!\n')
    
    assert File.counter == 1

def test_log():
    with File("demo.txt", "a") as f:
        f.write('Hello!\n')
        
    assert file.log_print(None) == f"Run #{File.counter} without errors\n"