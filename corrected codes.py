#code-1
def reverse_string(s):
    reversed_str = ""
    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i]
    return reversed_str

def main():
    input_string = "Hello, world!"
    reversed_string = reverse_string(input_string)
    print(f"Reversed string: {reversed_string}")

if __name__ == "__main__":
    main()
#Here we changed the variable from reversed to reversed str as it is the correct form because it is inside the reverse string function
#We also fixed return to return reversed str

#code-2
def get_age():
    age = input("Please enter your age: ")
    # Error 1: The 'age' variable is a string from user input.
    # The code compares it directly with an integer, which is incorrect.
    # Additionally, using 'isnumeric()' doesn't handle negative numbers or floats.
    if age.isdigit() and int(age) >= 18:  # Correction 1
        return int(age)
    else:
        return None

def main():
    age = get_age()
    if age is not None:  # Correction 2
        print(f"You are {age} years old and eligible.")
    else:
        print("Invalid input. You must be at least 18 years old.")

if _name_ == "_main_":
    main()

#code-3
def read_and_write_file(filename):
    try:
        # Issue 1: The code reads the content from the file and immediately overwrites the file with uppercase content.
        # This results in losing the original content and writing the modified content to the same file.
        with open(filename, 'r') as file:
            content = file.read()
        with open(f"{filename}_modified.txt", 'w') as new_file:
            new_file.write(content.upper())  # Correction: Writing modified content to a new file
        print(f"File '{filename}' processed successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    filename = "sample.txt"
    read_and_write_file(filename)

if _name_ == "_main_":
    main()

#code-4
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

def main():
    arr = [38, 27, 43, 3, 9, 82, 10]
    merge_sort(arr)
    print(f"The sorted array is: {arr}")

if __name__ == "_main_":
    main()