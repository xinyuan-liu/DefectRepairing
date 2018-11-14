import json
import os
import multiprocessing
import random
import time
from multiprocessing import Manager
import requests
nb_workers=10
running_state=multiprocessing.Array('B',nb_workers+1)

def process(worker):
    while(True):
        patch_id=requests.get('http://127.0.0.1:8000').text
        if patch_id=='-1':
            break
        f=os.path.join('tool/patches/INFO',str(patch_id)+".json")
        f=open(f)
        data=json.load(f)
        f.close()
        project=data['project']
        if project=="Closure" or project=="Mockito":
            continue
        bug_id=data['bug_id']
        os.system('cd worker%s/source && python3 run.py %s %s %s >%s.stdout 2>%s.stderr'%(str(worker),project,bug_id,patch_id,patch_id,patch_id))
#init workers
for i in range(1,nb_workers+1):
    if os.path.exists('worker%d'%i):
        continue
    os.system('mkdir worker%d'%i)
    os.system('cp -r tool worker%d/'%i)


pool = multiprocessing.Pool(processes=nb_workers)

for i in range(1,nb_workers+1):
    pool.apply_async(func=process, args=(i,))

pool.close()
pool.join()
