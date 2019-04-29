#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sqlite3,os
#导入模块
# os.system('CHCP 65001')
vulnDB = 'vuln.db'

conn = sqlite3.connect(vulnDB)
#读取文件
conn.text_factory = lambda x: str(x, 'gbk', 'ignore')
#不太清楚是啥。加进去先

sqlread = r"""select * from VULNDB"""

sqlwrite = r"""insert into VULNDB1 (Plugin_ID,NAME,Risk,Description,Solution) values(?,?,?,?,?)"""


for i in conn.execute(sqlread).fetchall():
  
    print(i)

    para = i

    conn.execute(sqlwrite,para)

conn.commit()       
