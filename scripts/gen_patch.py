import os
import sys

def gen_patch(source,target,patch_file):
    global path
    f=open(os.path.join(path,'defects4j.build.properties'))
    for line in f:
        line=line.strip()
        if line[0]=='#':
            continue
        pair=line.split('=')
        if pair[0]=='d4j.dir.src.classes':
            path2src=pair[1]
            break
    os.system('cd %s/.. && diff -r -u -w %s %s > %s'%(path,os.path.join(source,path2src),os.path.join(target,path2src),patch_file))

if __name__=='__main__':
    global path
    path=sys.argv[1]
    #gen_patch(sys.argv[0],sys.argv[1],sys.argv[2])
    if path[-1]=='/':
        path=path[:-1]
    cur_dirname=path.split('/')[-1]
    l=cur_dirname.split('_')
    project=l[0].title()
    bug_id=l[1]
    source=project+bug_id+'b'
    target=cur_dirname
    patch_dir=os.path.join(path,'../../..','patch_SimGen')
    patch_file=os.path.join(patch_dir,'PatchSimGen%d'%(len(os.listdir(patch_dir))))
    gen_patch(source,target,patch_file)
