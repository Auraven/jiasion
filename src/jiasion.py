class Serializable():   
    def __init__(self, json_object : dict = None, **kwargs):
        if json_object is not None: #Decode JSON into Class
            self.decode(json_object)
        for key, value in kwargs.items(): #Override Class Attributes with values
            self.__setattr__(key, value)
        for attr_name in self.__annotations__: #Ensure that Attributes exist, even if not set
            if attr_name not in self.__dict__:
                self.__setattr__(attr_name, None)

    def decode(self, json_object : dict):
        for attr_name , attr_type in self.__annotations__.items():
            attr = attr_type() #Instantiate default subclass Serializable
            self.__setattr__(attr_name, attr) #Create default attribute of name and type, even if not in the JSON            
            
            if issubclass(attr_type, Serializable): #Is Serializable
                attr.decode(json_object[attr_name])
            elif isinstance(attr, list) and issubclass(attr_type.__args__[0], Serializable): #Check if list of type Serializable
                serial_type = attr_type.__args__[0]
                serial_list = []
                for object_element in json_object[attr_name]:
                    serial_list.append(serial_type(object_element))
                self.__setattr__(attr_name, serial_list)
            else: #Basic Key Value
                self.__setattr__(attr_name, json_object[attr_name])           
   
    def encode(self) -> dict:
        json_object = {}
        for attr_name , attr_type in self.__annotations__.items():
            attr = self.__getattribute__(attr_name)
            if issubclass(attr_type, Serializable):
                json_object[attr_name] = attr.encode()
            elif isinstance(attr, list) and issubclass(attr_type.__args__[0], Serializable):
                serial_list = []
                for object_element in attr:
                    serial_list.append(object_element.encode())
                json_object[attr_name] = serial_list
            else:
                json_object[attr_name] = attr
        return json_object