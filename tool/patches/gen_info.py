import os
from unidiff import PatchSet
import json
projects=['Chart','Time','Lang','Closure','Math','Mockito']
l=os.listdir('.')
for patch_file in l:
    info={}
    try:
        patch = PatchSet.from_filename(patch_file)
        target_file=patch[0].source_file
    
    except:
        continue
    s=target_file.split('/')[0]
    info['ID']=patch_file
    s=s.split('_')[0]
    info['tool']='SimGen'
    info['correctness']='Incorrect'
    for p in projects:
        if p in s:
            info['project']=p
            info['bug_id']=s[len(p):-1]
    
    #print(info)
    f=open('INFO/%s.json'%patch_file,'w')
    json.dump(info,f)
    f.close()
