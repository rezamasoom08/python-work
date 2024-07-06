class Korean:
    def __init__(self):
        self.name = "Korean"
    
    def speak_korean(self):
        return "An-neyon?"

class British:

    def __init__(self):
        self.name = "British"
    
    def speak_english(self):
        return "Hello"

class Adapter:

    def __init__(self, object, **adapter_method):
        self._object = object

        self.__dict__.update(adapter_method)
    
    def __getattr__(self, attr):
        return getattr(self._object, attr)

object = []

korean = Korean()

british = British()

object.append(Adapter(korean, speak=korean.speak_korean))
object.append(Adapter(british, speak=british.speak_english))

for obj in object:
    print("{} says '{}'\n".format(obj.name, obj.speak()))