# pip install psutil
import psutil
import time

TIME_TO_LOOP = 60
start = time.time()
while time.time() < start + TIME_TO_LOOP:
    start = time.time()
    cpu = psutil.cpu_percent(interval=1) # Вывод загрузки процессора в роцентах
    working_set = psutil.virtual_memory().used
    private_bytes = psutil.virtual_memory().percent # Вывод работы оперативной памяти
    #for proc in psutil.process_iter(['pid', 'name', 'username']):
    print("\nЗагрузка процессора - {}% \nИспользование памяти - {} \nПамять - {}%".format(cpu, working_set, private_bytes))
time.sleep(5)




