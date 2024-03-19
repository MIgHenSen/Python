import tkinter as tk
from tkinter import messagebox

def calcular_media():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        media = (num1 + num2) / 2

        messagebox.showinfo("Resultado", f"A média dos números é: {media:.2f}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira apenas números válidos.")

# Criando a janela principal
root = tk.Tk()
root.title("Média2Números")
root.geometry("240x160")
root.configure(bg="lightblue")

# Criando e posicionando os widgets na janela
label_instrucao = tk.Label(root, text="Para calcular a média de 3 números:", bg="lightblue")
label_instrucao.grid(row=0, columnspan=2, padx=20, pady=5)

label_num1 = tk.Label(root, text="N1:")
label_num1.grid(row=1, column=0, padx=10, pady=7, sticky="e")
label_num1.configure(bg="lightblue")
entry_num1 = tk.Entry(root)
entry_num1.grid(row=1, column=1, padx=10, pady=5)

label_num2 = tk.Label(root, text="N2:")
label_num2.grid(row=2, column=0, padx=10, pady=5, sticky="e")
label_num2.configure(bg="lightblue")
entry_num2 = tk.Entry(root)
entry_num2.grid(row=2, column=1, padx=10, pady=5)

btn_calcular = tk.Button(root, text="Calcular Média", command=calcular_media)
btn_calcular.grid(row=4, columnspan=2, padx=10, pady=10)
btn_calcular.configure(bg="gray", fg="white")

# Iniciando o loop principal da aplicação
root.mainloop()
