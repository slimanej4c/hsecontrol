import tkinter
from tkinter import *
from datetime import datetime
import time
from tkinter import ttk
import time


import processus_db

import data
data.createdata()

date_now = time.strftime('%d%m%Y')
data.open_data()
data.list_date_date()
list_date=data.list_date
data.mydb.close()
date_now1=int(date_now)
print(date_now1)

if str(date_now1) in str(data.list_date):
    print("ok it is")

else:
    data.insert_date_id(date_now)
    data.list_site.clear()
    list_site = data.list_site
    data.list_site_site()

    data.insert_vsite(date_now, list_site)



class part_1:

    def __init__(self,root):
        self.root=root

    def widget_part_1(self):
        import build_site
        go_part_2=build_site.part_2(self.root)
        go_part_2.global_()


if __name__ == "__main__":
    root = Tk()
    depart=part_1(root)
    depart.widget_part_1()
    root.mainloop()



