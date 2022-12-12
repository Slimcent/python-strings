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


def string_slice():  # get characters from position 2 to position 5, excluding 5
    text = "Hello, Python!"
    print(text[2:5])

    text1 = "Hello, Python!"  # get characters from the start position to position 5, excluding 5
    print(text1[: 5])

    text2 = "Hello, Python!"  # get characters from the position 2 to the end position
    print(text2[2:])

    text3 = "Hello, World!"  # - index means, get characters from the end of the string
    print(text3[-5:-2])  # count 5 from the end, making the start position to be "o", and end position to be "l",
    # ie -5[o], -4[r], -3[l]


def string_split():
    text = "Hello, World!"
    print(text.split(","))  # returns ['Hello', ' World!']


def string_format():
    age = 60
    txt = "My name is Obinna, and I am {}"
    print(txt.format(age))

    quantity = 3
    item_no = 567
    price = 49.95
    my_order = "I want {} pieces of item {} for {} dollars."
    print(my_order.format(quantity, item_no, price))


string_display()
string_length()
string_check()
string_loop()
string_slice()
string_split()
string_format()
