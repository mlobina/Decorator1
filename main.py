from datetime import datetime

def logger_decorator(old_func):
    def new_func(*args, **kwargs):
        call_time = datetime.today()
        start = datetime.now()
        f = open('logs_file.txt', 'a')
        f.write(call_time.strftime("%A, %d. %B %Y %I:%M%p") + '\n')
        f.write(f'Function "{old_func.__name__}" was called with arguments "{args, kwargs}". \n')
        result = old_func(*args, **kwargs)
        f.write(f'Function was executed {datetime.now() - start} with result "{result}". \n________________________\n')
        f.close()
        return result

    return new_func

@logger_decorator
def sum(a, b):
   return a + b

@logger_decorator
def dif(a, b):
   return a - b

if __name__ == '__main__':
    sum(4, 5)
    dif(11, 5)