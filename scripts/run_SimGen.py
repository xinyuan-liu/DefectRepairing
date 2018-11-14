import os

projects={"chart":26,"lang":65,"math":106,"time":27}
base_dir='/disk/ICSE18Extend'

for project in projects:
    for bug_id in range(1,projects[project]+1):
        tar_dir=os.path.join(base_dir,'SimGen_Repo',project,"%s_%d_buggy"%(project,bug_id))
        if not os.path.exists(tar_dir):
            os.system('defects4j checkout -p %s -v %db -w %s'%(project.title(),bug_id,tar_dir))
        bas_dir=os.path.join(base_dir,'SimGen_Repo',project,"%s%db"%(project.title(),bug_id))
        if not os.path.exists(bas_dir):
            os.system('cp -r %s %s'%(tar_dir,bas_dir))
        os.system('cd %s && java -jar SimGen.jar --proj_home=%s --proj_name=%s --bug_id=%d'%(os.path.join(base_dir,'SimFix'),os.path.join(base_dir,'SimGen_Repo'),project,bug_id))
