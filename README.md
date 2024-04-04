# ODD_automation
Automate - Operation Transfer Documentation 

# Operational Transfer Document (ODD) Automation Tool

This tool automates the creation of Operational Transfer Documents (ODD) for selected modules, using a user-friendly graphical interface. It allows users to select modules, set a date, and generate a document containing all necessary operational commands and information.

## Features

- Generate ODDs with pre-defined commands for selected modules.
- Customizable date and environment settings.
- Easy-to-use graphical interface.
- Save ODDs as text files for operational use.

## Prerequisites

- Python 3.6 or later.
- `customtkinter`, `tkinter`, and `PIL` libraries installed.
- A `modules.json` file containing the commands and comments for each module.

## Setup

1. **Install Python and Libraries:**
   Ensure Python 3.6+ is installed and then install the required Python libraries using:

   ```
   pip install customtkinter pillow
   ```

2. Prepare the `modules.json` File:**
   Create a `modules.json` file in the project directory containing the commands and comments for each module. This file should follow the format:

   ```json
   {
     "MODULE_NAME": {
       "command": "Command to execute",
       "comment": "Comment about the command {date}"
     }
   }
   ```

3. Download and Configure the Script:**
   Download the provided Python script (`nobet_bot.py`) to your project directory.

## Usage

1. Run the Python script using:

   ```
   python nobet_bot.py
   ```

2. In the GUI:
   - Set the desired date and link.
   - Choose the environment (TEST or PROD).
   - Select the modules to include in the ODD.
   - Click "Generate ODD" to create and save the document.

3. The generated ODD will be saved in the specified location as a `.txt` file.

## Customization

- Modify the `modules.json` file to add or change the modules and their associated commands and comments.
- Update the GUI elements in the Python script as needed for additional functionality or changes in the interface design.


<img width="798" alt="Ekran Resmi 2024-04-04 16 57 27" src="https://github.com/aozgokmen/ODD_automation/assets/74674469/4496f613-bd66-452e-86cf-2d9345a4a404">
