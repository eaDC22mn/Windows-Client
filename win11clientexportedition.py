import tkinter as tk
from tkinter import messagebox
import os

def show_new_message():
    os.system(r'"C:\XXXXX\AppData\Local\Programs\Microsoft VS Code\Code.exe"')

def show_message():
    os.system(r'"C:\Program Files (x86)\Inno Setup 6\Compil32.exe"')
    
def open_writable_box():
    writable_window = tk.Toplevel()
    writable_window.title("PY Notepad")
    writable_window.geometry("400x300")

    text_box = tk.Text(writable_window, wrap='word', width=40, height=10)
    text_box.pack(pady=15)

    def save_text():
        text_content = text_box.get("1.0", tk.END).strip()
        save_path = r'C:\Users\XXXXX\OneDrive\Desktop\PY notepad saves\saved_text.txt'
        
        try:
            with open(save_path, 'w') as file:
                file.write(text_content)
            messagebox.showinfo("Success", f"Text saved to {save_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save text: {e}")

    save_button = tk.Button(writable_window, text="Save", command=save_text)
    save_button.pack(pady=10)

def open_IPbox_box():
    ip_window = tk.Toplevel()
    ip_window.title("IP Logger")
    ip_window.geometry("300x100")



    text_box = tk.Text(ip_window, wrap='word', width=26, height=1)
    text_box.pack(pady=10)
    def save_ip():
        text_content = text_box.get("1.0", tk.END).strip()
        save_path = r'C:\Users\XXXXX\OneDrive\Desktop\Logged IPs\Logged IP.txt'
      
        try:
            with open(save_path, 'w') as file:
                file.write(text_content)
            messagebox.showinfo("Success", f"Text saved to {save_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save text: {e}")

    

    save_button = tk.Button(ip_window, text="Log IP", command=save_ip)
    save_button.pack(pady=20)

    

            

    

    

def main():
    global root
    root = tk.Tk()
    root.title("PY script Client")
    root.geometry("300x600")

    long_text = (
        "Welcome to the Main window of the Python WIndows Client!  "
        "Various programs with various uses can be found on the Client launcher. "
        "Click [End Session] to close the launcher."
    )
    
    label = tk.Label(root, text=long_text, wraplength=300)
    label.pack(pady=10)

    def close_program():
        root.quit()

    
        


    tk.Button(root, text="Run Inno setup", command=show_message).pack(pady=5)
    tk.Button(root, text="Run MS visual studio", command=show_new_message).pack(pady=5)
    tk.Button(root, text="Open PY notepad", command=open_writable_box).pack(pady=5)
    tk.Button(root, text="IP Logger", command=open_IPbox_box).pack(pady=5)
   



    def open_second_window():
        second_window = tk.Toplevel()
        second_window.title("PY gamebar module")
        second_window.geometry("400x300")

        label = tk.Label(second_window, text="Gamebar Module. CLick [close Module] to close.")
        label.pack(pady=10)

        def show_secondary_message():
            os.system(r'"C:\XboxGames\Minecraft Launcher\Content\Minecraft.exe"')


        def show_secondary_messageHH():
            os.system(r'"%LocalAppData%\Discord\Update.exe" --processStart Discord.exe')

        def close_second_window():
            second_window.destroy()

        def Run_spotify():
            os.system(r'"C:\Users\XXXXX\AppData\Local\Microsoft\WindowsApps\Spotify.exe"')

       
            

        tk.Button(second_window, text="Run Minecraft Launcher", command=show_secondary_message).pack(pady=3)
        tk.Button(second_window, text="Run Discord", command=show_secondary_messageHH).pack(pady=3)
        tk.Button(second_window, text="Run Spotify", command=Run_spotify).pack(pady=3)
        tk.Button(second_window, text="Close PY gamebar module", command=close_second_window).pack(pady=3)

    def duplicate_main_window():
     duplicate_window = tk.Toplevel()
     duplicate_window.title("Duplicate Main Window")
     duplicate_window.geometry("300x600")

     long_text = (
        "Welcome to the Duplicate Main window of the Python Windows Client!  "
        "Various programs with various uses can be found on the Client launcher. "
        "Click [End Session] to close the launcher."
     )
    
     label = tk.Label(duplicate_window, text=long_text, wraplength=300)
     label.pack(pady=10)

     def close_duplicate():
        duplicate_window.destroy()

     tk.Button(duplicate_window, text="Run Inno setup", command=show_message).pack(pady=5)
     tk.Button(duplicate_window, text="Run MS visual studio", command=show_new_message).pack(pady=5)
     tk.Button(duplicate_window, text="Open PY notepad", command=open_writable_box).pack(pady=5)
     tk.Button(duplicate_window, text="IP Logger", command=open_IPbox_box).pack(pady=5)
     tk.Button(duplicate_window, text="End Duplicate Session", command=close_duplicate).pack(pady=5)
    








    def shutdownmodu():
        shutdownmodu = tk.Toplevel()
        shutdownmodu.title("Shut Down  (2s delay)")
        shutdownmodu.geometry("150x120")

        label = tk.Label(shutdownmodu, text="")
        label.pack(pady=5)
         
        def shutdownpc():
            os.system("shutdown /s /t 2")
            root.deiconify

        def restartpc():
            os.system("restart /s /t 5")
            root.deiconify

        tk.Button(shutdownmodu, text="Shut down", command=shutdownpc).pack(pady=1)
        tk.Button(shutdownmodu, text="Close and Restart", command=restartpc).pack(pady=1)


    def open_third_window():
        third_window = tk.Toplevel()
        third_window.title("Utilities Module")
        third_window.geometry("400x300")

        label = tk.Label(third_window, text="Utility Module, press [close module] to destroy window.")
        label.pack(pady=10)

        def close_third_window():
            third_window.destroy()

        def Run_msteams():
            os.system(r'"C:\Users\XXXXX\AppData\Local\Microsoft\WindowsApps\ms-teams.exe msteams:consumer"')

        tk.Button(root, text="Duplicate Main Window", command=duplicate_main_window).pack(pady=5)

        tk.Button(third_window, text="Run MS Teams [personal]", command=Run_msteams).pack(pady=3)
       
        tk.Button(third_window, text="Close module", command=close_third_window).pack(pady=3)
        






    tk.Button(root, text="Utilities Module", command=open_third_window).pack(pady=10) 
    tk.Button(root, text="GB Module", command=open_second_window).pack(pady=10)      
    tk.Button(root, text="Open shutdown Module and close.", command=shutdownmodu).pack(pady=5)
    tk.Button(root, text="End Client session", command=close_program).pack(pady=5)


    root.mainloop()

if __name__ == "__main__":
    main()
