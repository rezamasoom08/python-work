# When you want to allow only one object from a class

class Borg:

    _shared_data = {} #Attribute dictionary

    def __init__(self):
        self.__dict__ = self._shared_data #Make an attribute dictionary

class Singleton(Borg):
    def __init__(self, **kwargs):
        Borg.__init__(self)
        self._shared_data.update(kwargs)  #Update the attribute dictionary by insertinga new key-value pair
        
    def __str__(self):
        return str(self._shared_data) #Returns attribute dictionary for printing
    
# Let's create a sinleton object and add our first acronym

x = Singleton(HTTP = "Hype Text Transfer Protocol")
print(x)

y = Singleton(FTP = "File Transfer protocol")
print(y)