class File(object):
    counter = 0
    
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
        
    def __enter__(self):
        File.counter += 1
        return self.file_obj
    
    def __exit__(self, exc_type, exc_value, traceback): 
        
        self.log(exc_type)
            
        if exc_value is not None:
            print(f"Got an exception: {exc_value}")
            # raise exc_value
            
        self.file_obj.close()
                
        return True
    
    @classmethod
    def get_num_of_usage(self):
        return self.counter
    
    def log(self, exc_type):
        with open("log.txt", "a") as l:
            if exc_type is None:
                l.write(f"Run #{File.counter} without errors\n")
            else:
                l.write(f"Run #{File.counter} error - {exc_type}!!!\n")
                
    def log_print(self, exc_type):
        if exc_type is None:
            log = f"Run #{File.counter} without errors\n"
        else:
            log = f"Run #{File.counter} error - {exc_type}!!!\n"
            
        return log
    

with File('demo.txt', 'a') as opened_file:
    opened_file.write('Hello!\n')
    
print(File.counter)
    
with File('demo.txt', 'a') as opened_file:
    opened_file.func('Hello!\n')
    
print(File.counter)