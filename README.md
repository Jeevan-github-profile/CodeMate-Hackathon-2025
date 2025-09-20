# Python Terminal Emulator 


## Overiew:
This project is a **Python-based terminal emulator** that replicates the behaviour of a real-system terminal. 
It supports standard file and directory operations, system monitoring, command history and intergrates basic
**CodeMate AI features** for error suggestions and reports

This emulator is fully compatible with **Windows, macOS and Linux**, and runs entirely on Python (no external libraries
are required)

---

## Features:

### Core Features:
**File and Directory Operations**
1. 'ls' -> List files and folders
2. 'pwd' -> Print current working directory
3. 'cd <Directory_Name>' -> Change directory
4. 'mkdir <folder_name>' -> Create a folder
5. 'rm <file/folder>' -> Remove file or folder

**System Monitoring**
1. 'cpu' -> Show CPU load
2. 'mem' -> Show memory usage
3. 'ps' -> List running processes

**Command History**
1. 'history' -> Displays a list of previously executed commands

**CodeMate AI Integration**
1. 'report' -> Generates a summary of commands executed (CodeMate Build Report)
2. Automatic suggestions for invalid commands (e.g 'sl' -> "'Did you mean 'ls'?")

---
## Installation and Setup

### Local Setup
1. Ensure **Python 3.x** is installed in your system
2. Clone or download the project folder:
'''bash
git clone <repository-link>
cd terminal_emulator

## Run the emulaor
python main.py
