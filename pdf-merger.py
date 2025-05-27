import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger


def select_files():
    files = filedialog.askopenfilenames(filetypes=[("PDF Dateien", "*.pdf")])
    if len(files) > 8:
        messagebox.showerror("Fehler", "Maximal 8 PDFs erlaubt!")
    else:
        listbox.delete(0, tk.END)
        for file in files:
            listbox.insert(tk.END, file)


def merge_pdfs():
    files = list(listbox.get(0, tk.END))
    if not files:
        messagebox.showerror("Fehler", "Bitte wähle bis zu 6 PDFs aus.")
        return

    output_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Dateien", "*.pdf")])
    if not output_file:
        return

    merger = PdfMerger()
    for file in files:
        merger.append(file)

    merger.write(output_file)
    merger.close()
    messagebox.showinfo("Erfolg", f"PDFs erfolgreich als '{output_file}' gespeichert.")


app = tk.Tk()
app.title("PDF Merger")
app.geometry("400x250")

tk.Label(app, text="Wähle bis zu 8 PDF-Dateien aus").pack(pady=5)
btn_select = tk.Button(app, text="Dateien auswählen", command=select_files)
btn_select.pack(pady=5)

listbox = tk.Listbox(app, width=50, height=6,bg="white",fg="black",borderwidth=2,relief="solid")

listbox.pack(pady=5)


btn_merge = tk.Button(app, text="PDFs zusammenführen", command=merge_pdfs)
btn_merge.pack(pady=10)

app.mainloop()
