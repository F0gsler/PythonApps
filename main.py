from tkinter import *

def submitBudget():
    totalBudget = entry.get()
    print(totalBudget)

def deleteBudget():
    totalBudget = entry.delete(0, END)
    print(totalBudget)

window = Tk()
window.geometry("400x400")
window.title("Budget App")

logo = PhotoImage(file="logo.png")
window.iconphoto(True,logo)
window.configure(background="#0f1117")

submit = Button(window, text="Submit", fg="white", bg="#4f8ef7",
                activebackground="#6ba3ff", activeforeground="white",
                relief="flat", font=("Helvetica", 11, "bold"),
                cursor="hand2", command=submitBudget, padx=16, pady=6)
submit.pack(side="right", padx=(0, 10), pady=10)

delete = Button(window, text="Delete", fg="white", bg="#e05252",
                activebackground="#f07070", activeforeground="white",
                relief="flat", font=("Helvetica", 11, "bold"),
                cursor="hand2", command=deleteBudget, padx=16, pady=6)
delete.pack(side="right", pady=10)

showTotalBudget = Label(window, text="Total Budget: ", fg="#7c8099",
                        bg="#0f1117", font=("Helvetica", 11))
showTotalBudget.pack()

entry = Entry(window, fg="#e8eaf0", bg="#1c1f2b", insertbackground="#4f8ef7",
              relief="flat", font=("Helvetica", 13),
              highlightthickness=1, highlightbackground="#2a2d3d",
              highlightcolor="#4f8ef7", width=20)
entry.config(fg="#e8eaf0", bg="#1c1f2b")
entry.pack(side="left", padx=10, ipady=6)

window.mainloop()