
class Dict(dict):
    __setattr__ = dict.__setitem__
    __getattr__ = dict.__getitem__


def complex_dict_to_object(Obj):
    '''把一个字典转换为一个对象，如果列表里包含字典会继续拆分'''

    if not (isinstance(Obj, dict) or isinstance(Obj, list)):
        return Obj
    inst = Dict()
    if isinstance(Obj, dict):
        for k, v in Obj.items():
            inst[k] = complex_dict_to_object(v)
        return inst
    if isinstance(Obj, list):
        obj_list = []
        for x in Obj:
            obj_list.append(complex_dict_to_object(x))
            # x = complex_dict_to_object(x)
        return obj_list
