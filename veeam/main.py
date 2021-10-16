# pip install psutil
import psutil

cpu = psutil.cpu_percent() # Вывод работы процессора
memory_my = psutil.virtual_memory() # Вывод работы оперативной памяти
print('\nВывод процессора -', cpu, '\nВывод памяти -', memory_my)