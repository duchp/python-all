import os

class ImageRename():
    def __init__(self,r,s):
        self.path = r+ '/' + s
    def rename(self):
        filelist = os.listdir(self.path)
        total_num = len(filelist)

        n = 0
        for item in filelist:
            if item.endswith('.jpg'):
                oldname = os.path.join(os.path.abspath(self.path), item)
                newname = os.path.join(os.path.abspath(self.path), s+ format(str(n), '0>3s') + '.jpg')
                os.rename(oldname, newname)
                n += 1
        print ('total %d to rename & converted %d jpgs' % (total_num, n))

PHASE=['train','val']
SPECIES = ['rabbits', 'rats', 'chickens']

for p in PHASE:
    for s in SPECIES:
        newname = ImageRename(p,s)
        newname.rename()