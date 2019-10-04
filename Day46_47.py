class Library:
  def __init__(self,book,shelf):
      self.book=book
      self.shelf=shelf


class science_section(Library):
    
    def __init__(self,book,shelf,name):
     super().__init__(book,shelf)
     self.name=name
    def printInfo(self):
        print("book:", self.book,"self:",self.shelf,"name",self.name) 




obj=science_section(300,45,"Physics books")
obj.printInfo()        
obj2=science_section(20,4,"Physics books")
obj2.printInfo()        
