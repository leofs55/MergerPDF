import tkinter as tk
from tkinter import filedialog
import datetime
import merger


class App:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Mesclador de Arquivos")
        self.root.geometry("400x300")

        self.PATH_INPUT = tk.StringVar()
        self.PATH_OUTPUT = tk.StringVar()
        self.name_file = tk.StringVar()
        self.name_file.set(f"Arquivo{datetime.date.today()}")

        tk.Label(self.root, text='Diretório de entrada').pack(pady=5)
        entrada = tk.Entry(self.root,
                           textvariable=self.PATH_INPUT, width=50)
        entrada.pack()
        tk.Button(self.root, text='Selecionar',
                  command=self.selector_directory_input).pack(pady=5)

        tk.Label(self.root, text='Diretório de saída').pack(pady=5)
        saida = tk.Entry(self.root,
                         textvariable=self.PATH_OUTPUT, width=50)
        saida.pack()
        tk.Button(self.root, text='Selecionar',
                  command=self.selector_directory_output).pack(pady=5)

        tk.Label(self.root, text='Nome do arquivo: ').pack(pady=5)
        nome = tk.Entry(self.root,
                        textvariable=self.name_file, width=50)
        nome.pack()

        tk.Button(self.root, text="Mesclar Arquivos",
                  command=self.merge_files).pack(pady=5)

    def exec(self) -> None:
        self.root.mainloop()

    def selector_directory_input(self) -> None:
        path = filedialog.askdirectory()
        if path:
            self.PATH_INPUT.set(path)

    def selector_directory_output(self) -> None:
        path = filedialog.askdirectory()
        if path:
            self.PATH_OUTPUT.set(path)

    def merge_files(self):
        md = merger.Merger(self.PATH_INPUT.get(), self.PATH_OUTPUT.get(),
                           self.name_file.get())
        md.merge_files()
