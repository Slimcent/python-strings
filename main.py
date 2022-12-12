def string_display():
    name = 'Obichukwu'
    print("name is" + " " + name)

    multi_line_string = """ Obinna is a good boy, fighting his
    darkness and demons all by himself,
    and hoping for a better tomorrow
    """
    print(multi_line_string)


def string_length():
    _length = "Hello, Python"
    print(len(_length))

    position = "Hello, Python"
    print(position[4])


def string_loop():
    for x in "banana":
        print(x)


def string_check():
    check_string = "The best things in life are free!"
    print("free" in check_string)

    txt = "The best things in life are free!"
    if "free" in txt:
        print("Yes, 'free' is present.")

    txt1 = "The best things in life are free!"
    print("expensive" not in txt)

    txt2 = "The best things in life are free!"
    if "expensive" not in txt:
        print("No, 'expensive' is NOT present.")


string_display()
string_length()
string_check()
string_loop()
