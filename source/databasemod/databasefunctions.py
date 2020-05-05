import sqlite3 as sq
import traceback
import hashlib

# encryption function to secure the passwords store in the DB
# while autoristaion of sign in only the hashcode will be compared
# plain text will be used to generate tokens only and only the hashes are stored
def EncryptString(password):
    sha_signature = \
        hashlib.sha256(password.encode()).hexdigest()
    return sha_signature

# connecting to database with relative path
try:
    con = sq.connect("database.db") # the database is in the ssame path as this module
    cur = con.cursor()
except Exception:
    print("Database error occurred ")
    # print(traceback.)
    traceback.print_exc()  # printing stack trace for the error occurred


# declaring required functions

# function to fetch user credentials form the database
def fetch_cred(user):
    global con, cur
    try:
        cur.execute(f"select * from user where name='{user}'")
        return cur.fetchall()
    except Exception:
        print("Error while trying to fetch creds")
        traceback.print_exc()
        return None

# function to obtain all the posts that were uploaded by the user of given type
def fetch_posts(user, type):
    global con, cur
    try:
        cur.execute(f"select * from posts where post_by='{user}' and post_type='{type}'")
        return cur.fetchall()
    except Exception:
        print("Eror while trying to fetch posts")
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
        cur.execute(f"select * from posts where post_by='{user}' and post_type='{type}' and exp=1")
        return cur.fetchall()
    except Exception:
        print("Eror while trying to fetch posts")
        traceback.print_exc()
        return None

# function to add a new user
# add user func
# add post func
# print(EncryptString("Balarubinan"))