import tkinter as tk
from tkinter import filedialog

def count_sequence(sequence):
    counts = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    for base in sequence:
        if base in counts:
            counts[base] += 1
    return counts

def sequence_counter():
    sequence = manual_entry.get().upper()
    if not sequence:
        file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                sequence = file.read().upper()
    result = count_sequence(sequence)
    result_text.set(f'A: {result["A"]}, T: {result["T"]}, C: {result["C"]}, G: {result["G"]}')

# Create the main window
root = tk.Tk()
root.title("Sequence Counter with File Handling")

# Create and pack widgets
tk.Label(root, text="Sequence Counter", font=("Helvetica", 16)).pack(pady=10)

file_button = tk.Button(root, text="Open File", command=sequence_counter, padx=10, pady=5, bg="#4CAF50", fg="white", font=("Helvetica", 12))
file_button.pack(pady=5)

manual_label = tk.Label(root, text="Enter sequence manually:", font=("Helvetica", 12))
manual_label.pack(pady=5)

manual_entry = tk.Entry(root, width=40, font=("Helvetica", 12))
manual_entry.pack(pady=5)

manual_button = tk.Button(root, text="Count Sequence", command=sequence_counter, padx=10, pady=5, bg="#4CAF50", fg="white", font=("Helvetica", 12))
manual_button.pack(pady=20)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=("Helvetica", 12))
result_label.pack(pady=10)

# Start the main loop
root.mainloop()
