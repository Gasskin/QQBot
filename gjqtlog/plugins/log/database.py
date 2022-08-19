from logging import logThreads
import sqlite3


# 玩家账号信息数据库
account = sqlite3.connect("Account.db")
cursorAccount = account.cursor()
# DPS的数据库
logDps = sqlite3.connect('Dps.db')
cursorDps = logDps.cursor()
# T的数据库
logTank = sqlite3.connect("Tank.db")
cursorTank = logTank.cursor()


cursorAccount.execute('SELECT * FROM Account')
rows = cursorAccount.fetchall()
for row in rows:
    print(row)


account.close()
logDps.close()
logTank.close()