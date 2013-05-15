

class sortedList(object):
        
    def __init__(self, list):
        self.list = []
        for i in list:
            self.add(i)
            # self.show()
            
    # Ajoute la liste passee en parametre 
    def addList(self, list):
        for i in list:
            self.add(i)
    
    # Ajoute le nombre passe en parametre a la liste
    def add(self, n):
        # print("Adding %d to the list" % n)
        if len(self.list) == 0 or n > self.list[-1]:
            self.list.append(n)
            return 1
            
        a = 0
        b = len(self.list) - 1
        
        while True:
            i = (a + b)//2
                    
            di = n - self.list[i]
            
            if di == 0:#n deja dans la liste\
                # print("deja dans la liste", n)
                return 0
            
            if a == i:#a+1 == b
                if self.list[a] > n:
                    self.list.insert(a, n)
                    return 1
                else:
                    self.list.insert(a+1, n)
                    return 1
                
            if di > 0:
                a = i
            elif di < 0:
                b = i
                
    def __contains__(self, n):
        # print("Teste l'appartenance de %d" % n)
        # self.show()
        if n < self.list[0] or n > self.list[-1]:
            return False
            
        if n == self.list[-1]:
            return True
            
        a = 0
        b = len(self.list) - 1
        
        while True:
            i = (a + b)//2
            
            di = n - self.list[i]
            
            if di == 0:
                return True
                
            if a == i:
                return n == self.list[a]
                
            if di > 0:
                a = i
            elif di < 0:
                b = i
                
                
    def index(self, n):
        if n < self.list[0] or n > self.list[-1]:
            return -1
            
        if n == self.list[-1]:
            return len(self.list)-1
            
        a = 0
        b = len(self.list) - 1
        
        while True:
            i = (a + b)//2
            
            di = n - self.list[i]
            
            if di == 0:
                return i
                
            if a == i:
                if n == self.list[a]:
                    return a
                return -1
                
            if di > 0:
                a = i
            elif di < 0:
                b = i
    
    def __add__(self, stranger):
        newList = sortedList([])
        newList.list = self.list.copy()
        
        for i in stranger.list:
            newList.add(i)
            
        return newList
        
        
    def __len__(self):
        return len(self.list)
        
    def __getitem__(self, i):
        return self.list[i]
                
    def show(self):
        print(self.str())
        
    def str(self):
        return str(self.list)
        
    def __str__(self):
        return str(self.list)
        
    def size(self):
        return len(self.list)
        
    def sum(self):
        result = 0
        
        for i in self.list:
            # print(i)
            result += i
            
        return result    