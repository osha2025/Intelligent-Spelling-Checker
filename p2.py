import tkinter as tk
from textblob import TextBlob

root = tk.Tk()
root.title("Spelling Checker")
root.geometry("700x400")
root.config(background="#dae6f6")

def check_spelling():
    word = enter_text.get()
    blob = TextBlob(word)
    corrected_word = str(blob.correct())
    if word != corrected_word:
        message = f"Original: {word}\nCorrected: {corrected_word}"
    else:
        message = "No errors found!"
    result_label.config(text=message)

heading = tk.Label(root, text="Spelling Checker", font=("Trebuchet MS", 30, "bold"), bg="white")
heading.pack(pady=20)

enter_text = tk.Entry(root, justify="center", width=30, font=("poppins", 25), bg="white")
enter_text.pack(pady=10)
enter_text.focus()

check_button = tk.Button(root, text="Check", font=("arial", 20, "bold"), fg="white", bg="red", command=check_spelling)
check_button.pack(pady=10)

result_label = tk.Label(root, font=("poppins", 20), bg="#dae6f6", fg="#364971")
result_label.pack(pady=20)

root.mainloop()
