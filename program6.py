def is_palindrome(s):
    """
    Check if a string is a palindrome.

    Args:
        s (str): Input string

    Returns:
        bool: True if the string is a palindrome, False otherwise
    """
    s = s.replace(" ", "").lower()  
    return s == s[::-1]

def main():
    # Get user input
    s = input("Enter a string: "
    if is_palindrome(s):
        print(f"'{s}' is a palindrome.")
    else:
        print(f"'{s}' is not a palindrome.")

if_name_ == "_main_":
   main()