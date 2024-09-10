#!/usr/bin/env python3
from dev_aberto.dev_aberto import hello
from datetime import datetime
import babel.dates as bd

import gettext
gettext.bindtextdomain('hello', 'locale')
gettext.textdomain('hello')
_ = gettext.gettext

if __name__ == '__main__':
    date, name = hello()

    date_formated = ""
    for i in date:
        if i == "-":
            date_formated += "/"
        elif (i.isalpha() and i.isdigit() == False) == False:
            date_formated += i
        else:
            date_formated += " "
    date_formated = date_formated[:-1]

    print(_("Último commit feito em: {} por {}").format(bd.format_datetime(datetime.strptime(date_formated, '%Y/%m/%d %H:%M:%S')), name))