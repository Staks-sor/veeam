import sys
import ctypes

import PySimpleGUI as sg

from main_window import MainWindow

def main():
    if sys.platform.startswith("win"):
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            u"CompanyName.ProductName.SubProduct.VersionInformation"
        )
    sg.theme("Dark Brown")

    w = MainWindow()
    w.event_loop()


if __name__ == "__main__":
    main()
