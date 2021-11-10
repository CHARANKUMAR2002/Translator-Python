from tkinter import *
from googletrans import Translator
from tkinter import messagebox, ttk
from gtts import gTTS
from PIL import Image, ImageTk
import playsound
import os
from clipboard import copy


root = Tk()
root.config(bg='black')
root.geometry('600x285')
root.title('Translator v2.0')
root.resizable(False, False)

separate = Frame(root, bg='white')
separate.pack(expand=1, fill='y')
Label(separate, text="").pack()

t = Translator()

Label(root, text='Translate From...', font=('times', 14, 'italic'), bg='black', fg='white').place(x=6, y=10)

input_content = Text(root, width=34, height=9, font=('times', 12, 'bold'), bg='black', fg='white')
input_content.place(x=10, y=80)

Label(root, text='Translated...', font=('times', 14, 'italic'), bg='black', fg='white').place(x=310, y=10)

output_language = ttk.Combobox(root, width=15, state='readonly')
output_language['values'] = ['Select Language', 'Tamil', 'Malayalam', 'Kannada', 'Telugu', 'Hindi', 'Bengali', 'Urdu', 'Italian', 'Japanese', 'Chinese', 'Arabic', 'English', 'Thai', 'French', 'Swedish', 'Russian', 'Spanish', 'German', 'Turkish', 'Portuguese', 'Dutch', 'Korean', 'Greek', 'Indonesian', 'Serbian']
output_language.current(0)
output_language.place(x=315, y=50)

output_content = Text(root, width=34, height=9, font=('times', 12, 'bold'), bg='black', fg='white')
output_content.place(x=315, y=80)


def trans():
    in_con = input_content.get(0.0, END)
    
    out_lang = output_language.get()


    if len(input_content.get(0.0, END)) != 1 :
        global translated_content
        
        if out_lang == 'Chinese':
            translated_content = t.translate(in_con, dest='zh-TW')
            output_content.insert(0.0, translated_content.text)
        
        elif out_lang == "Select Language":
            messagebox.showerror("Translator", "Select A Language")
                
        else:
            translated_content = t.translate(in_con, dest=out_lang)
            output_content.delete(0.0, END)
            output_content.insert(0.0, translated_content.text)
    
    else:
        messagebox.showerror("Translator", "Content Not Given To Translate")


def copy_to_clipboard():
    content = len(output_content.get(0.0, END))
    if content == 1:
        messagebox.showerror('Translator', 'No Content To Copy on Clipboard')
    else:
        copy(output_content.get(0.0, END))
        messagebox.showinfo("Translator", "Content Copied To Clipboard")
        


def clear_input():
    input_content.delete(0.0, END)


def clear_output():
    output_content.delete(0.0, END)


def speak_input():
    content = len(input_content.get(0.0, END))
    if content != 1:
        in_l = input_content.get(0.0, END)
        audio = gTTS(text=in_l)
        audio.save("Original.mp3")
        playsound.playsound("Original.mp3")
        root.update_idletasks()
        os.remove("Original.mp3")
    else:
        messagebox.showerror("Translator", "No Content To Speak")


def speak_output():
    out = output_language.get()
    content = len(output_content.get(0.0, END))
    if content != 1:
        if out == 'Tamil':
            audio = gTTS(text=translated_content.text, lang='ta')
            audio.save("Translated.mp3")
            playsound.playsound("Translated.mp3")
            root.update_idletasks()
            os.remove("Translated.mp3")
        elif out == 'Malayalam':
            audio = gTTS(text=translated_content.text, lang='ml')
            audio.save("Translated.mp3")
            playsound.playsound("Translated.mp3")
            root.update_idletasks()
            os.remove("Translated.mp3")
        elif out == 'Kannada':
            audio = gTTS(text=translated_content.text, lang='kn')
            audio.save("Translated.mp3")
            playsound.playsound("Translated.mp3")
            root.update_idletasks()
            os.remove("Translated.mp3")
        elif out == 'Telugu':
            audio = gTTS(text=translated_content.text, lang='te')
            audio.save("Translated.mp3")
            playsound.playsound("Translated.mp3")
            root.update_idletasks()
            os.remove("Translated.mp3")
        elif out == 'Hindi':
            audio = gTTS(text=translated_content.text, lang='hi')
            audio.save("Translated.mp3")
            playsound.playsound("Translated.mp3")
            root.update_idletasks()
            os.remove("Translated.mp3")
        elif out == 'Urdu':
            audio = gTTS(text=translated_content.text, lang='ur')
            audio.save("Translated.mp3")
            playsound.playsound("Translated.mp3")
            root.update_idletasks()
            os.remove("Translated.mp3")
        elif out == 'Italian':
            audio = gTTS(text=translated_content.text, lang='it')
            audio.save("Translated.mp3")
            playsound.playsound("Translated.mp3")
            root.update_idletasks()
            os.remove("Translated.mp3")
        elif out == 'Japanese':
            audio = gTTS(text=translated_content.text, lang='ja')
            audio.save("Translated.mp3")
            playsound.playsound("Translated.mp3")
            root.update_idletasks()
            os.remove("Translated.mp3")
        elif out == 'Chinese':
            audio = gTTS(text=translated_content.text, lang='zh-TW')
            audio.save("Translated.mp3")
            playsound.playsound("Translated.mp3")
            root.update_idletasks()
            os.remove("Translated.mp3")
        elif out == 'English':
            audio = gTTS(text=translated_content.text, lang='en')
            audio.save("Translated.mp3")
            playsound.playsound("Translated.mp3")
            root.update_idletasks()
            os.remove("Translated.mp3")
        elif out == 'Thai':
            audio = gTTS(text=translated_content.text, lang='th')
            audio.save("Translated.mp3")
            playsound.playsound("Translated.mp3")
            root.update_idletasks()
            os.remove("Translated.mp3")
        elif out == 'French':
            audio = gTTS(text=translated_content.text, lang='fr')
            audio.save("Translated.mp3")
            playsound.playsound("Translated.mp3")
            root.update_idletasks()
            os.remove("Translated.mp3")
        elif out == 'Swedish':
            audio = gTTS(text=translated_content.text, lang='sv')
            audio.save("Translated.mp3")
            playsound.playsound("Translated.mp3")
            root.update_idletasks()
            os.remove("Translated.mp3")
        elif out == 'Russian':
            audio = gTTS(text=translated_content.text, lang='ru')
            audio.save("Translated.mp3")
            playsound.playsound("Translated.mp3")
            root.update_idletasks()
            os.remove("Translated.mp3")
        elif out == 'Spanish':
            audio = gTTS(text=translated_content.text, lang='es')
            audio.save("Translated.mp3")
            playsound.playsound("Translated.mp3")
            root.update_idletasks()
            os.remove("Translated.mp3")
        elif out == 'German':
            audio = gTTS(text=translated_content.text, lang='de')
            audio.save("Translated.mp3")
            playsound.playsound("Translated.mp3")
            root.update_idletasks()
            os.remove("Translated.mp3")
        elif out == 'Portuguese':
            audio = gTTS(text=translated_content.text, lang='pt')
            audio.save("Translated.mp3")
            playsound.playsound("Translated.mp3")
            root.update_idletasks()
            os.remove("Translated.mp3")
        elif out == 'Dutch':
            audio = gTTS(text=translated_content.text, lang='nl')
            audio.save("Translated.mp3")
            playsound.playsound("Translated.mp3")
            root.update_idletasks()
            os.remove("Translated.mp3")
        elif out == 'Korean':
            audio = gTTS(text=translated_content.text, lang='ko')
            audio.save("Translated.mp3")
            playsound.playsound("Translated.mp3")
            root.update_idletasks()
            os.remove("Translated.mp3")
        elif out == 'Greek':
            audio = gTTS(text=translated_content.text, lang='el')
            audio.save("Translated.mp3")
            playsound.playsound("Translated.mp3")
            root.update_idletasks()
            os.remove("Translated.mp3")
        elif out == 'Indonesian':
            audio = gTTS(text=translated_content.text, lang='id')
            audio.save("Translated.mp3")
            playsound.playsound("Translated.mp3")
            root.update_idletasks()
            os.remove("Translated.mp3")
        elif out == 'Arabic':
            audio = gTTS(text=translated_content.text, lang='ar')
            audio.save("Translated.mp3")
            playsound.playsound("Translated.mp3")
            root.update_idletasks()
            os.remove("Translated.mp3")
        elif out == 'Bengali':
            audio = gTTS(text=translated_content.text, lang='bn')
            audio.save("Translated.mp3")
            playsound.playsound("Translated.mp3")
            root.update_idletasks()
            os.remove("Translated.mp3")
        elif out == 'Serbian':
            audio = gTTS(text=translated_content.text, lang='sr')
            audio.save("Translated.mp3")
            playsound.playsound("Translated.mp3")
            root.update_idletasks()
            os.remove("Translated.mp3")
        elif out == 'Turkish':
            audio = gTTS(text=translated_content.text, lang='tr')
            audio.save("Translated.mp3")
            playsound.playsound("Translated.mp3")
            root.update_idletasks()
            os.remove("Translated.mp3")
    else:
        messagebox.showerror('Translator', 'No Content Is Translated To Speak')
    

Button(root, text='Translate', command=trans, bd=0, font=('times', 12, 'italic'), bg='black', fg='white', activebackground='black', activeforeground='gray').place(x=60, y=47)

Button(root, text='Clear', command=clear_input,  bd=0, font=('times', 12, 'italic'), bg='black', fg='white', activebackground='black', activeforeground='gray').place(x=150, y=47)

Button(root, text='Clear', command=clear_output,  bd=0, font=('times', 12, 'italic'), bg='black', fg='white', activebackground='black', activeforeground='gray').place(x=450, y=47)

speak = Image.open('speak.png')
speak_button = ImageTk.PhotoImage(speak)

Button(root, image=speak_button, bd=0, bg='black', activebackground='black', command=speak_input).place(x=220, y=57)

Button(root, image=speak_button, bd=0, bg='black', activebackground='black', command=speak_output).place(x=540, y=57)

clip_btn = Image.open('clipboard.png')
clip_icon = ImageTk.PhotoImage(clip_btn)

Button(root, image=clip_icon, command=copy_to_clipboard, bd=0, bg='black', activebackground='black').place(y=52, x=510)

root.mainloop()
