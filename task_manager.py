# """
# Capstone template project for FCS Task 19 Compulsory task 1.
# This template provides a skeleton code to start compulsory task 1 only.
# Once you have successfully implemented compulsory task 1 it will be easier to
# add a code for compulsory task 2 to complete this capstone
# """

# =====importing libraries===========
# '''This is the section where you will import libraries'''
import datetime
import time

global view_tasks


def get_userinfo():
    """
    This function opens a text file to read the usernames and corresponding passwords.
    The information is then stored in a dictionary.
    :return: login_info
    """
    with open("user.txt", "r", encoding='utf-8-sig') as user_info:
        # Dict    =  {key                : value               looping over file line for key & value}}
        login_info = {user.split(", ")[0]: user.split(", ")[1] for user in user_info.read().splitlines()}

        return login_info


def get_task_info():
    """
    This function reads tasks of users stored in a text file and store them in a 2_D list.
    :return: user_task_info
    """
    with open("tasks.txt", "r", encoding='utf-8-sig') as all_task_info:
        # List         = [    item              looping over file for each item]
        user_task_info = [user_task.split(", ") for user_task in all_task_info.read().splitlines()]

        return user_task_info


def is_yes_no(yes_no):
    """
    This function checks if a string input is either a 'yes' or 'no'.
    The loop continues to run until one of the options above is true.
    :param yes_no
    :return: yes_no
    """
    while True:
        if yes_no not in ["yes", "no"]:
            yes_no = input(f"\nIncorrect input: {yes_no} \nPlease enter either 'Yes' or 'No'")
        else:
            break
    return yes_no  # If yes_no is either 'yes' or 'no' then return yes_no as is


def is_valid_user(test_user, log_det):
    """
    This function checks if a username to be added is valid according to the rules below.
    :param test_user:
    :param log_det:
    :return: msg, user_passed
    """
    msg = ""
    user_passed = False
    allow_special = ["@", "."]  # These are the only 2 special characters allowed in making a username
    if test_user in log_det:
        msg = "This username already exist."  # Prevents duplication of usernames
    elif " " in test_user:
        msg = "Username must not contain spaces!"  # Space character cannot be in a username string
    elif test_user == "":
        msg = "Username is empty."  # A username cannot be an empty or null string
    elif len(test_user) < 4:
        msg = "Username must be at least 4 characters long."  # Minimum length of username is 4 characters
    elif len(test_user) > 25:
        msg = "Username must not be more than 25 characters long."  # Maximum length of a username is 25 characters
    elif any((char not in allow_special and not char.isalnum()) for char in test_user):
        msg = f"Username can only have the following special characters:\n {allow_special}"
    else:
        user_passed = True

    return msg, user_passed


def is_valid_pass(test_pass):
    """
    This function checks if a password is valid according to the rules below.
    :param test_pass:
    :return: msg, password_passed
    """
    msg = ""
    password_passed = False
    allow_special = "!@#$%&*-+=|/\\?"  # Allowed special characters for passwords
    if " " in test_pass:
        msg = "Password must not contain spaces!"
    elif test_pass.isnumeric():
        msg = "Password must not contain numbers only"
    elif test_pass == "":
        msg = "Password is empty"
    elif len(test_pass) < 4:
        msg = "Password must be at least 4 characters long."
    elif len(test_pass) > 15:
        msg = "Password must not be more than 15 characters long."
    elif any((char not in allow_special and not char.isalnum()) for char in test_pass):
        msg = f"Password can only have the following special characters:\n {allow_special}"
    else:
        password_passed = True

    return msg, password_passed


def is_leap_year(any_year):
    # Leap year code below adopted from L1T13 task 2 by Fortune Ncube 09 January 2023

    if (any_year % 400 == 0) or (
            any_year % 100 != 0 and any_year % 4 == 0):  # Check leap year conditions
        return True
    else:
        return False


def paragraphing(long_str, len_limit):
    """
    This function takes in an iterable (list, string, etc.) and breaks it into a paragraph based on the
    maximum sentence length `len_limit`
    The returned sentence is in multiple lines.
    :param long_str:
    :param len_limit:
    :return: sentence
    """
    sub_length = len(long_str)  # Original length of each of a very long string > 'len_limit'
    if len(long_str) > len_limit:  # Indents text output if text length is longer than a constant 'max_len'
        start_index = 0
        end_index = len_limit
        sentence = []  # Initializing with an empty list

        # Splitting or de-concatenation of a very long string to a paragraph of sentences
        while sub_length > len_limit:  # Keeps indenting until length of last sub string < 'max_len'
            # Splitting string at nearest "space" character immediately before 'max_len'
            if long_str[end_index] == " ":
                # Appending the "next line" character at the end of each split sentence
                sentence.append(long_str[start_index:(end_index + 1)])

                start_index = end_index + 1  # Define new starting index for the next sentence
                sub_length = len(long_str) - start_index  # Reduce original length by the length of 'sentence'

                # Determine 'end_index' based on whether the remaining text length is < 'max_len'
                if sub_length > len_limit:
                    end_index = start_index + len_limit
                else:
                    end_index = len(long_str)
                    sentence.append(long_str[start_index:(end_index + 1)])
            else:
                end_index -= 1  # Decrement 'end_index' by 1 until character at 'end_index' is a "space"
    else:
        sentence = [long_str]  # Creating a singular element list

    return sentence  # The returned sentence is a list of paragraph sentences


def due_date():
    while True:
        # Error Handling for Date Input
        try:
            inp_due_date = input("\nPlease enter a Due Date in the format: yyyy-mm-dd ")
            year = int(inp_due_date[0:4])
            month = int(inp_due_date[5:7])
            day = int(inp_due_date[8:10])

            today_date = datetime.date.today()
            next_date = datetime.date(year, month, day)  # Year, month and day out of range errors are captured

            if len(inp_due_date[0:4]) != 4 or len(inp_due_date[5:7]) != 2 or len(inp_due_date[8:10]) != 2:
                raise ValueError("Date format is incorrect.")
            elif year < 0 or month < 0 or day < 0:
                raise ValueError("Date format is incorrect.")
            elif len(inp_due_date) != 10:
                raise ValueError("Date format is incorrect.")

            if today_date > next_date:
                raise ValueError("Due date has passed. Due date must be a future date.")
        except ValueError as dd_err:
            print("\n%s Please enter date in the correct format: YYYY-MM-DD" % dd_err)
        else:
            return next_date


def table_display(list_of_user, max_len):
    """
    This function prints to console expected data in table format.
    :param list_of_user:
    :param max_len:
    :return:
    """

    ordered_task = []
    task_details = get_task_info()
    td_track_task = []

    for users_name in list_of_user:  # Creating a list of users with each item being a list of user tasks
        user_tasks = []

        if view_tasks == "va":
            # Grouping user task info based on username that tasks were assigned to
            for j_enum, tasks_info in enumerate(task_details):
                if tasks_info[0] == users_name:
                    # Rearranging task columns
                    user_tasks.append([tasks_info[3],
                                       tasks_info[4],
                                       tasks_info[1],
                                       tasks_info[5],
                                       tasks_info[2]
                                       ])

            ordered_task.append(user_tasks)
        else:
            print("You have the following tasks assigned to YOU.")
            # Grouping user task info based on username that tasks were assigned to
            task_num = 0
            for j_enum, tasks_info in enumerate(task_details):
                if tasks_info[0] == users_name:
                    # Rearranging task columns
                    task_num += 1
                    if view_tasks == "vm":
                        td_track_task.append(j_enum)  # Hold the index of this task in the task_details list (tasks.txt)

                    user_tasks.append([str(task_num),
                                       tasks_info[3],
                                       tasks_info[4],
                                       tasks_info[1],
                                       tasks_info[5],
                                       tasks_info[2]
                                       ])

            ordered_task.append(user_tasks)

    # Table headings in the order in which a table is created based on task.txt storage format
    if view_tasks == "va":
        table_head = ["Date assigned", "Due date", "Task", "Task Complete?", "Task description"]
    else:
        table_head = ["Task Number", "Date assigned", "Due date", "Task", "Task Complete?", "Task description"]

    # Creating a list with maximum table column widths of each task info (Vertical Alignment of Table)
    table_col_width = []
    vert_table_sep = " \u2502 "  # Character sequence for separating a table (vertical lines)

    for t, table_heading in enumerate(table_head):
        table_col_width.append(len(table_head[t]))

    # Find the maximum table column widths of a table from all tasks
    for j_enum, users_name in enumerate(list_of_user):  # Iterating over each user from a list of users
        for i_enum, tasks_info in enumerate(ordered_task[j_enum]):  # Iterating over each task from a list of user tasks
            for k_enum, col in enumerate(table_head):  # Iterating over each task contents (Ass. Date, Due Date, Task,.)
                if tasks_info != "" and len(tasks_info[k_enum]) > table_col_width[k_enum]:

                    table_width = len(max(paragraphing(tasks_info[k_enum], max_len), key=len))
                    if table_width > table_col_width[k_enum]:
                        table_col_width[k_enum] = table_width

    # Maximum character length of horizontal line
    hor_line_len = sum(table_col_width) + len(vert_table_sep) * 5 - 1  # There are 5 vertical table lines

    rgb_colour1 = "\033[38;2;0;255;255m"
    rgb_colour2 = "\033[38;2;255;0;255m"
    white_colour = "\033[0m"

    # Creating a table for each user
    for j_enum, users_name in enumerate(list_of_user):  # Iterating over each user
        print(rgb_colour2 + f"\nTASKS ASSIGNED TO : {users_name}" + white_colour)
        print(rgb_colour1 + '_' * hor_line_len + white_colour)  # Print horizontal table line

        headings = []  # Populating table headings and formatting with space characters
        blank = ""
        for t, col in enumerate(table_head):
            headings.append(table_head[t] + " " * (table_col_width[t] - len(table_head[t])) + vert_table_sep)
            blank += (" " * table_col_width[t] + vert_table_sep)

        print("".join(headings).upper())  # Print table headings
        print(rgb_colour1 + '_' * hor_line_len + white_colour)  # Print horizontal table line

        # Setting up each table column
        for i_enum, task_item in enumerate(ordered_task[j_enum]):  # Iterating over each task item of a user
            col_info = []
            for col_num, col in enumerate(table_head):  # Iterating over each table column
                col_info.append(paragraphing(task_item[col_num], max_len))

            max_sent_len = len(max(col_info, key=len))  # Length of the longest paragraph (Max No. of sentences)

            output_row_info = []  # List containing all rows of the output table for user's tasks
            # Setting up each table row with info for all columns in table
            for k_enum in range(0, max_sent_len):  # Populate rows equal to the number of sentences
                row_info = []  # List containing all rows of info for a singe user's task

                # Populate each row according to the order of columns
                for t, col in enumerate(table_head):
                    # Check if column is empty for any row and populate with spaces or column contents
                    if k_enum < len(col_info[t]) <= max_sent_len:  # column not empty (column info + spaces + separator)
                        each_sent = col_info[t][k_enum]
                        sent_str = each_sent + " " * (table_col_width[t] - len(each_sent)) + vert_table_sep
                        row_info.append(sent_str)
                    else:  # column is empty (spaces + separator)
                        row_info.append(" " * table_col_width[t] + vert_table_sep)

                output_row_info.append(row_info)

            # Printing all rows for a user's table
            for row_task in output_row_info:
                print(rgb_colour1 + "".join(row_task) + white_colour)
            print(rgb_colour1 + blank + white_colour)

    # Mark the required tasks as Complete. e.i. Change the 'No' to a 'Yes' under Task Complete section
    if view_tasks == "vm":
        mark_task(td_track_task)


def list_display(users_tasks, max_len):
    """
    This function takes in data and prints in list format.
    :param users_tasks:
    :param max_len:
    :return:
    """

    # Table headings in the order in which a list is created based on task.txt storage format
    if view_tasks == "vm":
        table_head = [
            "Assigned to",
            "Task",
            "Task description",
            "Date assigned",
            "Due date",
            "Task Complete?",
            "Task Number"]

        table_order = [6, 1, 0, 3, 4, 5, 2]
        print("You have the following tasks assigned to YOU.")
    else:
        table_head = ["Assigned to",
                      "Task",
                      "Task description",
                      "Date assigned",
                      "Due date",
                      "Task Complete?"]

        table_order = [1, 0, 3, 4, 5, 2]

    task_num = 0
    ld_track_task = []

    long_space = len(max(table_head, key=len))  # The maximum length of
    const_space = 4

    free_space = long_space + const_space + 1
    split_at = "\n" + " " * (free_space - 1) + ":"  # Character sequence added between split sub-strings

    rgb_colour1 = "\033[38;2;0;255;255m"
    white_colour = "\033[0m"

    print(rgb_colour1 + "_" * (max_len + free_space) + white_colour)

    for j_enum, tasks_info in enumerate(users_tasks):  # Iterating over each task
        task_num += 1
        if view_tasks == "vm":
            ld_track_task.append(int(tasks_info[6]))

        for i_enum in table_order:  # Iterating over each task item

            if view_tasks == "vm":
                tasks_info[6] = str(task_num)
                # tasks_info.append(track_task_value)
                paragraph = split_at.join(paragraphing(tasks_info[i_enum], max_len))
            else:
                paragraph = split_at.join(paragraphing(tasks_info[i_enum], max_len))

            space = long_space - len(table_head[i_enum]) + const_space
            print(rgb_colour1 + f"{table_head[i_enum]}" + " " * space + ":" + paragraph + white_colour)

            # Referencing
            # Stake Overflow - How to print RGB colour to the terminal. Accessed on 09 January 2023 from
            # https://stackoverflow.com/questions/74589665/how-to-print-rgb-colour-to-the-terminal
        print(rgb_colour1 + "_" * (max_len + free_space) + white_colour)

    if view_tasks == "vm":
        mark_task(ld_track_task)


def display_format(disp_my_tasks, disp_current_user, disp_sentence_len_limit):
    """
    This function takes sets of data and prints it in the required format.
    :param disp_my_tasks:
    :param disp_current_user:
    :param disp_sentence_len_limit:
    :return:
    """
    while True:
        display_method = input("Please choose '1' or '2' for a display format:"
                               "\n\t 1 : Lists Format"
                               "\n\t 2 : Tabular Format\n")

        if display_method == "1":
            print("\nDisplaying a LIST of Tasks.\n")
            list_display(disp_my_tasks, disp_sentence_len_limit)  # Display all tasks currently assigned to user
            break
        elif display_method == "2":
            print("\nDisplaying a TABLE of Tasks.\n")
            table_display(disp_current_user, disp_sentence_len_limit)
            break
        else:
            print(f"{display_method} is out of range!\n")
            continue


def reg_user():
    global try_user
    global try_pass

    registration = True
    ru_login_details = {}
    while registration:  # Registration process stops when False (termination of 'r' option)

        new_user = input("\nPlease enter a Username to register a new User:")

        # Error handling for username
        error_msg, user_name = is_valid_user(new_user, ru_login_details)

        # Go back 1 step and try registering a new user without going all the way back to MAIN MENU
        if not user_name:
            print(f"\n{error_msg}")
            try_user = input("\nWould you like to try a new username? Enter 'Yes'/'No': ").casefold()

            if is_yes_no(try_user) == "no":  # If 'yes' the username loop continues or re-runs
                # Quit the whole registration process and go back to MAIN MENU
                break
            else:
                continue

        # Password entry code (Inside the username loop because a password is input only for a valid username)
        while True:
            new_pass = input("\nPlease enter a new Password:\n")
            pass_confirm = input("Please confirm the Password:\n")

            error_msg, pass_word = is_valid_pass(new_pass)

            # Error handling for passwords shorter than a certain length, no password or username, exclude space etc
            if not pass_word:
                print(f"\n{error_msg}")
                try_pass = input("\nWould you like to enter another password? 'Yes'/'No': ").casefold()

                if is_yes_no(try_pass) == "yes":
                    continue
                else:
                    registration = False  # Go to MAIN MENU
                    break

            # Validate password
            elif new_pass == pass_confirm:
                with open("user.txt", "a", encoding='utf-8-sig') as user_details:
                    user_details.write(new_user + ", " + new_pass + "\n")
                    break
            # Password validation failed
            else:
                print("\nYour confirmation password is incorrect: ")
                try_pass = input("\nWould you like to enter another password? 'Yes'/'No': ").casefold()

                if is_yes_no(try_pass) == "no":  # if 'yes' the password loop continues or re-runs
                    registration = False  # Go to MAIN MENU
                    break

        if try_pass == "no":  # Quit the whole registration process
            # Go to MAIN MENU
            break

        # Register another user without going back to MAIN MENU
        print("\nA new Username and Password have been registered.")
        another_user = input("\nWould you like to register another user? Enter 'Yes'/'No': ").casefold()

        if is_yes_no(another_user) == "yes":
            continue  # Goes back to prompt administrator to register another username and password
        else:
            break

    return try_user


def der_user():
    du_login_details = get_userinfo()  # Retrieve Usernames and Passwords
    task_details = get_task_info()  # Retrieve All Tasks

    de_reg_usernames = []  # A list of de-registered usernames
    # de_reg_tasks = []  # A list of tasks for all de-registered users
    user_count = len(du_login_details) - 1  # The number of possible users to be de-registered excluding Administrator

    user_options = {}  # A dictionary with numerical str cast keys and usernames as values
    for user_num_opt, username in enumerate(du_login_details, start=1):
        user_options.update({str(user_num_opt): username})

    # Selecting a username option to de-register and validating it
    while True:

        # Displaying all registered users for selection of de-registering
        print("\nDe-register any of the following users:\n\nOptions : Username")
        for user_num_opt in user_options.keys():
            print(user_num_opt + ". " + "\t" + user_options[user_num_opt])

        user_num = input("\nPlease Select One Option below or enter '0' to quit options:"
                         "\n" + ", ".join(list(user_options.keys())) + "\n")

        #  Validating username
        if user_num == "0":  # Option to quit De-registration before selecting a user to be de-registered
            print("\nDe-registration Cancelled!")
            break
        elif user_num not in user_options:
            print(f"\n\"{user_num}\" Option out of range")
            try_user_num = input("Would you like to enter another option? 'Yes'/'No': ").casefold()

            if is_yes_no(try_user_num) == "no":  # if 'yes' the de-registration loop continues or re-runs
                # Go to MAIN MENU
                break
            else:
                print(f"\nChoose the correct Option from the below: \n{user_options.keys()}\n")
        elif user_options[user_num] == current_user and user_count == 0:
            print("\nERROR : Administrator is currently the only user and cannot be DE-REGISTERED!")
            break
        elif user_options[user_num] == current_user:  # The administrator is a MAIN user and must bot be REMOVED
            print("\nERROR : Administrator cannot be DE-REGISTERED!")
            continue
        elif user_count == 0:  # Quit de-registration if all users have been de-registered
            print("\nERROR : There are no more users to be de-registered!")
            break
        else:
            confirm_de_register = input(f"\nAre you sure you want to de-register {user_options[user_num]}?"
                                        f" Enter a 'Yes' or 'No' : ").casefold()

            if is_yes_no(confirm_de_register) == "yes":
                print(f"\n{user_options[user_num]} will be de-registered from task_manager.py")

                de_reg_usernames.append(list(du_login_details)[int(user_num) - 1])  # De-register a user
                user_options.pop(user_num)  # Remove the de-registered username option

                de_register_other = input("\nWould you like to de-register another User? Enter a 'Yes' or 'No' : ")

                # Error handling for De_register_other variable
                if is_yes_no(de_register_other) == "yes":
                    user_count -= 1
                    continue
                else:
                    break
            else:
                break

    # Save de-registered users information and associated tasks
    if len(de_reg_usernames) >= 1:

        with open("d_users.txt", "a+") as de_reg_users:
            for de_reg_user in de_reg_usernames:
                # Capturing username and password of users to be de-registered
                de_reg_users.write(de_reg_user + ", " + du_login_details[de_reg_user] + "\n")

                # Removing username and password in user.txt file
                du_login_details.pop(de_reg_user)

        with open("d_tasks.txt", "a+") as de_reg_tasks:
            for j, task_info in enumerate(task_details):
                if task_info[0] == de_reg_user:
                    # Capturing task assigned to de-registered user
                    de_reg_tasks.write(", ".join(task_info) + "\n")

                    # Removing task assigned to the de-registered user
                    task_details.pop(j)

        # Rewrite the remaining registered usernames and passwords
        with open("user.txt", "w+", encoding='utf-8-sig') as user_details:
            for new_user in du_login_details:
                user_details.write(new_user + ", " + du_login_details[new_user] + "\n")

        # Rewrite the remaining registered tasks
        with open("tasks.txt", "w+") as task_write_info:
            for task_info in task_details:
                task_write_info.write(", ".join(task_info) + "\n")


def view_stats():
    print("\nThe following is Statistical Data for all registered Users.")

    generate_reports()  # Always call generate_reports. Admin user may have updated users or tasks while logged in.

    with open("task_overview.txt", "r", encoding='utf-8-sig') as task_overview_info:
        # List         = [items]
        task_info = task_overview_info.read().split(" ")

    with open("user_overview.txt", "r", encoding='utf-8-sig') as user_overview_info:
        # List    = [ item                looping over file for each item]
        user_info = [user_task.split(" ") for user_task in user_overview_info.read().splitlines()]

    num_users = user_info[0][0]  # Number of registered users
    num_tasks = user_info[0][1]  # Number of all tasks

    long_username = len([user[0] for user in user_info[1:]])

    rgb_colour1 = "\033[38;2;0;255;255m"
    rgb_colour2 = "\033[38;2;255;0;255m"
    white_colour = "\033[0m"
    vert_table_sep = " \u2502 "  # Character sequence for separating a table (vertical lines)

    headings = ["Username",
                "Tasks (No.)",
                "Total (%)",
                "Complete (%)",
                "Incomplete (%)",
                "Overdue (%)"
                ]

    # Printing all users with their respective statistics of tasks from user_overview.txt
    print(rgb_colour2)
    print(headings[0], "", vert_table_sep, (vert_table_sep + " ").join(headings[1:]), vert_table_sep[1:], white_colour)
    for vs_i, username in enumerate(user_info[1:], start=1):  # Get username
        row = []
        # Adding a username to each line to be printed
        if long_username > len(headings[0]):
            row.append(user_info[vs_i][0] + " " * (long_username - len(user_info[vs_i][0]) + 1) + vert_table_sep)
        else:
            row.append(user_info[vs_i][0] + " " * (len(headings[0]) - len(user_info[vs_i][0]) + 1) + vert_table_sep)

        # Adding all statistical values to the line to be printed
        for j in range(1, 6):
            if len(headings[j]) > len(user_info[vs_i][j]):
                row.append(" "
                           + user_info[vs_i][j]
                           + " " * (len(headings[j]) - len(user_info[vs_i][j]))
                           + vert_table_sep)
            else:
                row.append(" " + user_info[vs_i][j] + " " * (5 - len(user_info[vs_i][j])) + vert_table_sep)

        # Printing each user's line of statistics
        print(rgb_colour1 + "".join(row) + white_colour)

    # Printing data from task_overview.txt
    print(rgb_colour1)
    print(f"""The below is a summary of all users tasks:
                The total number of users is            : {num_users}
                The total number of tasks is            : {num_tasks}
                The total number of complete tasks is   : {task_info[1]}
                The total number of incomplete tasks is : {task_info[2]}
                The total number of Overdue tasks is    : {task_info[3]}
                The percentage of incomplete tasks is   : {task_info[4]}
                The percentage of overdue tasks is      : {task_info[5]}
                """)

    print("- " * 50 + white_colour)


def change_pass():
    # Get login details again in case the current user is ADMIN and had UPDATED users prior to this decision.
    # Otherwise, the updated users' information (usernames, passwords) will be lost.

    cp_login_details = get_userinfo()
    change_in_password = True

    # Change the password of a currently logged-in user
    print("\nTo change your password, please follow the following:")
    while change_in_password:
        current_pass = input("\nPlease enter your Current password: ")

        # Avoid current user's password being changed by another user while current user is away (FRAUD)
        if not current_pass == cp_login_details[current_user]:
            print("\nCurrent password is incorrect.")
            cp_try_pass = input("\nWould you like to enter another password? 'Yes'/'No': ").casefold()

            if is_yes_no(cp_try_pass) == "no":  # if 'yes' the changing password loop continues or re-runs
                # Go to MAIN MENU
                break
            else:
                continue

        # changing password after current user has confirmed current password
        while True:
            changed_pass = input("Please enter a New password: ")
            pass_confirm = input("Please confirm the New Password: ")

            error_msg, pass_word = is_valid_pass(changed_pass)

            # New password must not be the same as Current password (Avoid Redundancy)
            if current_pass == changed_pass:
                print("\nPassword is unchanged.")
                cp_try_pass = input("\nWould you like to enter another password? 'Yes'/'No': ").casefold()

                if is_yes_no(cp_try_pass) == "no":  # if 'yes' the password loop continues or re-runs
                    change_in_password = False  # Go to MAIN MENU
                    break

            # Error handling for passwords shorter than a certain length, no password etc.
            elif not pass_word:
                print(f"\n{error_msg}")
                cp_try_pass = input("\nWould you like to enter another password? 'Yes'/'No': ").casefold()

                if is_yes_no(cp_try_pass) == "no":  # if 'yes' the password loop continues or re-runs
                    change_in_password = False  # Go to MAIN MENU
                    break

            # Validating password
            elif changed_pass == pass_confirm:
                cp_login_details[current_user] = changed_pass

                # Writing usernames and passwords to a text file
                with open("user.txt", "w+", encoding='utf-8-sig') as user_details:
                    for username, password in cp_login_details.items():
                        user_details.write(username + ", " + password + "\n")

                print("\nPassword has been successfully changed!")
                change_in_password = False
                break

            # Password validation failed
            else:
                print("\nYour confirmation password is incorrect: ")
                cp_try_pass = input("\nWould you like to enter another password? 'Yes'/'No': ").casefold()

                if is_yes_no(cp_try_pass) == "no":  # if 'yes' the change password loop continues or re-runs
                    change_in_password = False
                    break


def add_task():
    ad_login_details = get_userinfo()  # always get updated login details
    # Selecting a username option to assign a task and validating it
    while True:
        print("\nAssigning a task to Any of the Following users : "
              "\n\nOptions : Username")

        # Printing Username Options for Assigning a task
        user_num = 0
        user_options = {str(0): "Quit/Exit"}
        print(str(0) + ". " + "\t\t " + "Quit/Exit")

        for username in ad_login_details.items():
            user_num += 1
            print(str(user_num) + ". " + "\t\t " + str(username[0]))
            user_options.update({str(user_num): username})

        user_num = input(f"\nPlease Select One of the Options below: \n{list(user_options.keys())}\n ")

        #  Validating username option
        if user_num == "0":
            print("\nTask assignment terminated.\n")
            break
        elif user_num not in user_options:
            print(f"\n\"{user_num}\" Option out of range")
            try_user_num = input("Would you like to enter another option? 'Yes'/'No': ").casefold()

            if is_yes_no(try_user_num) == "no":  # if 'yes' the assigning task loop continues or re-runs
                print("\nTask assignment terminated.\n")  # Go to MAIN MENU
                break
            else:
                print(f"\nChoose the correct Option from the below: \n{user_options.keys()}\n")

        username = list(ad_login_details)[int(user_num) - 1]
        task_title = input(f"Please enter a Task Title for username without commas (,): {username} \n: ")
        description = input(f"\nPlease enter a Task Description for username without commas (,): {username} \n: ")

        #  Getting Due Date from user and validating it.

        task_complete = "No"

        today_date = datetime.date.today()
        date_needed = due_date()

        task_box_row = [username,
                        task_title,
                        description,
                        today_date.strftime("%d %b %Y"),
                        date_needed.strftime("%d %b %Y"),
                        task_complete,
                        ]

        task_box.append(task_box_row)
        print("\nTask has been successfully assigned.")

        other_task = input("\nWould you like to assign another task? Enter a 'Yes' or 'No' : ")

        # Error handling for other_task variable
        if is_yes_no(other_task) == "yes":
            continue
        else:
            break

    # Writing tasks into text file
    with open("tasks.txt", "a", encoding='utf-8-sig') as task_write_info:
        for row in task_box:
            task_line = ", ".join(row)
            task_write_info.write(task_line + "\n")


def view_all():
    task_details = get_task_info()  # A 2-D List of lists
    va_login_details = get_userinfo()

    user_list = list(va_login_details.keys())  # Creating a list of usernames

    # Call displaying function to output information onto console
    display_format(task_details, user_list, sentence_len_limit)


def view_mine():
    vm_task_details = get_task_info()

    rgb_colour3 = "\033[38;2;0;255;255m"
    white_colour3 = "\033[0m"

    my_tasks = []  # A list containing only the current user's tasks
    for task_enum, task_info in enumerate(vm_task_details):
        if task_info[0] == current_user:
            task_info.append(str(task_enum))
            my_tasks.append(task_info)

    if not my_tasks:
        print(rgb_colour3 + "You do not have any tasks assigned to you." + white_colour3)
    else:
        list_current_user = [current_user]
        display_format(my_tasks, list_current_user, sentence_len_limit)


def generate_reports():
    gr_login_details = get_userinfo()
    gr_task_details = get_task_info()

    total_num_complete = 0
    total_num_incomplete = 0
    total_num_overdue = 0
    total_num_tasks = len(gr_task_details)
    total_num_users = len(gr_login_details)

    # A 2D list of usernames tracked with task_manager on fist sub-list
    # This list holds 2 data types (str and int), hence some of non-fatal highlighted errors
    user_task_info = [[user for user in gr_login_details.keys()]]

    # All other sub-lists of the 2D list are initialized to zero
    for gr_j in range(0, 5):
        user_task_info.append([0 for gr_i in range(0, total_num_users)])

    for enum_task, user_task in enumerate(gr_task_details):
        user_index = user_task_info[0].index(user_task[0])
        user_task_info[1][user_index] += 1  # Counts the number tasks ASSIGNED to a user

        if user_task[5] == "Yes":
            total_num_complete += 1  # Counts ALL tasks that are COMPLETE
            user_task_info[2][user_index] += 1  # Counts the number of tasks COMPLETED for a user
        else:
            total_num_incomplete += 1  # Counts ALL tasks that are INCOMPLETE
            user_task_info[3][user_index] += 1  # Counts the number of tasks INCOMPLETE for a user

            today_date = datetime.date.today()  # Get today's date
            dd = user_task[4].split(" ")[::-1]  # Retrieve str date of the due date
            gr_due_date = datetime.datetime.strptime("-".join(dd), "%Y-%b-%d").date()  # Convert str date to digital

            # Check if due_date is less than today_day (Overdue if True)
            if today_date < gr_due_date:
                total_num_overdue += 1
                user_task_info[4][user_index] += 1  # Counts the number of tasks INCOMPLETE and OVERDUE for a user

    per_incomplete = (total_num_incomplete / total_num_tasks) * 100
    per_overdue = (total_num_overdue / total_num_tasks) * 100

    # Printing task overview info onto a txt file
    with open("task_overview.txt", "w+", encoding="utf-8-sig") as task_overview_file:
        task_overview_file.write(str(total_num_tasks) + " "
                                 + str(total_num_complete) + " "
                                 + str(total_num_incomplete) + " "
                                 + str(total_num_overdue) + " "
                                 + str(per_incomplete) + " "
                                 + str(per_overdue))

    # Printing user overview info onto a txt file
    with open("user_overview.txt", "w+", encoding="utf-8-sig") as user_overview_file:
        user_overview_file.write(str(total_num_users) + " " + str(total_num_tasks) + "\n")

        for user_enum, user in enumerate(user_task_info[0]):
            user_task_num = user_task_info[1][user_enum]
            per_user_task = (user_task_num / total_num_tasks) * 100

            user_overview_file.write(user_task_info[0][user_enum] + " ")
            if per_user_task > 0:
                per_comp = (user_task_info[2][user_enum] / user_task_info[1][user_enum]) * 100
                per_incomp = (user_task_info[3][user_enum] / user_task_info[1][user_enum]) * 100
                per_incomp_due = (user_task_info[4][user_enum] / user_task_info[1][user_enum]) * 100
            else:
                per_comp = 0
                per_incomp = 0
                per_incomp_due = 0

            user_overview_file.write(str(user_task_num) + " "
                                     + str(round(per_user_task, 1)) + " "
                                     + str(round(per_comp, 1)) + " "
                                     + str(round(per_incomp, 1)) + " "
                                     + str(round(per_incomp_due, 1)) + "\n"
                                     )


def mark_task(mt_track):
    mt_task_details = get_task_info()
    mt_login_details = get_userinfo()

    # Mark the required tasks as Complete. e.i. Change the 'No' to a 'Yes' under Task Complete section
    #                                           OR
    # Edit the Task by Re-assigning it to another user and/or Changing the task's due date

    # Loop through tasks to mark as needed

    # Prompt a user to mark their tasks
    mt_mark = input("\nWould you like to Mark and/or Edit a Task? Enter a 'Yes' or 'No' : ")

    edit_mark = True
    while edit_mark:

        # Error handling for a Yes or No prompt question to mark and/or edit a task
        if is_yes_no(mt_mark) == "yes":

            edit_history = []  # A list that stores all the tasks numbers that have been marked or edited
            # Error handling for a Task Number to be within provided range
            while True:
                mt_task_num = input("\nPlease enter a Task Number to Mark or Edit a task. Enter '-1' to exit : ")

                # Mark or Edit
                if mt_task_num == "-1":
                    # Exiting the marking or editing of a task procedure
                    print("\nNo tasks were marked.")
                    edit_mark = False
                    break
                elif not mt_task_num.isdigit():
                    # Task number must be an integer
                    print("\nOption out of range.")
                    continue
                elif int(mt_task_num) in range(1, len(mt_track) + 1):

                    # Find task in a list of all tasks and mark or edit it
                    if mt_task_details[mt_track[int(mt_task_num) - 1]][5].casefold() == "yes":
                        # Preventing the remarking of a marked task
                        print("\nThis task has already been Marked.")
                        break
                    elif mt_task_num in edit_history:
                        # Preventing the re-editing of an edited task
                        print("\nThis task has already been Edited.")
                        break
                    else:
                        # Mark or Edit Task
                        while True:
                            mt_edit = input("\nPlease enter: "
                                            "\n\t'm' - 'Mark' - Mark a task as Complete. Task Complete : Yes "
                                            "\n\t'e' - 'Edit' - Edit a Task's Due date or delegate to another User.")

                            # Mark a Task as Complete
                            if mt_edit.casefold() == 'm':
                                # Marking a task as Complete with a 'Yes'
                                mt_task_details[mt_track[int(mt_task_num) - 1]][5] = "Yes"
                                print(f"\nTask Number {str(mt_task_num)} has been marked as Completed.")
                                break

                            # Edit a Task - Re-assign to Another user and/or Change Due Date
                            elif mt_edit.casefold() == 'e':

                                # Printing Username Options for Assigning a task
                                edit_user = 0
                                user_options = {str(-1): "Quit/Exit"}
                                print("\nAssigning a task to Any of the Following users : "
                                      "\n\nOptions : Username")

                                print("\n" + str(-1) + ". " + "\t " + "Quit/Exit")

                                # Printing usernames with corresponding numbering
                                for username in mt_login_details.items():
                                    edit_user += 1
                                    print(str(edit_user) + " . " + "\t " + str(username[0]))
                                    user_options.update({str(edit_user): username})

                                # Prompt for username whom task is to be re-assigned
                                edit_user = input(
                                    f"\nPlease Select One of the Options below: \n{list(user_options.keys())}\n ")

                                #  Quiting selection of username option
                                if edit_user == "-1":
                                    print("\nTask editing terminated.\n")
                                    break

                                # Options that are out of the presented
                                elif edit_user not in user_options:
                                    print(f"\n\"{edit_user}\" Option out of range")
                                    try_user_num = input(
                                        "Would you like to enter another option? 'Yes'/'No': ").casefold()

                                    if is_yes_no(try_user_num) == "no":  # if 'yes' the loop continues or re-runs
                                        print("\nTask editing terminated.\n")
                                        break
                                    else:
                                        print(
                                            f"\nChoose the correct Option from below: \n{user_options.keys()}\n")

                                # Editing a task
                                else:
                                    username = list(mt_login_details)[int(edit_user) - 1]
                                    task_name = mt_task_details[mt_track[int(mt_task_num) - 1]][1]
                                    task_description = mt_task_details[mt_track[int(mt_task_num) - 1]][2]
                                    task_assign_date = mt_task_details[mt_track[int(mt_task_num) - 1]][3]
                                    task_due = mt_task_details[mt_track[int(mt_task_num) - 1]][4]
                                    task_complete = mt_task_details[mt_track[int(mt_task_num) - 1]][5]

                                    edit_due_date = input(f"\nChange the Due Date for User: {username}"
                                                          f"\nAssigned Task : {task_name}?"
                                                          f"\n'Yes' or 'No'\n")

                                    # Update due date with a new date, else keep it unchanged
                                    if is_yes_no(edit_due_date) == "yes":
                                        task_due = due_date()

                                    # Get current username
                                    curr_user = mt_task_details[mt_track[int(mt_task_num) - 1]][0]

                                    # Re-assigning task to another user and removing it under current user's tasks
                                    # if current logged-in user is not 'username'
                                    mt_task_details[mt_track[int(mt_task_num) - 1]] = [username,
                                                                                       task_name,
                                                                                       task_description,
                                                                                       task_assign_date,
                                                                                       task_due,
                                                                                       task_complete,
                                                                                       ]

                                    # Output different messages depending on weather current user = 'username'
                                    if curr_user == username:
                                        if edit_due_date == "yes":
                                            # Task still assigned to current user and postponed to a future date
                                            print(f"\nTask Number {mt_task_num} has been"
                                                  f" postponed to {task_due}")
                                        else:
                                            # Task still assigned to current user without a change in due date
                                            print(f"\nTask Number {mt_task_num} has not been edited"
                                                  f" and is still due on {task_due}.")
                                    else:
                                        # Task re-assigned with same date as previously assigned
                                        if edit_due_date == "yes":
                                            print(f"\nTask Number {mt_task_num} has been re-assigned"
                                                  f" to {username} and is now due on {task_due}.")
                                        # Task re-assigned with an updated future date
                                        else:
                                            print(f"\nTask Number {mt_task_num} has been re-assigned"
                                                  f" to {username} and is still due on {task_due}.")
                                    edit_history.append(mt_task_num)
                                break

                            #  Error Handling for 'mark_edit' variable
                            else:
                                print(f"\nOption out of range: {mt_edit}")
                                continue

                else:
                    # Try and select a Task number that is within the given range
                    print("\nOption out of range.")
                    continue

                # Mark another task before closing task marking process
                another_task_mark = input("\nMark or Edit another Task? 'Yes' or 'No' : ")
                if is_yes_no(another_task_mark) == "yes":
                    continue
                else:
                    # print("\nTasks have been Marked.")
                    edit_mark = False
                    break

        else:
            break

    # Rewrite the tasks including the original unmarked tasks and the recently marked tasks
    with open("tasks.txt", "w+") as dis_task_write_info:
        for task_info in mt_task_details:
            dis_task_write_info.write(", ".join(task_info) + "\n")


# ====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''

login_trials = 3  # Limit number of login attempts for all incorrect login details
administrator = False
usercheck = ""  # The username used to check or validate the one stored in users.txt during login

# Welcome Message
print("\n|-|-|-|-|- Welcome to Task_Manager  -|-|-|-|-|\n")
print("|-|-|-|-|- Please proceed to login. -|-|-|-|-|\n")
# Requesting User to input and validating Username and Password.
while True:
    try:
        # If login_trials are exhausted, user must wait 10 seconds before trying again.
        # This is for security purposes.
        login_delay = 10  # Time to delay login by
        if login_trials == 0:
            print(f"\nYour access is blocked. Please try again after {str(login_delay)} seconds.")
            # Display a count-down timer
            for i in range(login_delay, -1, -1):
                time.sleep(1)
                print("", end=f"\rLogin In {str(i)}")
            print()

        print()
        usercheck = input("Please enter your login username: ")  # Getting Username input from user
        pass_check = input("Please enter your login password: ")  # Getting Password input from user

        login_details = get_userinfo()  # Calling function to retrieve all stored usernames and passwords
        # Check if username exists
        if usercheck in login_details:
            # Check if password corresponds to username
            if pass_check == login_details[usercheck]:
                # Checking if User is Administrator to give access to Admin rigs or deny if otherwise
                print("\nAccess granted to Task_Manager!!!")
                if list(login_details).index(usercheck) == 0:
                    administrator = True
                    print("\nYou are logged in as 'Administrator' with administrative rights.")
                else:
                    print(f"\nYou are logged in as '{usercheck}' with user rights only.")
                break
            else:
                raise KeyError("The username and/or password you entered are incorrect.")
        else:
            raise KeyError("The username you entered does not exist.")
    except KeyError as error:
        login_trials -= 1
        print(f"\n%s\nYou have {str(login_trials)} chances left to login." % error)

        # Option to quit login if correct username and password cannot be remembered.
        try_login = input("\nWould you like to try to login again? Enter 'Yes'/'No':")
        if is_yes_no(try_login) == "no":  # If 'yes' the username loop continues or re-runs
            print("\nClosing task_manager.py\nGoodbye!")
            exit()  # Quit the whole registration process and go back to MAIN MENU
        else:
            continue

current_user = usercheck  # Store the username for other validations through the code
# Menu Options
while True:

    # Presenting the menu to the user and prompting for the next user's preferred step.
    if administrator:  # Admin user has a different menu due to their added functionality
        menu = input(
            '''\nSelect one of the following Options below:
            r  - Registering a user
            d  - Unregistering a user
            vs - View Statistics
            c  - Change Password 
            a  - Adding a task
            va - View all tasks
            vm - view my task
            gr - Generate Reports
            e  - Exit
            :\n'''
        ).lower()
    else:  # Non-admin user has limited functionality
        menu = input(
            '''\nSelect one of the following Options below:
            c  - Change Password
            a  - Adding a task
            va - View all tasks
            vm - view my task
            e  - Exit
            :\n'''
        ).lower()

    task_count = 0  # Used to count the number of tasks
    task_box = []  # A list to store all tasks
    sentence_len_limit = 50  # Limit for character length of a long sentence to be turned into a paragraph

    # This Part is only for the ADMIN user to REGISTER New Users
    if menu == 'r':
        '''In this block you will write code to add a new user to the user.txt file
        - You can follow the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same.
            - If they are the same, add them to the user.txt file,
            - Otherwise you present a relevant message.'''
        try_user = try_pass = ""

        # For a user who 'knows' that admin has options (r, d, s, etc.) the user must not have access to them
        if not administrator:  # Limit access of registering users to ADMIN only
            print("\nYou have made a wrong choice, Please Try again")
            continue

        # Register a Username (Only if the logged-in user is Administrator)
        reg_user()

        if try_user or try_pass == "no":  # Quit the whole registration process and go to MAIN MENU
            # Prompts user with an option to continue using Task_Manager or Exit
            to_continue = input("\nWould you like to go to Main Menu? Enter a 'Yes' or 'No' : ").casefold()
            if is_yes_no(to_continue) == "yes":
                continue
            else:
                print('\nClosing Task_Manager. \nGoodbye!!!')
                break

    # This Part is only for the ADMIN user to DE-REGISTER any of the Existing Users
    elif menu == 'd':
        '''In this block the admin user can de-register any user
        -Print all currently registered users
        -Choose a user to be de-registered
        -Store username and password in txt file for d-users
        -Store assigned task in txt file for d-tasks
        -Delete de-registered user from user txt file and delete tasks assigned to them on tasks txt file
        '''

        if not administrator:  # Limit access to De-Registering only to Administrator
            print("\nYou have made a wrong choice, Please Try again")
            continue

        # De-register a Username (Only if the logged-in user is Administrator)
        der_user()

        # Prompts user to an option to continue using Task_Manager or Exit
        to_continue = input("\nWould you like to go to Main Menu? Enter a 'Yes' or 'No' : ").casefold()
        if is_yes_no(to_continue) == "yes":
            continue
        else:
            print('\nClosing Task_Manager. \nGoodbye!!!')
            break

    # This Part is only for the ADMIN user to View Statistical Data (Tasks and Users)
    elif menu == 'vs':

        if not administrator:  # Only Administrator has access to viewing statistics
            print("\nYou have made a wrong choice, Please Try again")
            continue

        view_stats()

        # Prompts user to an option to continue using Task_Manager or Exit
        to_continue = input("\nWould you like to go to Main Menu? Enter a 'Yes' or 'No' : ").casefold()
        if is_yes_no(to_continue) == "yes":
            continue
        else:
            print('\nClosing Task_Manager. \nGoodbye!!!')
            break

    # This Part is for ALL users who wish to CHANGE their Password
    elif menu == 'c':
        '''In this block, a user has a option to change their password
        '''

        change_pass()

        # Prompts user to an option to continue using Task_Manager or Exit
        to_continue = input("\nWould you like to go to Main Menu? Enter a 'Yes' or 'No' : ").casefold()
        if is_yes_no(to_continue) == "yes":
            continue
        else:
            print('\nClosing Task_Manager. \nGoodbye!!!')
            break

    # This Part is for ALL users who wish to ASSIGN tasks to themselves and other users
    elif menu == 'a':
        '''In this block you will put code that will allow a user to add a new task to task.txt file
        - You can follow these steps:
            - Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
            - Then get the current date.
            - Add the data to the file task.txt and
            - You must remember to include the 'No' to indicate if the task is complete.'''

        add_task()

        # Prompts user to an option to continue using Task_Manager or Exit
        to_continue = input("\nWould you like to go to Main Menu? Enter a 'Yes' or 'No' : ").casefold()
        if is_yes_no(to_continue) == "yes":
            continue
        else:
            print('\nClosing Task_Manager. \nGoodbye!!!')
            break

    # This Part is for ALL users who wish to view tasks for ALL users
    elif menu == 'va':
        '''In this block you will put code so that the program will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the L1T19 pdf file page 6
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 in L1T19 pdf
            - It is much easier to read a file using a for loop.'''

        view_tasks = "va"
        view_all()

        # Prompts user to an option to continue using Task_Manager or Exit
        to_continue = input("\nWould you like to go to Main Menu? Enter a 'Yes' or 'No' : ").casefold()
        if is_yes_no(to_continue) == "yes":
            continue
        else:
            print('\nClosing Task_Manager. \nGoodbye!!!')
            break

    # This Part is for ALL users who wish to view ONLY their tasks
    elif menu == 'vm':
        '''In this block you will put code the that will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the L1T19 pdf
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same you print the task in the format of output 2 shown in L1T19 pdf '''
        view_tasks = "vm"
        view_mine()

        # Prompts user with an option to continue using Task_Manager or Exit
        to_continue = input("\nWould you like to go to Main Menu? Enter a 'Yes' or 'No' : ").casefold()
        if is_yes_no(to_continue) == "yes":
            continue
        else:
            print('\nClosing Task_Manager. \nGoodbye!!!')
            break

    # This Part is only for the ADMIN user to Generate Reports (Tasks and Users)
    elif menu == 'gr':

        if not administrator:  # Only Administrator has access to viewing statistics
            print("\nYou have made a wrong choice, Please Try again")
            continue

        generate_reports()

        print("\nUser and Task Overview reports have been generated.\n")

        view_report = input("Would you like to view the reports? Enter a 'Yes' or 'No' : ").casefold()
        if is_yes_no(view_report) == "yes":
            view_stats()

        # Prompts user to an option to continue using Task_Manager or Exit
        to_continue = input("\nWould you like to go to Main Menu? Enter a 'Yes' or 'No' : ").casefold()
        if is_yes_no(to_continue) == "yes":
            continue
        else:
            print('\nClosing Task_Manager. \nGoodbye!!!')
            break

    elif menu == 'e':
        print('\nClosing Task_Manager. \nGoodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
