import copy

class Serializable():
    def __init__(self, json_object : dict):
        self.decode(json_object)   

    def decode(self, json_object : dict):
        for attr_name in json_object:
            attr = self.__getattribute__(attr_name)
            if issubclass(type(attr), Serializable):
                attr.decode(json_object[attr_name])
            elif issubclass(type(attr), list) and len(attr) == 1 and issubclass(type(attr[0]), Serializable):
                attr_list = []
                for sub_object in json_object[attr_name]:
                    attr_copy = copy.deepcopy(attr[0])
                    attr_copy.decode(sub_object)
                    attr_list.append(attr_copy)
                self.__setattr__(attr_name, attr_list)
            else:
                self.__setattr__(attr_name, json_object[attr_name])
   
    def encode(self) -> dict:
        json_object = {}
        for attr_name in self.__dict__:
            attr = self.__getattribute__(attr_name)
            if issubclass(type(attr), Serializable):
                json_object[attr_name] = attr.encode()
            elif issubclass(type(attr), list) and len(attr) > 0 and issubclass(type(attr[0]), Serializable):
                attr_list = []
                for sub_object in attr:
                    attr_list.append(sub_object.encode())
                json_object[attr_name] = attr_list
            else:
                json_object[attr_name] = attr
        return json_object