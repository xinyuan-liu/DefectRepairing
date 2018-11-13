import json
import os
import multiprocessing
import random
import time
from multiprocessing import Manager

nb_workers=10
running_state=multiprocessing.Array('B',nb_workers+1)

def process(Patch):
    lock=running_state._lock
    lock.acquire()
    worker=0
    for i in range(1,nb_workers+1):
        if running_state[i]==0:    
            worker=i
            running_state[i]=1
            break
    lock.release()
    if worker==0:
        print(error)
        return 1    
    print(worker,end='\t')
    print(Patch)
    project,bugid,patch_no=Patch
    os.system('cd worker%s/tool/source && python3 run.py %s %s %s >%s.stdout 2>%s.stderr'%(str(worker),project,bugid,patch_no,patch_no,patch_no))
    
    
    lock.acquire()
    running_state[worker]=0
    lock.release()


#patch_no_List=list(range(1,211))
#patch_no_List+=['HDRepair1', 'HDRepair2', 'HDRepair3', 'HDRepair4', "HDRepair5", "HDRepair6", "HDRepair7", "HDRepair8", "HDRepair9", 'HDRepair10']

patch_no_List=['%dh'%i for i in list(range(1,317))+list(range(318,396))]

#init workers
for i in range(1,nb_workers+1):
    if os.path.exists('worker%d'%i):
        continue
    os.system('mkdir worker%d'%i)
    os.system('cp -r tool worker%d/tool'%i)

List=[]
for patch_no in patch_no_List:
    f=os.path.join('tool/patches/INFO',"Patch"+str(patch_no)+".json")
    f=open(f)
    data=json.load(f)
    f.close()
    project=data['project']
    if project=="Closure" or project=="Mockito":
        continue
    bugid=data['bug_id']
    patch_no=data['ID']
    List.append((project,bugid,patch_no))
print(len(List))
print(List)
input()

pool = multiprocessing.Pool(processes=nb_workers)

for Patch in List:
    pool.apply_async(func=process, args=(Patch,))

pool.close()
pool.join()
