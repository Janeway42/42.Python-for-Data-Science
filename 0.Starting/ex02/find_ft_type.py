def all_thing_is_obj(object: any) -> int:
    try:
        # only strings can be concatenated with other strings
        object + "" 
        print(f"{object} is in the kitchen : <class 'str'>")
    except:
        try:
            # only lists can use .append()
            object.append(None)
            print("List : <class 'list'>")
        except:
            try:
                # only sets cand use .add()
                object.add(None)
                print("Set : <class 'set'>")
            except:
                try:
                    # only dicts can use key assignment
                    object["key"] = "value"
                    print("Dict : <class 'dict'>")
                except:
                    try:
                        #tuples are indexable and concatenable
                        object[0]
                        object + object
                        print("Tuple: <class 'tuple'>")
                    except:
                        print("Type not found")
    return 42