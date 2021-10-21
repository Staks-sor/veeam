import dataclasses
import datetime
import threading
import time
import typing
import json
import PySimpleGUI as sg
import psutil


@dataclasses.dataclass
class SystemInfo:
    cpu: float
    private_bytes: float
    working_set: float
    pid: int
    current_time: typing.Any


def get_system_info() -> SystemInfo:
    cpu = psutil.cpu_percent(interval=1)
    private_bytes = psutil.virtual_memory().used
    working_set = psutil.virtual_memory().percent
    pid = psutil.Process().pid
    current_time = datetime.datetime.now().strftime("%F %T")
    log_str = " cpu               {}%\n private_bytes   {}\n working_set     {}%\n pid          {}\n current_time            {}".format(
        cpu, private_bytes, working_set, pid, current_time
    )
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


class MainWindow(sg.Window):
    def __init__(self):
        self.text = sg.Text("Введите интервал проверки в секундах")
        self.input_text = sg.InputText(key="-INPUT-", size=(10, 10))
        self.output = sg.Output(size=(88, 20))
        self.start = sg.Submit("Начать")
        self.exit = sg.Exit("закрыть")
        self.layout = [
            [self.text, self.input_text],
            [self.output],
            [self.start, self.exit],
        ]
        super().__init__("Test exercise", self.layout, resizable=False, finalize=True)
        self.thread = None
        self.thread_canceled = False

    def on_start_button(self):
        def thread_function(window, sleep_interval):
            while True:
                time.sleep(sleep_interval)
                info: SystemInfo = get_system_info()
                window.write_event_value("-THREAD-", info)

        try:
            interval = int(self.input_text.get())
            self.thread = threading.Thread(
                target=thread_function, args=(self, interval), daemon=True
            )
            self.thread.start()
        except ValueError:
            print("Значание должно быть числом")

    def event_loop(self):
        while True:
            event, values = self.Read()
            if event in (None, "Exit", "закрыть"):
                return
            elif event == "Начать":
                self.on_start_button()
            elif event == "-THREAD-":
                pass
