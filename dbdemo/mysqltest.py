import pymysql as mysql
# 建立数据库连接
conn=mysql.connect(
    host='43.142.56.188',
    port=3306,
    user='root',
    database='testdb',
    password='123456',
    charset='utf8'
)
# 获取游标
cursor=conn.cursor()

# 创建数据库
# cursor.execute("create database if not exists testdb")



cursor.execute('drop table if exists testTable')
# 创建一个表
sql_createTable = '''create table `testTable` (
          `id` int not null auto_increment,
          `name` text not null ,
          primary key (`id`)    
        )'''
cursor.execute(sql_createTable)
print(sql_createTable)

# 插入多条
values=[]
for i in range(1,101):
    values.append("wyh"+str(i))

sql_insert='insert into testTable(name) values(%s)'
rows=cursor.executemany(sql_insert,values)
conn.commit()

#更新数据
sql_update='update testTable set name=%s where id =%s '
cursor.execute(sql_update,('helloworld','1'))
conn.commit()

# sql_query="select * from testTable "
# sql_condtion="where id > 55 "
# cursor.execute(sql_query+sql_condtion)
# result2=cursor.fetchmany(11)
# result=cursor.fetchall()
# print(result)
# print(result2)

sql1="select * from testTable"
sql2="select * from testTable where id >88"
cursor.execute(sql1)
cursor.execute(sql2)
print(cursor.fetchall())

# print(type(result))
# for row in result:
#     print(row)




cursor.close()
conn.close()
# # 执行sql语句
# sql='insert into test(id,name) values(%s,%s)'
# rows=cursor.execute(sql,('4','qzcsbj4'))
 
# # 提交
# conn.commit()
 
# # 关闭游标
# cursor.close()
 
# # 关闭连接
# conn.close()　　
