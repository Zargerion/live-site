# venv\Scripts\deactivate

# venv\Scripts\activate

# Если css не хочет обновляться чисти кеш браузера (ctrl+shift+del).
# Если выдает тупые ошибки перезайди в venv, manage.py migrate.

import sys
import os
import time

sys.stdout.write("If you want to activate venv enter *a*.\nIf you want to activate venv enter *d*.\n")
for i in range(40):
    sys.stdout.write("\r{0}>".format("=" * i))
    sys.stdout.flush()
    time.sleep(0.05)
sys.stdout.write('\nEnter here:')


def decide_1():
    input_com = input()
    if input_com == 'a':
        sys.stdout.write(os.path.dirname(os.path.abspath(__file__)) + r">venv\Scripts\activate")
    elif input_com == 'd':
        sys.stdout.write("(venv) " + os.path.dirname(os.path.abspath(__file__)) + r">venv\Scripts\deactivate")
    else:
        decide_1()


decide_1()

# Так я открыл для себя много нового =(
