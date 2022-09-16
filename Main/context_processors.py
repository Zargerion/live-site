import os
import sqlite3
from Main.casino import call_casino


# To func will work with @request@ init it by sitting.py in context_processors


def score(request):
    with sqlite3.connect(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + r"\db.sqlite3") as db:

        cursor = db.cursor()
        cursor.execute(r"""
           SELECT score FROM auth_user WHERE username LIKE (?)
           """, (request.user.username,))  # takes other field by using one of field of string

    if request.user.is_authenticated:
        the_variable = ''.join(str(x) for x in cursor.fetchone())  # change () type to str type for int types in ()
    else:
        the_variable = "0"
    return {
        'score_out': the_variable
    }
