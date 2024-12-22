
import tkinter as tk
from tkinter import messagebox
import smtplib
import random

# Function to generate a 6-digit OTP
def generate_otp():
    return ''.join([str(random.randint(0, 9)) for i in range(6)])

# Function to send OTP to the user's email
def send_otp_via_email(receiver_email, otp):
    try:
        sender_email = 'leelasai7094@gmail.com'  # User email
        sender_password = 'lnkh xduf krfr cvab'  # User App password

        # Set up the Subject & message
        subject = "Your current OTP Code"
        message = f"Subject: {subject}\n\nDon't share the OTP code with anyone. Your OTP is: {otp}. It is valid for 5 minutes."

        # Set up the SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Enable TLS security
            server.login(sender_email,
                         sender_password)  # Log in with email and app password
            server.sendmail(sender_email, receiver_email, message)  # Send the email

        print(f"OTP sent to {receiver_email}.")
        return True
    except Exception as e:
        print(f"Error sending OTP: {e}")
        return False

# GUI Setup
def main_gui():
    def send_otp():
        global otp_for_validation, attempts_left
        email = email_entry.get()
        if not email:
            messagebox.showerror("Error", "Please enter a valid email address.")
            return

        # Generate OTP and send email
        otp_for_validation = generate_otp()
        attempts_left = 5  # Reset attempts on OTP generation
        if send_otp_via_email(email, otp_for_validation):
            otp_status_label.config(text="OTP has been sent! Please enter it below.")
            validate_button.config(state="normal")

    def validate_otp_input():
        global attempts_left
        user_otp = otp_entry.get()
        if validate_otp(otp_for_validation, user_otp):
            messagebox.showinfo("Success", "Access Granted! Welcome Sai")
            window.destroy()
        else:
            attempts_left -= 1
            if attempts_left > 0:
                messagebox.showerror("Error", f"Incorrect OTP. {attempts_left} attempts left.")
            else:
                messagebox.showerror("Error", "Access Denied! No attempts left.")
                window.destroy()

    def validate_otp(generated_otp, user_otp):
        return user_otp == generated_otp

    # Initialize Tkinter window
    window = tk.Tk()
    window.title("OTP Verification System")
    window.geometry("400x300")

    # Create labels, entry boxes, and buttons
    email_label = tk.Label(window, text="Enter your email address:")
    email_label.pack(pady=10)

    email_entry = tk.Entry(window, width=30)
    email_entry.pack(pady=10)

    send_button = tk.Button(window, text="Send OTP", command=send_otp)
    send_button.pack(pady=10)

    otp_status_label = tk.Label(window, text="")
    otp_status_label.pack(pady=10)

    otp_label = tk.Label(window, text="Enter the 6-DIGIT OTP sent to your email:")
    otp_label.pack(pady=10)

    otp_entry = tk.Entry(window, width=30)
    otp_entry.pack(pady=10)

    validate_button = tk.Button(window, text="Submit", command=validate_otp_input, state="disabled")
    validate_button.pack(pady=10)

    window.mainloop()


#Main GUI Program Execution
if __name__ == "__main__":
    otp_for_validation = ""  # Store OTP globally for validation
    attempts_left = 5  # Initialize attempts count
    main_gui()
