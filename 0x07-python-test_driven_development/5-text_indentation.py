def text_indentation(text):
    """ Prints a text with 2 new lines after each of these characters: ., ?, : """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    text = text.strip()
    print(text)
