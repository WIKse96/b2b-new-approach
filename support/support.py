def check_text(text):
    if "@" in text and text.index("@") > 0:
        at_index = text.index("@")

        if "." in text[at_index:] and text.index(".", at_index) < len(text) - 1:
            print("True")
            return True
    print("False")
    return False
