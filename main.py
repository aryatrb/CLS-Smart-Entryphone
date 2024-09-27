import face_recognize
import mail

mode = 1
email = 'ariq.torabi.extra.num5@gmail.com'
while True:
    number = 0  # get number
    button = 1  # get button
    keypad = 1


    if button == 1 & mode != 1:
        print("green")
        # turn on led green
        # turn off led red
    if keypad == 1:
        name = face_recognize.recognize()
        if mode == 1:
            if (not name.__eq__('none')) & button == 1:
                print("green")
                # turn on led green
                # turn off led red
        if mode == 2:
            mail.sendmail(email, "dareto gozashtan", name + " dareto gozasht")
        if mode == 3 & (not name.__eq__('none')):
            print("green")
            # turn on led green
            # turn off led red
            mail.sendmail(email, "dareto gozashtan", "gharibe dareto gozasht")
