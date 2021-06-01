from django.shortcuts import render
import pymysql
# Create your views here.
def add_product(data):
    id=data['pid']
    name=data['pname']
    price=data['pprice']
    conn = pymysql.connect(user='root', password='root', host='db',port=3306, database='Products')
    cursor = conn.cursor()
    cmd="INSERT INTO products (pid,pname,pprice) VALUES ('"+str(id)+"',"+"'"+name+"',"+"'"+price+"');"
    print(cmd)
    try:
        cursor.execute(cmd)
        conn.commit()
    except:
        print("failed")
        conn.rollback()
    conn.close()
def create_table_products():
    conn = pymysql.connect(user='root', password='root', host='db',port=3306, database='Products')
    cursor = conn.cursor()
    cmd="CREATE TABLE products (pid int,pname varchar(255),pprice int);"
    print(cmd)
    try:
        cursor.execute(cmd)
        conn.commit()
    except:
        print("failed")
        conn.rollback()
    conn.close()
def get_prodcuct(id):
    conn = pymysql.connect(user='root', password='root', host='db',port=3306, database='Products')
    cursor = conn.cursor()
    cmd="Select * from products"
    print(cmd)
    try:
        cursor.execute(cmd)
        data=cursor.fetchall()
        # for i in data:
        #     print(i)
        conn.commit()
    except:
        print("failed")
        conn.rollback()
    conn.close()
    return data
def index(request):
    try:
        conn = pymysql.connect(user='root', password='root', host='db',port=3306)
        cursor = conn.cursor()
        cmd="Create database Products;"
        print(cmd)
        cursor.execute(cmd)
        conn.commit()
    except:
        print("failed")
        conn.rollback()
    conn.close()
    return render(request, 'index.html', {})
def create_product(request):
    data=(request.POST) 
    try:
        create_table_products()
    except:
        pass
    try:
        add_product(data)
    except:
        pass
    return render(request, "create.html",{}) 

def retrive_product(request):
    data=get_prodcuct(1)
    datal=[]
    for i in data:
        # print(i)
        datal.append(i)
    d={}
    d['data']=datal
    print(d['data'])
    
    return render(request,'retrive.html',d)
    
def search_p(data):
    try:
        id=data['pid']
        conn = pymysql.connect(user='root', password='root', host='db',port=3306, database='Products')
        cursor = conn.cursor()
        cmd="Select * from products where pid="+id+";"
        try:
            cursor.execute(cmd)
            dataq=cursor.fetchall()
            # for i in dataq:
            #     print(i)
            conn.commit()
        except:
            print("failed")
            conn.rollback()
        conn.close()
        return dataq
    except:
        pass
    
    


    
def search_product(request):
    data=(request.POST)
    data=search_p(data)
    datal=[]
    try:
        for i in data:
            datal.append(i)
    except:
        pass
    d={}
    d['data']=datal
    print(d['data'])

    return render(request,'search.html',d)



