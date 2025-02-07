# AlarmManager.py ⏰

## Overview
This Python script is an interactive command-line application for managing alarm data using an SQLite database. It allows users to:
- Insert new alarm records ⏳
- View existing records 📃
- Update records ✏️
- Delete records ❌
- Exit the application ⏏

The script ensures data validation and user-friendly interactions.

---

## Code Breakdown 📝

### 1. **Importing Required Libraries**
```python
from datetime import datetime
from colorama import Fore
import sqlite3
import os
```
- `datetime`: Used to retrieve and format the current date and time.
- `colorama.Fore`: Adds color to terminal text for better readability.
- `sqlite3`: Provides database connectivity to store and manage alarms.
- `os`: Used to clear the terminal screen.

---

### 2. **Clearing the Screen**
```python
os.system('clear')
```
- Clears the terminal screen to provide a clean user interface.

---

### 3. **Starting the Infinite Loop**
```python
while True:
```
- This keeps the program running until the user chooses to exit.

---

### 4. **Connecting to SQLite Database**
```python
con = sqlite3.connect(r'allarm_data.db')
ta = con.cursor()
```
- Establishes a connection to an SQLite database named `allarm_data.db`.
- Creates a cursor object to execute SQL commands.

---

### 5. **Displaying Menu Options**
```python
print(Fore.RED + 'Data entry: 1')
print('View data: 2')
print('Update of data: 3')
print('Delete data: 4')
print('Exit: 0')
```
- Provides users with options to interact with the database.
- Uses `colorama.Fore.RED` to highlight menu items.

---

### 6. **Getting User Input**
```python
enter = int(input(Fore.MAGENTA + 'Enter: '))
```
- Prompts the user to select an option from the menu.

---

## **Feature 1: Data Entry**

### 7. **Retrieving the Current Date and Time**
```python
datatime = datetime.now()
day, month, year = datatime.day, datatime.month, datatime.year
hour, minute, strftime = datatime.hour, datatime.minute, datatime.strftime('%p')
```
- Fetches the current system date and time.
- Extracts the day, month, year, hour, and minute values.

---

### 8. **Getting User Input for New Alarm**
```python
insert_Day = int(input(Fore.MAGENTA + 'Insert Day: ') or day)
insert_Month = int(input('Insert Month: ') or month)
insert_Year = int(input('Insert Year: ') or year)
insert_name = input('Insert Name: ').title()
```
- Asks the user for the alarm details, with default values set to the current date.

---

### 9. **Validating User Input**
```python
if not (1 <= insert_Day <= 31):
    print(Fore.RED + 'Error! Invalid day.')
    continue
```
- Ensures that the user enters valid values for day, month, hour, and minute.
- If an invalid value is entered, an error message is displayed and the loop continues.

---

### 10. **Creating the Table if Not Exists**
```python
ta.execute("SELECT name FROM sqlite_master WHERE type='table';")
```
- Checks if the `allarm` table exists in the database.
```python
if 'allarm' not in table_names:
    ta.execute('CREATE TABLE allarm(title TEXT, date TEXT, time TEXT)')
```
- Creates the `allarm` table if it does not exist.

---

### 11. **Inserting Data into Database**
```python
ta.execute("INSERT INTO allarm(title, date, time) VALUES(?, ?, ?)",
   (insert_name, f"{insert_Day}/{insert_Month}/{insert_Year}", f"{insert_hour}:{insert_minute}{insert_strftime}"))
```
- Inserts the user-provided alarm details into the database.

---

## **Feature 2: Viewing Data**
```python
elif enter == 2:
    ta.execute("SELECT * FROM allarm")
    sd = ta.fetchall()
    for i in sd:
        print(Fore.MAGENTA + f'Name: {i[0]}')
        print(Fore.MAGENTA + f'Era: {i[1]}')
        print(Fore.MAGENTA + f'Time: {i[2]}')
```
- Fetches and displays all records from the `allarm` table.

---

## **Feature 3: Updating Data**
- The user selects a title and chooses to update either `title`, `date`, or `time`.
```python
ta.execute(f"UPDATE allarm SET title = ? WHERE title = ?", (word, title_delete))
```
- Updates the selected record based on user input.

---

## **Feature 4: Deleting Data**
```python
ta.execute("DELETE FROM allarm WHERE title = ?", (delete_name,))
```
- Deletes the selected record from the database.
- Ensures that the record exists before deletion.

---

## **Feature 5: Exiting the Program**
```python
elif enter == 0:
    break
```
- Exits the loop, terminating the program.

---

## **Error Handling**
```python
except Exception as e:
    print(f'Obviously there was an error, please try again.\n{e}')
```
- Catches and displays errors, ensuring the program does not crash unexpectedly.

---

## **Final Commit and Closing Connection**
```python
con.commit()
con.close()
```
- Saves changes to the database.
- Closes the database connection to prevent data corruption.

---

## **Conclusion**
#### This script effectively manages alarm records in an SQLite database, providing options to add, view, update, and delete records. The user-friendly interface, input validation, and error handling make it a reliable tool for simple alarm management.
--
# Alarm_Checker.py ⏰

## Overview
This Python script continuously monitors an SQLite database for scheduled alarms and triggers them when the current date and time match the stored values. It utilizes:
- **SQLite** for storing alarm records 🗄️
- **Datetime module** to fetch the current system time and date 📅
- **Colorama** for colored terminal output 🎨
- **OS and Time modules** for screen clearing and interval execution ⚙️

---

## Code Breakdown 📝

### **1. Importing Required Libraries**
```python
from datetime import datetime
from colorama import Fore
import sqlite3
import time
import os
```
- `datetime`: Retrieves the current date and time.
- `colorama.Fore`: Adds color to text output in the terminal.
- `sqlite3`: Connects to an SQLite database to fetch stored alarms.
- `time`: Implements a delay to prevent excessive CPU usage.
- `os`: Clears the terminal screen for a cleaner display.

---

### **2. Establishing Database Connection**
```python
con = sqlite3.connect('allarm_data.db')
cur = con.cursor()
```
- Connects to the `allarm_data.db` database.
- Creates a cursor `cur` for executing SQL queries.

---

### **3. Starting an Infinite Loop**
```python
try:
    while True:
```
- Keeps the program running indefinitely to check for alarms.

---

### **4. Fetching the Current Date and Time**
```python
now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.strftime('%I')
minute = now.minute
strftime = now.strftime('%p')
calendar = f"{day}/{month}/{year}"
now_time = f'{hour}:{minute:02d}{strftime}'
```
- Retrieves the current date and time.
- Formats the time in **12-hour format** (`%I`) and appends **AM/PM** (`%p`).
- Constructs `calendar` for the date and `now_time` for the time, ensuring proper formatting.

---

### **5. Checking if the 'allarm' Table Exists**
```python
cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='allarm'")
if not cur.fetchone():
    print(Fore.RED + "Table 'allarm' does not exist.")
    break
```
- Queries SQLite to check if the `allarm` table exists.
- If the table is missing, the program displays a warning and **exits the loop**.

---

### **6. Fetching Stored Alarms from Database**
```python
cur.execute('SELECT * FROM allarm')
data = cur.fetchall()
alarm_triggered = False
```
- Retrieves all records from the `allarm` table.
- Initializes `alarm_triggered` as `False` to track if an alarm has matched the current time.

---

### **7. Comparing Stored Alarms with Current Time**
```python
for row in data:
    stored_date = row[1].strip()
    stored_time = row[2].strip()
    if now_time == stored_time and calendar == stored_date:
```
- Iterates through each stored alarm.
- Compares `stored_date` and `stored_time` with `calendar` and `now_time`.
- **If they match, the alarm is triggered**.

---

### **8. Triggering the Alarm**
```python
os.system('clear')
print(Fore.RED + f'Name: {row[0]}')
print(Fore.RED + f'Era: {row[1]}')
print(Fore.RED + f'Time: {row[2]}')
alarm_triggered = True
break
```
- Clears the screen.
- Displays the alarm details in **red** using `colorama.Fore.RED`.
- Sets `alarm_triggered` to `True` and **exits the loop**.

---

### **9. No Alarm Found Handling**
```python
if not alarm_triggered:
    os.system('clear')
    print(Fore.MAGENTA + "No match...")
```
- If no alarm matches the current date and time, clears the screen and displays `No match...` in **magenta**.

---

### **10. Adding a Time Delay**
```python
time.sleep(1)
```
- Pauses execution for **1 second** to reduce CPU usage.

---

### **11. Handling User Interruption (CTRL+C)**
```python
except KeyboardInterrupt:
    print(Fore.YELLOW + "Program terminated by user.")
```
- Catches `KeyboardInterrupt` (CTRL+C) to allow graceful program termination.

---

### **12. Handling Other Exceptions**
```python
except Exception as e:
    print(Fore.RED + f"An error occurred: {e}")
```
- Catches any unexpected errors and displays the error message in **red**.

---

### **13. Closing the Database Connection**
```python
finally:
    con.close()
```
- Ensures the database connection is closed when the program exits.

---

## **Conclusion** 🎯
This script efficiently monitors alarms stored in an SQLite database, triggering them at the specified time. It includes:
- **Database validation** 🗄️
- **Continuous monitoring** 🔄
- **Error handling** 🚨
- **User-friendly display** 🎨

Happy Coding! 🚀


