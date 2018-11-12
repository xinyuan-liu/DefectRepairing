import os
import sys

def gen_patch(source,target,patch_file):
    f=open(os.path.join('defects4j.build.properties'))
    for line in f:
        line=line.strip()
        if line[0]=='#':
            continue
        pair=line.split('=')
        if pair[0]=='d4j.dir.src.classes':
            path2src=pair[1]
            break
    os.system('cd .. && diff -r -u -w %s %s > %s'%(os.path.join(source,path2src),os.path.join(target,path2src),patch_file))

if __name__=='__main__':
    #gen_patch(sys.argv[0],sys.argv[1],sys.argv[2])
    cur_dirname=os.getcwd().split('/')[-1]
    l=cur_dirname.split('_')
    project=l[0].title()
    bug_id=l[1]
    source=project+bug_id+'b'
    target=cur_dirname
    patch_file=os.path.join('patch_SimGen','PatchSimGen%s%d'%(project,len(os.listdir('../patch_SimGen'))))
    gen_patch(source,target,patch_file)
