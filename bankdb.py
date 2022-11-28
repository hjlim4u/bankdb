import pymysql as pms

def authorize():
    admin_ssn = input('essn: ')

    connection = pms.connect(host='localhost', port=3306, user='root', password='gudwn1211~', db='bankDB',
                             charset='utf8')
    cursor = connection.cursor()
    verify_sql = '''
    SELECT essn
    FROM admin
    '''
    cursor.execute(verify_sql)
    authorization = cursor.fetchall()
    for essn in authorization:
        if admin_ssn in essn:
            connection.commit()
            connection.close()
            return True
    print("No authorization, please input valid essn.")
    connection.commit()
    connection.close()
    return False



while True:
    option = int(input('0.Exit\n1.customer menu\n2.admin menu\n'))
    if option == 0:
        break
    if option == 1:
        option2 = int(input('0.Return to previous menu\n1.Register User\n2.Create account\n3.deposit/withdraw money\n'))
        if not option2:
            continue
        if option2 == 1:
            name = input('name : ')
            sex = input('sex:  ')
            ssn = input('ssn: ')
            phone = input('phone: ')
            address = input('address: ')
            ID = input('ID: ')
            answer = input('where are you from?: ')
            connection = pms.connect(host='localhost', port=3306, user='root', password='gudwn1211~', db='bankDB',charset='utf8')
            cursor = connection.cursor(pms.cursors.DictCursor)
            regsql = '''
            INSERT INTO user
            values (%s, %s, %s, %s, %s, %s, %s);
            '''
            cursor.execute(regsql, (name, sex, ssn, phone, address, ID, answer))
            connection.commit()
            connection.close()
            print('user created: '+name)
            continue
        if option2 == 2:
            userID = input('userID: ')
            account_name = input('account name: ')
            account_number = input('account number: ')
            pwd = int(input('password: '))
            interest = float(input('interest rate: '))
            connection = pms.connect(host='localhost', port=3306, user='root', password='gudwn1211~', db='bankDB',
                                     charset='utf8')
            cursor = connection.cursor(pms.cursors.DictCursor)
            acsql = '''
            INSERT INTO account
            values (%s, %s, %s, %s, %s, %s);
            '''
            cursor.execute(acsql, (account_name, account_number, pwd, interest, userID, 0))
            connection.commit()
            connection.close()
            continue
        if option2 == 3:
            user = input('user id: ')
            account = input('account number: ')
            plusorminus = input('deposit or withdraw? (dep/with): ')
            money = int(input('amount of money(+): '))
            pwd = int(input('password: '))
            connection = pms.connect(host='localhost', port=3306, user='root', password='gudwn1211~', db='bankDB',
                                     charset='utf8')
            cursor = connection.cursor()
            pwdsql = "SELECT password FROM account WHERE userID=%s and ac_number=%s;"
            cursor.execute(pwdsql, (user, account))
            pwdresult = cursor.fetchone()
            if pwd != pwdresult[0]:
                answer=input("Wrong password, Where are you from?")
                anssql = '''
                SELECT answer FROM user WHERE ID=%s;
                '''
                cursor.execute(anssql, user)
                location = cursor.fetchone()

                if answer != location:
                    print("Wrong password, Please try again.")
                    connection.commit()
                    connection.close()
                    continue
                print("Your password is " + pwdresult)
            absolute = money
            if plusorminus == 'with':
                money = money * (-1)

            moneysql = "SELECT money FROM account WHERE userID=%s and ac_number=%s;"
            cursor.execute(moneysql, (user, account))
            balance = cursor.fetchone()
            money = money + balance[0]
            if money < 0:
                print("No money, your balance is"+str(balance[0]))
                connection.commit()
                connection.close()
                continue
            updatesql = "UPDATE account SET money = %s WHERE userID=%s and ac_number=%s;"
            cursor.execute(updatesql, (money, user, account))
            print('update complete: your account '+account+ ' balance is '+str(money))
            histsql = '''
            INSERT INTO history(userID, accountID, deporwith, amount)
            VALUES (%s, %s, %s, %s);
            '''
            cursor.execute(histsql, (user,account, plusorminus, absolute))
            connection.commit()
            connection.close()
            continue
    if option == 2:
        option3 = int(input('0.Return to previous menu\n1.Register admin\n2.View user\n3.View stats\n4.View history\n5.fire admin\n'))
        if not option3:
            continue
        if option3 == 1:
            admin_name = input('admin name: ')
            admin_ssn = input('essn: ')
            admin_depart = input('department: ')
            connection = pms.connect(host='localhost', port=3306, user='root', password='gudwn1211~', db='bankDB',
                                     charset='utf8')
            cursor = connection.cursor(pms.cursors.DictCursor)
            admin_sql='''
            INSERT INTO admin
            VALUES (%s, %s, %s);
            '''
            cursor.execute(admin_sql, (admin_name, admin_ssn, admin_depart))
            connection.commit()
            connection.close()
            print("admin name "+admin_name+" registered")
            continue
        if option3 == 2:
            if not authorize():
                continue

            connection = pms.connect(host='localhost', port=3306, user='root', password='gudwn1211~', db='bankDB',
                                     charset='utf8')
            cursor = connection.cursor(pms.cursors.DictCursor)

            user = input('userID: ')


            viewsql = '''
            SELECT *
            FROM user_account
            WHERE userID=%s'''
            cursor.execute(viewsql, user)
            useraccount = cursor.fetchall()
            print(useraccount)
            connection.commit()
            connection.close()
            continue

        if option3 == 3:
            if not authorize():
                continue
            connection = pms.connect(host='localhost', port=3306, user='root', password='gudwn1211~', db='bankDB',
                                     charset='utf8')
            cursor = connection.cursor(pms.cursors.DictCursor)
            statsql='''
            SELECT userID, COUNT(*), AVG(amount)
            FROM history
            GROUP BY userID
            '''
            cursor.execute(statsql)
            statistics = cursor.fetchall()
            print(statistics)
            connection.commit()
            connection.close()

        if option3 == 4:
            if not authorize():
                continue
            user = input('userID: ')
            connection = pms.connect(host='localhost', port=3306, user='root', password='gudwn1211~', db='bankDB',
                                     charset='utf8')
            cursor = connection.cursor(pms.cursors.DictCursor)
            detailsql='''
            SELECT *
            FROM history
            WHERE userID=%s'''
            cursor.execute(detailsql, user)
            details=cursor.fetchall()
            print(details)
            continue
        if option3 == 5:
            if not authorize():
                continue
            connection = pms.connect(host='localhost', port=3306, user='root', password='gudwn1211~', db='bankDB',
                                     charset='utf8')
            cursor = connection.cursor(pms.cursors.DictCursor)
            essn=input('input essn of fired employee: ')
            firesql='''
            DELETE FROM admin
            WHERE essn=%s'''
            cursor.execute(firesql, essn)
            connection.commit()
            connection.close()
            print('employee fired: '+ essn)



