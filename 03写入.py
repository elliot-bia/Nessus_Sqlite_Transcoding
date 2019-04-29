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

res = conn.execute(
            r"""select * from VULNDB""").fetchone()
#     # print(type(res.fetchone()))
#     pluginID, vulname, _, vul_desc, vul_solu = res
print(res)

sql = r"""insert into VULNDB1 (Plugin_ID,NAME,Risk,Description,Solution) values(?,?,?,?,?)"""

para = res

conn.execute(sql,para)

conn.commit()
