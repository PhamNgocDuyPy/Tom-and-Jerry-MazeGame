from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import os

# ----------ĐỊNH NGHĨA CÁC BIẾN----------
FONT = 'Open Sans'
BACKGROUND_COLOR_1 = 'SlateBlue1'
BACKGROUND_COLOR_3 = 'SlateBlue3'
FONT_SIZE = 22

accountSystem = Tk()  # Tạo 1 cửa sổ giao diện chính
window_height = 720
window_width = 1280
screen_width = accountSystem.winfo_screenwidth()
screen_height = accountSystem.winfo_screenheight()

x_cor = int((screen_width / 2) - (window_width / 2))
y_cor = int((screen_height / 2) - (window_height / 2))
accountSystem.rowconfigure(0, weight=1)  # Các dòng sẽ được hiển thị trên toàn bộ cửa sổ
accountSystem.columnconfigure(0, weight=1)  # Các cột sẽ được hiển thị trên toàn bộ cửa sổ

accountSystem.geometry('{}x{}+{}+{}'.format(window_width, window_height, x_cor,
                                            y_cor))  # cửa sổ có kích thước 1280x720 pixel và đặt vị trí x = 400, y = 150
accountSystem.title('ACCOUNT SYSTEM')  # Đặt tên cửa sổ là "ACCOUNT SYSTEM"

# Tạo 3 Frame cho 3 trang SIGN_IN_PAGE, SIGN_UP_PAGE và RESET_PASSWORD_PAGE
SIGN_IN_PAGE = Frame(accountSystem)
SIGN_UP_PAGE = Frame(accountSystem)
RESET_PASSWORD_PAGE = Frame(accountSystem)

# Liên kết giữa 3 trang SIGN_IN_PAGE, SIGN_UP_PAGE và RESET_PASSWORD_PAGE
for frame in (SIGN_IN_PAGE, SIGN_UP_PAGE, RESET_PASSWORD_PAGE):
    frame.grid(row=0, column=0, sticky='nsew')
    # sticky = 'nsew' đảm bảo cửa sổ lấp đầy không gian có sẵn theo mọi hướng (north, south, east, west).


# sử dụng phương thức tkraise để đưa khung (frame) thành khung hiển thị
def show_frame(frame):
    frame.tkraise()


show_frame(SIGN_IN_PAGE)  # hiện thị trang đăng nhập lên màn hình cửa sổ


# -----------------------------------------------------------------
# -------------------------SIGN IN---------------------------------
# -----------------------------------------------------------------

# ----------FUNCTIONAL PART----------
def signin_hide():  # ấn biểu tượng mắt nhắm -> mật khẩu có dạng * và biểu tượng mắt mở hiện ra
    signin_closeeye.config(file='images/close_eye.png')  # hiện biểu tượng mắt nhắm
    signin_passwordEntry.config(show='*')  # mật khẩu có dạng *
    signin_eyeButton.config(command=signin_show)  # biểu tượng mắt mở hiện ra


def signin_show():  # ấn biểu tượng mắt mở -> mật khẩu hiện bình thường và biểu tượng mắt nhắm hiện ra
    signin_closeeye.config(file='images/open_eye.png')  # hiện biểu tượng mắt mở
    signin_passwordEntry.config(show='')  # mật khẩu về trạng thái hiển thị bình thường
    signin_eyeButton.config(command=signin_hide)  # biểu tượng nhắm mắt hiện ra


def signin_user_enter(event):  # Khi ấn vào ô Username, chữ 'Username' bị xóa
    if signin_usernameEntry.get() == 'Username':
        signin_usernameEntry.delete(0, END)  # Xóa các phần tử từ vị trí đầu đến cuối (ở đây là chữ 'Username')


def signin_password_enter(event):  # Khi ấn vào ô password chữ 'Password' bị xóa
    if signin_passwordEntry.get() == 'Password':
        signin_passwordEntry.delete(0, END)
        signin_passwordEntry.config(show='*')  # Nội dung khi nhập sẽ hiển thị ra cửa sổ với dạng kí tự *


def signin():
    if signin_usernameEntry.get() == '' or signin_passwordEntry.get() == '':  # kiểm tra các ô có được điền hay chưa
        messagebox.showerror('Error', 'All Fields are required!')  # Nếu chưa thì hiện thông báo lỗi
    else:
        if os.path.exists(
                f"database/player/{signin_usernameEntry.get()}.txt"):  # Kiểm tra xem tên người dùng có tồn tại không
            with open(f"database/player/{signin_usernameEntry.get()}.txt",
                      "r") as file:  # Mở file tương ứng với tên người dùng
                if signin_passwordEntry.get() == file.readline():  # Kiểm tra xem mật khẩu có khớp không
                    messagebox.showinfo("Login successful!",
                                        "Login successful!")  # Hiển thị thông báo thành công
                    accountSystem.destroy()  # tắt cửa sổ khi Sign in thành công

                else:
                    messagebox.showerror("Invalid username or password!",
                                         "Invalid username or password!")  # Hiển thị thông báo lỗi
        else:
            messagebox.showerror("Invalid username or password!", "Invalid username or password!")


# ----------BACKGROUND IMAGE----------
# Load background image
signin_bgImage = ImageTk.PhotoImage(file='images/sign_in.jpg')
signin_bgLabel = Label(SIGN_IN_PAGE, image=signin_bgImage)
signin_bgLabel.place(x=0, y=0)

# Tạo nhãn 'Sign in' tại tọa độ x, y
signin_heading = Label(SIGN_IN_PAGE, text='SIGN IN', font=(FONT, 27, 'bold'), bg=BACKGROUND_COLOR_1, fg='white')
signin_heading.place(x=790, y=175)

# ----------USERNAME----------
# Tạo nhãn Username và ô nhập thông tin Username
signin_usernameEntry = Entry(SIGN_IN_PAGE, width=21, font=(FONT, FONT_SIZE, 'bold'), bg=BACKGROUND_COLOR_1,
                             fg='white', bd=0)  # Tạo khung nhập thông tin
signin_usernameEntry.place(x=680, y=276)  # Tọa độ khung
signin_usernameEntry.insert(0, 'Username')  # Ghi nội dung "Username" vào vị trí đầu của khung (textbox)
signin_usernameEntry.bind('<FocusIn>', signin_user_enter)  # Xóa chữ 'Username' khi người dùng ấn vào khung

# ----------PASSWORD---------
# Tạo nhãn Password và ô nhập thông tin Password
signin_passwordEntry = Entry(SIGN_IN_PAGE, width=18, font=(FONT, FONT_SIZE, 'bold'), bg=BACKGROUND_COLOR_1,
                             fg='white', bd=0)
signin_passwordEntry.place(x=680, y=357)
signin_passwordEntry.insert(0, 'Password')
signin_passwordEntry.bind('<FocusIn>', signin_password_enter)

# Tạo nút ẩn, hiện password
signin_closeeye = PhotoImage(file='images/close_eye.png')
signin_eyeButton = Button(SIGN_IN_PAGE, image=signin_closeeye, bd=0, bg=BACKGROUND_COLOR_1,
                          activebackground=BACKGROUND_COLOR_1, cursor='hand2', command=signin_show)
signin_eyeButton.place(x=970, y=348)

# ----------FORGET PASSWORD----------
# Tạo mục "Forget Password
signin_forgetButton = Button(SIGN_IN_PAGE, text='Forgot Password?', bd=0, bg=BACKGROUND_COLOR_3,
                             activebackground=BACKGROUND_COLOR_3, cursor='hand2', font=(FONT, 13, 'bold'),
                             fg='white', activeforeground='white',
                             command=lambda: show_frame(RESET_PASSWORD_PAGE))
signin_forgetButton.place(x=680, y=460)

# ----------LOG IN---------
signin_loginButton = Button(SIGN_IN_PAGE, text='Sign In', font=(FONT, FONT_SIZE - 2, 'bold'),
                            bg=BACKGROUND_COLOR_1, fg='white', activeforeground='white',
                            activebackground=BACKGROUND_COLOR_1, cursor='hand2', bd=0, command=signin)
signin_loginButton.place(x=868, y=445)

# ----------CREATE NEW ACCOUNT----------
# Tạo nhãn hỏi người dùng 'Don't have an account?'
signin_signupLabel = Label(SIGN_IN_PAGE, text="Don't have an account?", font=(FONT, 13, 'bold'),
                           bg=BACKGROUND_COLOR_3, fg='white', bd=0)
signin_signupLabel.place(x=710, y=535)

# Tạo nút 'Sign Up', chuyển người dùng đến trang sign_up
signin_signupButton = Button(SIGN_IN_PAGE, text='Sign Up', font=(FONT, 13, 'bold underline'), fg='white',
                             bg=BACKGROUND_COLOR_3, activeforeground='white',
                             activebackground=BACKGROUND_COLOR_3, cursor='hand2', bd=0,
                             command=lambda: show_frame(SIGN_UP_PAGE))  # Liên kết người dùng đến trang sign_up
signin_signupButton.place(x=905, y=530)


# --------------------------------------------------------------------
# -------------------------SIGN UP------------------------------------
# --------------------------------------------------------------------

# ----------fUCNTIONAL PART----------
def signup_hide():
    signup_closeeye.config(file='images/close_eye.png')
    signup_passwordEntry.config(show='*')
    signup_eyeButton.config(command=signup_show)


def signup_show():
    signup_closeeye.config(file='images/open_eye.png')
    signup_passwordEntry.config(show='')
    signup_eyeButton.config(command=signup_hide)


def signup_user_enter(event):
    if signup_usernameEntry.get() == 'Username':
        signup_usernameEntry.delete(0, END)


def signup_password_enter(event):
    if signup_passwordEntry.get() == 'Password':
        signup_passwordEntry.delete(0, END)
        signup_passwordEntry.config(show='*')


def signup_confirmpassword_enter(event):
    if signup_confirmpasswordEntry.get() == 'Confirm Password':
        signup_confirmpasswordEntry.delete(0, END)
        signup_confirmpasswordEntry.config(show='*')


def signup_clear():
    signup_usernameEntry.delete(0, END)
    signup_passwordEntry.delete(0, END)
    signup_confirmpasswordEntry.delete(0, END)


def connect_database():
    if signup_usernameEntry.get() == '' or signup_passwordEntry.get() == '' or signup_confirmpasswordEntry.get() == '':
        messagebox.showerror('Error', 'All Fields are required')
    elif signup_passwordEntry.get() != signup_confirmpasswordEntry.get():
        messagebox.showerror('Error', 'Password Mismatch')
    else:
        try:
            os.makedirs(f"database/player")
        except:
            if os.path.exists(
                    f"database/player/{signup_usernameEntry.get()}.txt"):  # Kiểm tra xem tên người dùng có tồn tại không
                messagebox.showerror("Username existed!", "Username existed!")  # Hiển thị thông báo lỗi
            elif signup_passwordEntry.get() == signup_confirmpasswordEntry.get():  # Kiểm tra xem mật khẩu và mật khẩu nhập lại có khớp không
                with open(f"database/player/{signup_usernameEntry.get()}.txt",
                          "w") as file:  # Tạo một file mới với tên người dùng
                    file.write(signup_passwordEntry.get())  # Ghi mật khẩu vào dòng đầu tiên của file
                messagebox.showinfo("Register successful!",
                                    "Register successful!")  # Hiển thị thông báo thành công
                signup_clear()  # Xóa các thông tin đã nhập trên màn hình
                show_frame(SIGN_IN_PAGE)
            else:
                messagebox.showerror("Passwords do not match!",
                                     "Passwords do not match!")  # Hiển thị thông báo lỗi


# ----------BACKGROUND IMAGE----------
signup_bgImage = ImageTk.PhotoImage(file='images/sign_up.jpg')
signup_bgLabel = Label(SIGN_UP_PAGE, image=signup_bgImage)
signup_bgLabel.place(x=0, y=0)

signup_heading = Label(SIGN_UP_PAGE, text='SIGN UP', font=(FONT, 27, 'bold'), bg=BACKGROUND_COLOR_1, fg='white')
signup_heading.place(x=790, y=174)

# ----------USERNAME----------
signup_usernameEntry = Entry(SIGN_UP_PAGE, width=21, font=(FONT, FONT_SIZE, 'bold'), bg=BACKGROUND_COLOR_1,
                             fg='white', bd=0)
signup_usernameEntry.place(x=680, y=253)
signup_usernameEntry.insert(0, 'Username')
signup_usernameEntry.bind('<FocusIn>', signup_user_enter)

# ----------PASSWORD----------
signup_passwordEntry = Entry(SIGN_UP_PAGE, width=18, font=(FONT, FONT_SIZE, 'bold'), bg=BACKGROUND_COLOR_1,
                             fg='white', bd=0)
signup_passwordEntry.place(x=680, y=325)
signup_passwordEntry.insert(0, 'Password')
signup_passwordEntry.bind('<FocusIn>', signup_password_enter)

signup_closeeye = PhotoImage(file='images/close_eye.png')
signup_eyeButton = Button(SIGN_UP_PAGE, image=signup_closeeye, bd=0, bg=BACKGROUND_COLOR_1,
                          activebackground=BACKGROUND_COLOR_1, cursor='hand2', command=signup_show)
signup_eyeButton.place(x=970, y=315)

# ----------CONFIRM PASSWORD----------
signup_confirmpasswordEntry = Entry(SIGN_UP_PAGE, width=21, font=(FONT, FONT_SIZE, 'bold'),
                                    bg=BACKGROUND_COLOR_1, fg='white', bd=0)
signup_confirmpasswordEntry.place(x=680, y=395)
signup_confirmpasswordEntry.insert(0, 'Confirm Password')
signup_confirmpasswordEntry.bind('<FocusIn>', signup_confirmpassword_enter)

# ----------REGISTER----------
signup_registerButton = Button(SIGN_UP_PAGE,
                               text='Sign Up',
                               font=(FONT, FONT_SIZE - 2, 'bold'),
                               bg=BACKGROUND_COLOR_1, fg='white',
                               activeforeground='white',
                               activebackground=BACKGROUND_COLOR_1,
                               cursor='hand2', bd=0,
                               command=connect_database)
signup_registerButton.place(x=800, y=463)

# ----------SIGN IN----------
signup_signinLabel = Label(SIGN_UP_PAGE, text="Already have an account?", font=(FONT, 13, 'bold'),
                           bg=BACKGROUND_COLOR_3, fg='white', bd=0)
signup_signinLabel.place(x=740, y=545)

signup_signinButton = Button(SIGN_UP_PAGE, text='Sign In', font=(FONT, 13, 'bold underline'), fg='white',
                             bg=BACKGROUND_COLOR_3, activeforeground='white',
                             activebackground=BACKGROUND_COLOR_3, cursor='hand2', bd=0,
                             command=lambda: show_frame(SIGN_IN_PAGE))  # Liên kết người dùng đến trang sign_in
signup_signinButton.place(x=950, y=541)


# -----------------------------------------------------------------
# -------------------------FORGOT PASSWORD-------------------------
# -----------------------------------------------------------------

def forgot_hide():
    forgot_closeeye.config(file='images/close_eye.png')
    forgot_passwordEntry.config(show='*')
    forgot_eyeButton.config(command=forgot_show)


def forgot_show():
    forgot_closeeye.config(file='images/open_eye.png')
    forgot_passwordEntry.config(show='')
    forgot_eyeButton.config(command=forgot_hide)


def forgot_user_enter(event):
    if forgot_usernameEntry.get() == 'Username':
        forgot_usernameEntry.delete(0, END)


def forgot_password_enter(event):
    if forgot_passwordEntry.get() == 'New Password':
        forgot_passwordEntry.delete(0, END)
        forgot_passwordEntry.config(show='*')


def forgot_confirmpassword_enter(event):
    if forgot_confirmpasswordEntry.get() == 'Confirm New Password':
        forgot_confirmpasswordEntry.delete(0, END)
        forgot_confirmpasswordEntry.config(show='*')


def change_database():
    if forgot_usernameEntry.get() == '' or forgot_passwordEntry.get() == '' or forgot_confirmpasswordEntry.get() == '':
        messagebox.showerror('Error', 'All Fields are required')
    elif forgot_passwordEntry.get() != forgot_confirmpasswordEntry.get():
        messagebox.showerror('Error', 'Password Mismatch')
    else:
        if not os.path.exists(
                f"database/player/{forgot_usernameEntry.get()}.txt"):  # Kiểm tra xem tên người dùng có tồn tại không
            messagebox.showerror("Username doesn't exist!", "Username doesn't exist!")  # Hiển thị thông báo lỗi
        elif forgot_passwordEntry.get() == forgot_confirmpasswordEntry.get():  # Kiểm tra xem mật khẩu và mật khẩu nhập lại có khớp không
            with open(f"database/player/{forgot_usernameEntry.get()}.txt",
                      "w") as file:  # Mở file với tên người dùng cần đổi mật khẩu
                file.write(forgot_passwordEntry.get())  # Ghi đè mật khẩu vào dòng đầu tiên của file
            messagebox.showinfo("Reset password successful!",
                                "Reset password successful!")  # Hiển thị thông báo thành công
            show_frame(SIGN_IN_PAGE)
        else:
            messagebox.showerror("Passwords do not match!", "Passwords do not match!")  # Hiển thị thông báo lỗi


# ----------BACKGROUND IMAGE----------
forgot_bgImage = ImageTk.PhotoImage(file='images/sign_up.jpg')
forgot_bgLabel = Label(RESET_PASSWORD_PAGE, image=forgot_bgImage)
forgot_bgLabel.place(x=0, y=0)

# Tạo nhãn RESET PASSWORD
forgot_heading = Label(RESET_PASSWORD_PAGE, text='RESET', font=(FONT, 27, 'bold'), bg=BACKGROUND_COLOR_1,
                       fg='white')
forgot_heading.place(x=800, y=174)

# ----------USERNAME----------
forgot_usernameEntry = Entry(RESET_PASSWORD_PAGE, width=21, font=(FONT, FONT_SIZE, 'bold'),
                             bg=BACKGROUND_COLOR_1, fg='white', bd=0)
forgot_usernameEntry.place(x=680, y=253)
forgot_usernameEntry.insert(0, 'Username')
forgot_usernameEntry.bind('<FocusIn>', forgot_user_enter)

# ----------NEW PASSWORD----------
forgot_passwordEntry = Entry(RESET_PASSWORD_PAGE, width=21, font=(FONT, FONT_SIZE, 'bold'),
                             bg=BACKGROUND_COLOR_1, fg='white', bd=0)
forgot_passwordEntry.place(x=680, y=325)
forgot_passwordEntry.insert(0, 'New Password')
forgot_passwordEntry.bind('<FocusIn>', forgot_password_enter)

forgot_closeeye = PhotoImage(file='images/close_eye.png')
forgot_eyeButton = Button(RESET_PASSWORD_PAGE, image=forgot_closeeye, bd=0, bg=BACKGROUND_COLOR_1,
                          activebackground=BACKGROUND_COLOR_1, cursor='hand2', command=forgot_show)
forgot_eyeButton.place(x=970, y=315)

# ----------CONFIRM NEW PASSWORD----------
forgot_confirmpasswordEntry = Entry(RESET_PASSWORD_PAGE, width=21, font=(FONT, FONT_SIZE, 'bold'),
                                    bg=BACKGROUND_COLOR_1, fg='white', bd=0)
forgot_confirmpasswordEntry.place(x=680, y=395)
forgot_confirmpasswordEntry.insert(0, 'Confirm New Password')
forgot_confirmpasswordEntry.bind('<FocusIn>', forgot_confirmpassword_enter)

# ----------SUBMIT----------
forgot_submitButton = Button(RESET_PASSWORD_PAGE, text='Submit', font=(FONT, FONT_SIZE, 'bold'),
                             bg=BACKGROUND_COLOR_1, fg='white', activeforeground='white',
                             activebackground=BACKGROUND_COLOR_1, cursor='hand2', bd=0, command=change_database)
forgot_submitButton.place(x=800, y=460)

# Tạo nút 'Create new account' và 'Signup', chuyển người dùng đến trang sign_up hoặc sign_in
forgot_signupButton = Button(RESET_PASSWORD_PAGE, text='Sign Up', font=(FONT, 13, 'bold underline'), fg='white',
                             bg=BACKGROUND_COLOR_3, activeforeground='white',
                             activebackground=BACKGROUND_COLOR_3, cursor='hand2', bd=0,
                             command=lambda: show_frame(SIGN_UP_PAGE))  # Liên kết người dùng đến trang sign_up
forgot_signupButton.place(x=780, y=541)

forgot_text = Label(RESET_PASSWORD_PAGE, text='or', font=(FONT, 13, 'bold'), fg='white', bg=BACKGROUND_COLOR_3)
forgot_text.place(x=855, y=543)

forgot_signinButton = Button(RESET_PASSWORD_PAGE, text='Sign In', font=(FONT, 13, 'bold underline'), fg='white',
                             bg=BACKGROUND_COLOR_3, activeforeground='white',
                             activebackground=BACKGROUND_COLOR_3, cursor='hand2', bd=0,
                             command=lambda: show_frame(SIGN_IN_PAGE))  # Liên kết người dùng đến trang sign_in
forgot_signinButton.place(x=885, y=541)

# ----------------------#
# ---------MAIN---------#
# ----------------------#
accountSystem.resizable(0, 0)
accountSystem.mainloop()
