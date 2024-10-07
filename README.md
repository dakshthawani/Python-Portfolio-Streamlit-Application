# Python Portfolio Streamlit Application

This project is a Python-based Streamlit application that showcases a portfolio of projects developed using Python. It includes an author profile and a list of projects, along with the capability to send email notifications.

## Table of Contents
- [Overview](#overview)
- [Requirements](#requirements)
- [Project Structure](#project-structure)
- [Setup](#setup)
- [Usage](#usage)
- [Features](#features)
- [How It Works](#how-it-works)
- [Additional Information](#additional-information)

## Overview
The application displays a profile of the author and lists Python projects stored in a CSV file. Users can view project titles, descriptions, and links to source code. Additionally, there is functionality to send email notifications.

## Requirements
- Python 3.x
- Required Python libraries:
  - `streamlit`
  - `pandas`
  - `smtplib` (standard library)

You can install the required libraries using:
```bash
pip install streamlit pandas

## Project Structure
```bash
├── images                # Directory containing author image and project images
│   ├── author.png
│   └── ...               # Other project images
├── dataset.csv           # CSV file containing project details
├── main.py               # The main Streamlit application script
├── send_email.py         # Script containing email sending functionality (optional)
├── README.md             # This README file
```

## Setup
1. Clone or download this repository to your local machine.
2. Ensure you have the required libraries installed (as mentioned in the Requirements section).
3. Prepare a CSV file named `dataset.csv` with the following structure:
```bash
title,description,image,url
Project Title 1,Description of project 1,project1_image.png,https://github.com/yourusername/project1
Project Title 2,Description of project 2,project2_image.png,https://github.com/yourusername/project2
...
```
Replace `project1_image.png`, `project2_image.png`, etc., with the actual image filenames located in the `images` directory.

## Usage
1. Run the Streamlit application using:
```bash
streamlit run main.py
```
2. The application will open in your web browser, displaying the author profile and the list of projects.

## Features
- Displays the author's image and profile description.
- Lists projects with titles, descriptions, images, and links to source code.
- The capability to send email notifications (refer to the `send_email.py` for implementation details).

## How It Works
1. Streamlit Application: The `main.py` script uses Streamlit to create a web interface.
2. Data Handling: It reads project data from `dataset.csv` using `pandas` and displays it in a structured layout.
3. Email Notification: The `send_mail` function in the `send_email.py` file handles email notifications using the `smtplib` library. You can customize the recipient's email and message.

## Email Sending Functionality
To enable the email feature, ensure that you have the following environment variable set with your email password:
```bash
export PASSWORD="your_email_password"
```
Update the username variable in the send_email.py file with your email address.

## Additional Information
- Make sure to adjust the CSV file path in main.py if it is located in a different directory.
- Customize the author profile content and project details in dataset.csv as needed.
- You can expand the project further by adding more functionalities such as user authentication or a contact form.
If you encounter any issues or have suggestions for improving this project, feel free to open an issue or submit a pull request.
```bash

### Key Notes:
- This README file includes sections that guide the user through understanding the project and how to set it up.
- Adjust the structure of the CSV file in the `Setup` section as necessary.
- Make sure to inform users about how to handle sensitive information, like email passwords, in a secure way.
- You can modify the content of the README to better fit your project's specifics or style. If you need further customization, just let me know!
```
