from tkinter import *
from tkinter import ttk
from translate import Translator

def translate_text():
    text = input_text.get("1.0", END).strip() # Get input text from tkinter Text widget
    src_lang = src_language_var.get() # Get selected source language from tkinter OptionMenu
    dest_lang = dest_language_var.get() # Get selected destination language from tkinter OptionMenu
    
    if text and src_lang and dest_lang:
        translator = Translator(from_lang=src_lang, to_lang=dest_lang)
        translated_text = translator.translate(text)
        output_text.delete("1.0", END) # Clear output Text widget
        output_text.insert(END, translated_text) # Update output Text widget with translated text
    else:
        output_text.delete("1.0", END) # Clear output Text widget
        output_text.insert(END, "Please enter text and select source and destination languages.") # Display error message

# Create tkinter window
root = Tk()
root.title("Text Translator")
root.geometry("700x350") # Set window size to 1000px x 800px

# Create style for tkinter widgets
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 14))
style.configure("TButton", font=("Helvetica", 14))

# Create input Text widget
input_text = Text(root, height=5, width=80)
input_text.pack(pady=20)

# Create source language OptionMenu
src_language_var = StringVar(root)
src_language_var.set("en") # Set default source language as English
src_language_optionmenu = ttk.OptionMenu(root, src_language_var, "en", "es", "fr", "de", "ja", "ko", "zh")
src_language_optionmenu.pack()

# Create destination language OptionMenu
dest_language_var = StringVar(root)
dest_language_var.set("es") # Set default destination language as Spanish
dest_language_optionmenu = ttk.OptionMenu(root, dest_language_var, "en", "es", "fr", "de", "ja", "ko", "zh")
dest_language_optionmenu.pack()

# Create translate button
translate_button = ttk.Button(root, text="Translate", command=translate_text)
translate_button.pack(pady=20)

# Create output Text widget
output_text = Text(root, height=5, width=80)
output_text.pack()

# Run tkinter event loop
root.mainloop()
