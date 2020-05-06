import sqlite3 as sq
import traceback
import hashlib
from datetime import datetime


# encryption function to secure the passwords store in the DB
# while autoristaion of sign in only the hashcode will be compared
# plain text will be used to generate tokens only and only the hashes are stored
def EncryptString(password):
    sha_signature = \
        hashlib.sha256(password.encode()).hexdigest()
    return sha_signature

#
# # connecting to database with relative path
# def get_db():
try:
    con = sq.connect("D:\html projects\Hackathon project\source\database.db")  # the database is in the ssame path as this module
    cur = con.cursor()
except Exception:
    print("Database error occurred ")
    traceback.print_exc()  # printing stack trace for the error occurred

# declaring required functions

# function to fetch user credentials form the database
def fetch_cred(user):
    global con, cur
    try:
        cur.execute(f"select * from user where name='{user}'")
        print(cur.fetchall())
        return cur.fetchall()
    except Exception:
        print("Error while trying to fetch creds")
        traceback.print_exc()
        return None


# function to obtain all the posts that were uploaded by the user of given type
def fetch_posts(cur,user, type):
    # global con, cur
    try:
        cur.execute(f"select * from posts where post_by='{user}' and post_type='{type}'")
        return cur.fetchall()
    except Exception:
        print("Eror while trying to fetch posts")
        traceback.print_exc()
        return None

#fetches a particular auction with title given

def fetch_auction(title):
    global con, cur
    try:
        cur.execute(f"select * from auction where title='{title}'")
        return cur.fetchall()
    except Exception:
        print("Error while trying to fetch auctions")
        traceback.print_exc()
        return None

# function to obtain the list of auctions
def fetch_auctions():
    global con, cur
    try:
        cur.execute("select * from auction")
        return cur.fetchall()
    except Exception:
        print("Error while trying to fetch auctions")
        traceback.print_exc()
        return None


# function to fetch historical posts
def fetch_his_posts(user,type):
    global con, cur
    try:
        cur.execute(f"select * from posts where post_by='{user}' and post_type='{type}'")
        return cur.fetchall()
    except Exception:
        print("Error while trying to fetch posts")
        traceback.print_exc()
        return None

# function to add a new user
def add_user(user):
    global con,cur
    try:
        cur.execute(f"insert into user values(?,?,?,?,?,?)",[user.name,user.email,user.phone,user.address,EncryptString(user.password),user.type])
        return True
    except Exception:
        print("Error while trying to insert into database")
        traceback.print_exc()
        return None

# fucntion to add posts
def add_post(post_title,post_descrpt,post_by,post_type):
    global cur,con
    try:
        datenow=datetime.now() # to get current date and time
        cur.execute("insert into posts values(?,?,?,?,?)",[post_title,post_descrpt,post_by,post_type,datenow])
        return True
    except Exception:
        return False

# print(get_db().execute("select * from user"))
# print(EncryptString("Bala"))
# print(fetch_cred("bala"))