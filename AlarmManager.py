from datetime import datetime
from colorama import  Fore
import sqlite3
import os
os.system('clear')
while True:
    try:
        con = sqlite3.connect(r'allarm_data.db')
        ta = con.cursor()
        print(Fore.RED + 'Data entry: 1')
        print( 'View data: 2')
        print( 'Update of data: 3')
        print( 'Delete data: 4')
        print( 'Exit: 0')
        print('-----------------------------------------')
        enter = int(input(Fore.MAGENTA +'Enter: '))
        print(Fore.RED + '-----------------------------------------')
        if enter == 1:
            datatime = datetime.now()
            day = datatime.day
            month = datatime.month
            year = datatime.year
            hour = datatime.hour
            strftime = datetime.now().strftime('%p')
            minute = datatime.minute
            insert_Day = int(input(Fore.MAGENTA + 'Insert Day: ') or day)
            insert_Month = int(input('Insert Month: ') or month)
            insert_Year = int(input('Insert Year: ') or year)
            insert_name = input('Insert Name: ').title()
            print(Fore.RED + '-----------------------------------------')
            insert_hour = int(input(Fore.MAGENTA + 'Insert Hour: ') or hour)
            insert_minute = int(input('Insert Minute: ') or minute)
            insert_strftime = input('Insert PM/AM: ').upper() or strftime
            print(Fore.RED + '-----------------------------------------')

            if not (1 <= insert_Day <= 31):
                print(Fore.RED + 'Error! Invalid day.')
                continue
            if not (1 <= insert_Month <= 12):
                print('Error! Invalid month.')
                continue
            if not (1 <= insert_hour <= 12):
                print('Error! Invalid hour.')
                continue
            if not (0 <= insert_minute <= 59):
                print('Error! Invalid minute.')
                continue
            if not insert_name:
                print('Please enter a valid integer for name.')


            ta.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = ta.fetchall()
            table_names = [table[0] for table in tables]
            if 'allarm' not in table_names:
                ta.execute('CREATE TABLE allarm(title TEXT, date TEXT, time TEXT)')
            ta.execute("INSERT INTO allarm(title, date, time) VALUES(?, ?, ?)", 
                   (insert_name, f"{insert_Day}/{insert_Month}/{insert_Year}", f"{insert_hour}:{insert_minute}{insert_strftime}"))
            ta.execute("SELECT * FROM allarm")
            sd = ta.fetchall()
            for i in sd:
                print(Fore.MAGENTA + f'Name: {i[0]}')
                print(Fore.MAGENTA + f'Era: {i[1]}')
                print(Fore.MAGENTA + f'Time: {i[2]}')
            print(Fore.RED + '-----------------------------------------')
        elif enter == 2:
            ta.execute("SELECT * FROM allarm")
            sd = ta.fetchall()
            for i in sd:
                print(Fore.MAGENTA + f'Name: {i[0]}')
                print(Fore.MAGENTA + f'Era: {i[1]}')
                print(Fore.MAGENTA + f'Time: {i[2]}')
                print(Fore.RED +'-----------------------------------------')
        elif enter == 3:
            try:
                title_delete = str(input(Fore.MAGENTA + 'Enter the title : ').title())
            except Exception as e:
                print(Fore.RED + '-----------------------------------------')
                print(e)
                print('-----------------------------------------')
                continue
            change = input(Fore.MAGENTA + 'Enter what you want to change title/date/time: ')
            if change == 'title':
                word = input('Enter the word you want to change: ').title
                ta.execute(f"UPDATE allarm SET title = ? WHERE title = ?", (word, title_delete))
                ta.execute("SELECT * FROM allarm")
                sd = ta.fetchall()
                for i in sd:
                    print(Fore.MAGENTA + f'Name: {i[0]}')
                    print(Fore.MAGENTA + f'Era: {i[1]}')
                    print(Fore.MAGENTA + f'Time: {i[2]}')
                print( Fore.RED + '-----------------------------------------')
            elif change == 'date':
                update_day = int(input(Fore.MAGENTA + 'Insert Day: ') or day)
                update_month = int(input("Insert Month: ") or month)
                update_year = int(input("Insert Month: ") or year)            
                ta.execute(f"UPDATE allarm SET date = ? WHERE title = ?",(f'{update_day}/{update_month}/{update_year}',title_delete))
                ta.execute("SELECT rowid,* FROM allarm")
                sd = ta.fetchall()
                for i in sd:
                    print(Fore.MAGENTA + f'Name: {i[0]}')
                    print(Fore.MAGENTA + f'Era: {i[1]}')
                    print(Fore.MAGENTA + f'Time: {i[2]}')
                print(Fore.RED + '-----------------------------------------')
            elif change == 'time':
                strftime = datetime.now().strftime('%p')
                update_hour = int(input(Fore.MAGENTA + 'Insert Hour: ') or hour)
                update_minute = int(input('Insert Minute: ') or minute)
                update_strftime = input('Insert PM/AM: ').upper() or strftime
                ta.execute(f"UPDATE allarm SET time = ? WHERE title = ?",(f'{update_hour}:{update_minute}{update_strftime}',title_delete))
                ta.execute("SELECT rowid,* FROM allarm")
                sd = ta.fetchall()
                for i in sd:
                    print(Fore.MAGENTA + f'Name: {i[0]}')
                    print(Fore.MAGENTA + f'Era: {i[1]}')
                    print(Fore.MAGENTA + f'Time: {i[2]}')
                print(Fore.RED + '-----------------------------------------')
            else:
                print('The value you entered does not exist in the database.')
                print('-----------------------------------------')
                continue
        elif enter == 4:
            while True:
                delete_name = input(Fore.MAGENTA + "Enter the name of the row you want to delete form the data / title: ").title()
                ta.execute("SELECT 1 FROM allarm WHERE title = ?",(delete_name,))
                result = ta.fetchone()
                if result:
                    ta.execute("DELETE FROM allarm WHERE title = ?",(delete_name,))
                    con.commit()
                    print(f'The row with title {delete_name} has been delete.')
                    print(Fore.RED + '-----------------------------------------')
                    break
                else:
                    print(f'The name is not found: {delete_name}.')
                    print('-----------------------------------------')
                    continue
        elif enter == 0:
            break
        else:
            print('Error!')
            print('-----------------------------------------')
            continue
        con.commit()
        con.close()
    except Exception as e:
        print(f'Obviously there was an error, please try again.\n{e}')
        print('-----------------------------------------')
        continue
    