def NULL_not_found(object: any) -> int:
    try:
        if object is None:
            print(f"Nothing: {object} <class 'NoneType'>")
            return 0
        
        if object is False:
            print(f"Fake: {object} <class 'bool'>")
            return 0
        
        if object == "":
            print(f"Empty: {object} <class 'str'>")
            return 0
        
        if object == 0:
            try:
                remainder = object % 2
                if remainder == 0:
                    print(f"Zero: {object} <class 'int'>")
                    return 0
            except:
                pass 
        
        if object != object:
            # NaN is float specific and the only value in python that is not equal to itself
            print(f"Cheese: {object} <class 'float>")
            return 0

        print("Type not found")
        return 0
    except:
        return 1