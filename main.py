import tkinter

def run_nullifier():
    main_window = tkinter.Tk()

    main_window.configure(bg='')
    main_window.wm_attributes('-fullscreen', True)

    main_window.title("Virtual Input Nullifier")
    main_window.iconbitmap("danger_skull.ico")

    main_window.mainloop()

run_nullifier()
