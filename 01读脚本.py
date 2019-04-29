import csv
import os
import sqlite3
import sys
import time


from openpyxl import Workbook, load_workbook

vulnDB = 'vuln.db'

conn = sqlite3.connect(vulnDB)
conn.text_factory = lambda x: str(x, 'gbk', 'ignore')



# print(pluginID, host, protocol, port,
        #   vulname, risk, vul_desc, vul_solu)
res = conn.execute(
    r"""select * from VULNDB""").fetchone()
if res:
# print(res[2])
pluginID, vulname, _, vul_desc, vul_solu = res
#yield (host, port, protocol, vulname, risk, vul_desc, vul_solu)
