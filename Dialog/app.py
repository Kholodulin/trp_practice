import tkinter as tk
from tkinter import messagebox, simpledialog

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("DIALOG-шаблон")
        self.root.geometry("300x200")

        menu_bar = tk.Menu(root)
        root.config(menu=menu_bar)

        task_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Меню", menu=task_menu)
        task_menu.add_command(label="Выполнить задачу", command=self.task)
        task_menu.add_command(label="Подтвердить действие", command=self.confirm)
        task_menu.add_command(label="Ввести данные", command=self.input_data)

        label_text = "пример в Меню"
        label = tk.Label(root, text=label_text)
        label.pack(pady=20)

    def on_exit(self):
        self.root.destroy()

    def task(self):
        messagebox.showinfo("Задача", "Выполнена задача")

    def confirm(self):
        result = messagebox.askokcancel("Подтверждение", "Вы хотите выполнить это действие?")
        if result:
            messagebox.showinfo("Подтверждение", "Действие выполнено")
        else:
            messagebox.showinfo("Подтверждение", "Действие отменено")

    def input_data(self):
        user_input = simpledialog.askstring("Ввод данных", "Введите текст:")
        if user_input:
            messagebox.showinfo("Введенные данные", f"Вы ввели: {user_input}")
        else:
            messagebox.showinfo("Введенные данные", "Ввод отменен")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
