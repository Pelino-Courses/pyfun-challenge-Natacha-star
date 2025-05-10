#Answers for question 2 
def text_editor(text,prefix="", suffix="",capitalize= False,max_length= None):
    """
    This program will help us to format a text by adding or mentioning a suffix,prefix,capitolize and maximum length
    args:
     text (str): The input string to format.
        prefix (str, optional): Text to add at the beginning. Default is "".
        suffix (str, optional): Text to add at the end. Default is "".
        capitalize (bool, optional): Whether to capitalize the text. Default is False.
        max_length (int, optional): Maximum length of the resulting string (including prefix/suffix). Default is None.
    
    Returns:
        str: The formatted string.
    """
    if not isinstance(text,str):
        raise TypeError("the 'text' must be a string")
    if not isinstance(prefix,str):
        raise TypeError("the 'prefix' must be a string")
    if not isinstance(suffix,str):
        raise TypeError("the 'suffix' must be a string")
    if not isinstance(capitalize,bool):
        raise TypeError("the 'capitalize' must be a string")
    if max_length is not None:
        if not isinstance(max_length, int):
            raise TypeError("The 'max_length' argument must be an integer or None.")
        if max_length < 0:
            raise ValueError("The 'max_length' argument cannot be negative.")
        
    result = text.upper() if capitalize else text 
    result = f"{prefix}{result}{suffix}"

    if max_length is not None:
        result = result[:max_length]

    return result
if __name__ == "__main__":
    print("Welcome to the Text Formatter!")

    text = input("Enter the text: ")
    prefix = input("Enter a prefix (or press Enter to skip): ")
    suffix = input("Enter a suffix (or press Enter to skip): ")

    cap_input = input("Do you want to capitalize the text? (yes/no): ").strip().lower()
    capitalize = cap_input == "yes"

    max_len = input("Enter max length (or press Enter to skip): ").strip()
    max_length = int(max_len) if max_len else None

    try:
        formatted = text_editor(text, prefix, suffix, capitalize, max_length)
        print("\nFormatted Text:")
        print(formatted)
    except (TypeError, ValueError) as e:
        print(f"Error: {e}") 
    
   
