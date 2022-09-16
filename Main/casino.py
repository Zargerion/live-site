import sqlite3
import os
import random


def call_casino(request):
    with sqlite3.connect(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + r"\db.sqlite3") as db:
        cursor = db.cursor()
        chance = random.randint(0, 300)
        balance = int(''.join(str(x) for x in cursor.execute(r"""
            SELECT score FROM auth_user WHERE username LIKE (?)
            """, (request.user.username,)).fetchone()))
        if balance <= 1:
            pass
        else:
            if chance < 100:
                cursor.execute(r"""
                    UPDATE auth_user SET score = score * 2 WHERE username LIKE (?)
                    """, (request.user.username,))
            else:
                cursor.execute(r"""
                    UPDATE auth_user SET score = score / 2 WHERE username LIKE (?)
                    """, (request.user.username,))





#    for user in cursor.execute("""
#        SELECT username FROM auth_user
#    """):
#        print(user)
#       cursor.execute("""
#           ALTER TABLE auth_user
#           ADD COLUMN score 'bigint' DEFAULT 1000
#           """)
#    cursor.execute("""
#        ALTER TABLE auth_user
#        DROP score;
#        """)
