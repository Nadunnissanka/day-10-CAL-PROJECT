first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")

def format_name(f_name, l_name):
    # print(f_name.title() + " " + l_name.title())
    formated_fname = f_name.title()
    formated_lname = l_name.title()

    return f"{formated_fname} {formated_lname}"

formated_string = format_name(f_name = first_name, l_name = last_name)
print(formated_string)