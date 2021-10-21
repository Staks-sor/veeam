import psutil
import time
import datetime
import json

number = int(input("Ведите промижуток времени проверки в секундах: "))



while True:
    time.sleep(number)
    cpu = psutil.cpu_percent(interval=1)  # Вывод загрузки процессора в роцентах
    private_bytes = psutil.virtual_memory().used  # Вывод работы оперативной памяти
    working_set = psutil.virtual_memory().percent  # Вывод работы оперативной памяти
    pid = psutil.Process().pid
    current_time = datetime.datetime.now().strftime("%F %T")
    log_str = " time            {}\n cpu             {}%\n private_bytes   {}\n working_set     {}%\n handle          {}\n".format(
        current_time, cpu, private_bytes, working_set, pid)
    print(log_str)
    metrics_data = {
        "cpu": cpu,
        "private_bytes": private_bytes,
        "working_set": working_set,
        "pid": pid,
        "current_time": current_time,
    }

    with open("data.json", "a") as data_file:
        json.dump(metrics_data, data_file, indent=2)

