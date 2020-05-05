import sqlite3 as sq
import traceback

# connecting to database with relative path
try:
    con = sq.connect("/database.db")
    cur = con.cursor()
except Exception:
    print("Database error occured ")
    # print(traceback.)
    traceback.print_exc()  # printing stacck trace for he error occured

# declaring required functions

#fuction to fetch user creditentials form the database
def fetch_cred(user):