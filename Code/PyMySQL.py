import pymysql
import random
import datetime
import string
'''
  fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
fetchall(): 接收全部的返回结果行.
rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。
'''
random.seed(datetime.datetime.now())
class MySql:
    def __init__(self, host, user, password, database): 
        self.host = host
        self.user = user
        self.pwd = password
        self.db = database
    def Connect(self):
        print("Connect")
        # 打开数据库连接 
        db = pymysql.connect(self.host, self.user, self.pwd, self.db ) 
        # 使用 cursor() 方法创建一个游标对象cursor 
        cursor = db.cursor() 
        # 使用 execute() 方法执行 SQL 查询 
        cursor.execute("SELECT VERSION()") 
        # 使用 fetchone() 方法获取单条数据. 
        data = cursor.fetchone() 
        print ("Database version : %s " % data) 
        # 关闭数据库连接 
        db.close()
    
    def Create(self):
        print("Create")
        # 打开数据库连接 
        db = pymysql.connect(self.host, self.user, self.pwd, self.db ) 
        # 使用 cursor() 方法创建一个游标对象 cursor 
        cursor = db.cursor() 
        # 使用 execute() 方法执行 SQL，如果表存在则删除 
        cursor.execute("DROP TABLE IF EXISTS EMPLOYEE") 
        # 使用预处理语句创建表 
        sql = """CREATE TABLE EMPLOYEE 
        ( FIRST_NAME CHAR(20) NOT NULL, 
        LAST_NAME CHAR(20),
        AGE INT, 
        SEX CHAR(1), 
        INCOME FLOAT )""" 
        cursor.execute(sql) 
        # 关闭数据库连接 
        db.close()
    
    def Insert(self):
        print("Insert")
        # 打开数据库连接 
        db = pymysql.connect(self.host, self.user, self.pwd, self.db )
        # 使用cursor()方法获取操作游标 
        cursor = db.cursor() 
        # SQL 插入语句 
        sql = """INSERT INTO EMPLOYEE
        (FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) 
        VALUES ('Mac', 'Mohan', 20, 'M', 2000)""" 
        try: 
            # 执行sql语句 
            cursor.execute(sql) 
            # 提交到数据库执行 
            db.commit() 
        except: 
            # 如果发生错误则回滚 
            db.rollback() 
            # 关闭数据库连接 
            db.close()
            
    def RandomInsert(self):
        print("RandomInsert")
        List = []
        # 打开数据库连接 
        db = pymysql.connect(self.host, self.user, self.pwd, self.db )
        # 使用cursor()方法获取操作游标 
        cursor = db.cursor() 
        for i in range(10):
            info = self.GetRandomInfo() 
            # SQL 插入语句 
            sql = """INSERT INTO EMPLOYEE
            (FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) 
            VALUES ('{}', '{}', {}, '{}', {})""".format(info[0], info[1], info[2], info[3], info[4])
            List.append(sql)
        try: 
            for s in List:
                # 执行sql语句 
                cursor.execute(s) 
                # 提交到数据库执行 
                db.commit() 
        except: 
            # 如果发生错误则回滚 
            db.rollback() 
            # 关闭数据库连接 
            db.close()
           
    def GetRandomInfo(self):
        
        age = random.randint(12,56)
        if random.randint(0,1) is 1:
            sex = 'M'
        else:
            sex = 'F'
        income = random.randint(2000, 2020)            
        fname = self.GetRandomName()
        lname = self.GetRandomName()
        info = (fname, lname, age, sex, income)
        
        return info

    def GetRandomName(self):
        s = string.ascii_lowercase
        name = ""
        for i in range(5):
            if i == 0:
                name = s[random.randint(0,25)].upper()
            else:
                name = name + s[random.randint(0,25)]
        return name    
    
    def Select(self):
        print("Select")
        # 打开数据库连接 
        db = pymysql.connect(self.host, self.user, self.pwd, self.db ) 
        # 使用cursor()方法获取操作游标 
        cursor = db.cursor() 
        # SQL 查询语句 
        sql = "SELECT * FROM EMPLOYEE WHERE INCOME > '%d'" % (1000) 
        try: 
            # 执行SQL语句 
            cursor.execute(sql) 
            # 获取所有记录列表 
            results = cursor.fetchall() 
            for row in results: 
                fname = row[0] 
                lname = row[1] 
                age = row[2] 
                sex = row[3] 
                income = row[4] 
                # 打印结果 
                print("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % (fname, lname, age, sex, income )) 
        except: 
            print ("Error: unable to fetch data") 
            # 关闭数据库连接 
            db.close()       
    def Update(self):
        print("Update")
        # 打开数据库连接 
        db = pymysql.connect(self.host, self.user, self.pwd, self.db ) 
        # 使用cursor()方法获取操作游标 
        cursor = db.cursor() 
        # SQL 更新语句 
        sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M') 
        try: 
            # 执行SQL语句 
            cursor.execute(sql) 
            # 提交到数据库执行 
            db.commit() 
        except: 
            # 发生错误时回滚 
            db.rollback() 
            # 关闭数据库连接 
            db.close()
            
    def Delete(self):
        print("Delete")
        # 打开数据库连接 
        db = pymysql.connect(self.host, self.user, self.pwd, self.db ) 
        # 使用cursor()方法获取操作游标 
        cursor = db.cursor() 
        # SQL 删除语句 
        sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20) 
        try: 
            # 执行SQL语句 
            cursor.execute(sql) 
            # 提交修改 
            db.commit() 
        except: 
            # 发生错误时回滚 
            db.rollback() 
            # 关闭连接 
            db.close()

if __name__ == "__main__":
    db = MySql('localhost', 'root', '123456', 'my')
    db.Connect()
    db.Create()
    db.Insert()
    db.RandomInsert()
    db.Select()
    #db.Update()
    #db.Delete()