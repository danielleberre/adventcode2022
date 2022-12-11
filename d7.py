import fileinput

class FSItem:
    def __init__(self,name):
        self.name = name
    
    def set_parent(self,parent):
        self.parent = parent

    def go_back(self):
        return self.parent

    def get_name(self):
        return self.name

    def size(self):
        pass

class Directory(FSItem):
    
    def __init__ (self,name):
        super().__init__(name)
        self.content= []
        self.cached = -1

    def append(self,f):
        f.set_parent(self)
        self.content.append(f)
        self.cached = -1
    
    def change_directory(self,name):
        return list(filter(lambda v: (v.get_name() == name), self.content))[0]

    def size(self):
        if self.cached>0:
            return self.cached
        my_sum = 0
        for c in self.content:
            my_sum += c.size()
        self.cached = my_sum
        return my_sum

    def __str__(self):
        return " ".join([str(i) for i in self.content])

    def visit(self,list):
        for c in self.content:
            c.visit(list)
        s = self.size()
        if s<100000:
            list.append(s)

    def visit2(self,list,value):
        for c in self.content:
            c.visit2(list,value)
        s = self.size()
        if s>value:
            list.append(s)
    
class File(FSItem):
    def __init__(self,name,size):
        self.name = name
        self.file_size = size

    def size(self):
        return self.file_size

    def __str__(self):
        return self.name + " " + str(self.file_size)

    def visit(self,list):
        pass

    def visit2(self,list,value):
        pass

ROOT = Directory("/")
pwd = ROOT

for line in fileinput.input():
    words = line.split(' ')
    if "$" == words[0]:
        if "cd" == words[1]:
            name = words[2].strip()
            if ".." == name:
                pwd = pwd.go_back()
            elif "/" ==  name:
                pwd = ROOT
            else:
                pwd = pwd.change_directory(name)
    else:
        name = words[1].strip()
        if "dir" == words[0]:
            fsi = Directory(name)
        else:
            fsi = File(name, int(words[0]))
        pwd.append(fsi)

sizes = []
ROOT.visit(sizes)
print(sum(sizes))
available = 70000000 - ROOT.size()
tofind = 30000000 - available
sizes = []
ROOT.visit2(sizes,tofind)
sizes.sort()
print(sizes[0])        

