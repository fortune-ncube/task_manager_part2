# Simple Task Manager for Small Businesses

This task manager program is designed to help small businesses efficiently manage tasks assigned to each member of the team. It allows users to register, log in, add tasks, view tasks, and more.

## Features

- **User Registration**: Register new users with unique usernames and passwords.
- **User De-registration**: De-register existing users with their passwords.
- **User Login**: Secure login system to access the task manager functionalities.
- **Task Assignment**: Assign tasks to specific users within the team.
- **Task Management**: Add tasks with titles, descriptions, due dates, and track their completion status.
- **Administrator Rights**: An admin user can register other users and has additional privileges.
- **Dual Display Format**: A user has the option to view tasks in either a tabular or a list format.

## Getting Started

To get started with the task manager program, follow these steps:

1. Clone the repository to your local machine.
2. Ensure you have Python installed (version 3.x).
3. Run the program using the command `python task_manager.py`.
4. Follow the on-screen prompts to register, log in, add tasks, and manage tasks.

## Usage

### Logging In

Use the "Login" option to access the task manager functionalities. Enter your username and password to log in.
Entering the username or password incorrectly 3 times consecutively will result in your account being blocked for 10 seconds.
Without altering the file, "user.txt" has a set of usernames and passwords you can use to login.

### Adding a Task

After logging in, choose the "Adding a Task" option to assign a task to a specific user. Enter the necessary details such as task title, description, and due date.

### Viewing Tasks

Select the "View All Tasks" option to see the tasks assigned to both you and other users.
Select the "View My Tasks" option to see the tasks assigned to you only.

### Changing Your Password

Select the "Change Password" option to change your password.

### Additional Functionality for the Administrator User

#### Registering a User

To register a new user, choose the "Registering a User" option from the main menu, then enter a unique username and password when prompted.

#### De-registering a User

To de-register an existing user, choose the "Unregistering a User" option from the main menu, then enter a unique username and password when prompted.

#### Generating Reports

Select the "Generate Reports" option to generate a summary of information about tasks and all active users.

#### Viewing statistics

Select the "View Statistics" option to view the statistics about users, tasks, and task completion rates.

## License

This project is licensed under the [MIT License](LICENSE).


## Contributing

Contributions are welcome! If you have any ideas for improvement, bug fixes, or new features, feel free to open an issue or submit a pull request.

## Acknowledgements

- This task manager program was created as a simple solution for small businesses to manage tasks efficiently.

