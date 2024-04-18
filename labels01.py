# Labels com Tkinter

# Exemplo 01: Label Simples

import tkinter as tk

janela = tk.Tk()
janela.geometry("300x200")
janela.title("Uso de Labels")

# Criar um label
label = tk.Label(janela, text="Aula de labels")

# Empacotar o Label na janela
label.pack()

# Loop principal
janela.mainloop()

# Exemplo 02

from tkinter import ttk

janela = tk.Tk()
janela.geometry("300x200")
janela.title("Uso de Labels 2")

# Mostrar Label comum
label1 = ttk.Label(
    janela,
    text = "Texto do Label 1",
    font = ("Helvetica", 18)
)
label1.pack(ipadx=10, ipady=30)

# Segundo Label
label2 = ttk.Label(
    janela,
    text = "Texto do Label 2",
    font = ("Arial", 20),
    foreground="blue"

)
label2.pack(ipadx=10, ipady=60)

janela.mainloop()

