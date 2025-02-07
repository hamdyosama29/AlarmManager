from datetime import datetime
from colorama import Fore
import sqlite3
import time
import os

con = sqlite3.connect('allarm_data.db')
cur = con.cursor()
try:
    while True:
        now = datetime.now()
        day = now.day
        month = now.month
        year = now.year
        hour = now.strftime('%I')
        minute = now.minute
        strftime = now.strftime('%p')
        calendar = f"{day}/{month}/{year}"
        now_time = f'{hour}:{minute:02d}{strftime}'
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='allarm'")
        if not cur.fetchone():
            print(Fore.RED + "Table 'allarm' does not exist.")
            break
        cur.execute('SELECT * FROM allarm')
        data = cur.fetchall()
        alarm_triggered = False
        for row in data:
            stored_date = row[1].strip()
            stored_time = row[2].strip()
            if now_time == stored_time and calendar == stored_date:
                os.system('clear')
                print(Fore.RED + f'Name: {row[0]}')
                print(Fore.RED + f'Era: {row[1]}')
                print(Fore.RED + f'Time: {row[2]}')
                alarm_triggered = True
                break
        if not alarm_triggered:
            os.system('clear')
            print(Fore.MAGENTA + "No match...")
        time.sleep(1)
except KeyboardInterrupt:
    print(Fore.YELLOW + "Program terminated by user.")
except Exception as e:
    print(Fore.RED + f"An error occurred: {e}")
finally:
    con.close()
