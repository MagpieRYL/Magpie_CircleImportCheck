import os

def graph_init(dnf, dfn, dnf_ , n):
    homeless = []
    homeless_flag = 1
    graph_im=[None]*n
    for i in range(n):
        graph_im[i]=[0]*n
    
    for i in range(n):
        file = dnf_[i]
        f = open(file , 'r')
        print("=================start==================")
        print(file)
        while 1:
            strl = f.readline()
            #print("###" + str(len(strl)))
            #if len(strl) == 2:
                #print(hex(ord(strl[0])))
                #print(hex(ord(strl[1])))
            str_import = strl.find("import")
            str_from   = strl.find("from")
            
            if len(strl) == 0:
                print("+++++++++++++++++end++++++++++++++++++")
                print("  ")
                print("  ")
                print("  ")
                break
            if str_import == -1 and str_from == -1 and ord(strl[0]) != 0x0d and ord(strl[1]) != 0x0a:
                #print(hex(ord(strl[0])))
                #print(hex(ord(strl[1])))
                print("+++++++++++++++++end++++++++++++++++++")
                print("  ")
                print("  ")
                print("  ")
                break
            
            if str_from   != -1:
                str_import = -1
                newstr    = strl[str_from+5:]
                space_pos = newstr.find(" ")
                #print(space_pos)
                if space_pos != -1:
                    finstr    = newstr[0:space_pos]
                else:
                    finstr    = newstr[:-2]
                print(finstr) 
                try:
                    idx = dfn[finstr]
                    homeless_flag = 0
                    print(idx)
                    graph_im[idx][i] = 1
                except:
                    (dirpath , filename) = os.path.split(file)
                    _dirpath = dirpath[8:] #  like : HexRaysPyTools/callbacks
                    path_rplc = _dirpath.replace("/",".") # like : HexRaysPyTools.callbacks
                    #now finstr is like : actions (or dir.module)
                    py_path  = path_rplc + "." + finstr # like : HexRaysPyTools.callbacks.actions
                    try:
                        idx = dfn[py_path]
                        homeless_flag = 0
                        print(idx)
                        graph_im[idx][i] = 1
                    except:
                        pass
                    
                    
                    #now we hope to handle with a dir_moudule like : HexRaysPyTools.callbacks
                    init_py_path = "workdir/" + finstr.replace("." , "/") + "/__init__.py"  # like : workdir/HexRaysPyTools/callbacks/__init__.py
                    init_py_dir  = "workdir/" + finstr.replace("." , "/")
                    try:
                        f_init_py = open(init_py_path , 'r')
                        print("__init__.py opened")
                        while 1:
                            strl_i = f_init_py.readline()
                            str_import_i = strl_i.find("import")
                            str_from_i   = strl_i.find("from")
            
                            if str_import_i == -1 and str_from_i == -1 and ord(strl_i[0]) != 0x0d and ord(strl_i[1]) != 0x0a:
                                break
            
                            if str_from_i   != -1:
                                str_import_i = -1
                                newstr_i    = strl_i[str_from_i+5:]
                                space_pos_i = newstr_i.find(" ")
                                if space_pos_i != -1:
                                    finstr_i    = newstr_i[0:space_pos_i]
                                else:
                                    finstr_i    = newstr_i[:-2]
                                print(finstr_i) 
                                try:
                                    idx = dfn[finstr_i]
                                    homeless_flag = 0
                                    print(idx)
                                    graph_im[idx][i] = 1
                                except:
                                    (dirpath_i , filename_i) = os.path.split(init_py_path)
                                    _dirpath_i = dirpath_i[8:] #  like : HexRaysPyTools/callbacks
                                    path_rplc_i = _dirpath_i.replace("/",".") # like : HexRaysPyTools.callbacks
                                    #now finstr_i is like : actions (or dir.module)
                                    py_path  = path_rplc_i + "." + finstr_i # like : HexRaysPyTools.callbacks.actions
                                    try:
                                        idx = dfn[py_path]
                                        homeless_flag = 0
                                        print(idx)
                                        graph_im[idx][i] = 1
                                    except:
                                        pass
                                    pass
                                if homeless_flag == 1:
                                    homeless.append(finstr + "###" +  init_py_path)
                                else:
                                    homeless_flag = 1
                            
                            if str_import_i != -1:
                                newstr_i    = strl_i[str_import_i+7:]
                                space_pos_i = newstr_i.find(" ")
                                if space_pos_i != -1:
                                    finstr_i    = newstr_i[0:space_pos_i]
                                else:
                                    finstr_i    = newstr_i[:-2]
                                print(finstr_i) 
                                try:
                                    idx = dfn[finstr_i]
                                    homeless_flag = 0
                                    print(idx)
                                    graph_im[idx][i] = 1
                                except:
                                    (dirpath_i , filename_i) = os.path.split(init_py_path)
                                    _dirpath_i = dirpath_i[8:] #  like : HexRaysPyTools/callbacks
                                    path_rplc_i = _dirpath_i.replace("/",".") # like : HexRaysPyTools.callbacks
                                    #now finstr_i is like : actions (or dir.module)
                                    py_path  = path_rplc_i + "." + finstr_i # like : HexRaysPyTools.callbacks.actions
                                    try:
                                        idx = dfn[py_path]
                                        homeless_flag = 0
                                        print(idx)
                                        graph_im[idx][i] = 1
                                    except:
                                        pass
                                    pass
                    
                                if homeless_flag == 1:
                                    homeless.append(finstr + "###" +  init_py_path)
                                else:
                                    homeless_flag = 1
                    
                    except:
                        pass
                    pass
                
                if homeless_flag == 1:
                    homeless.append(finstr + "###" +  file)
                else:
                    homeless_flag = 1
            
            if str_import != -1:
                newstr    = strl[str_import+7:]
                space_pos = newstr.find(" ")
                #print(space_pos)
                if space_pos != -1:
                    finstr    = newstr[0:space_pos]
                else:
                    if ord((newstr[-2:])[0]) == 0x0d and ord((newstr[-2:])[1]) == 0x0a:
                        finstr = newstr[:-2]
                    else:
                        finstr = newstr
                print(finstr) 
                try:
                    idx = dfn[finstr]
                    homeless_flag = 0
                    print(idx)
                    graph_im[idx][i] = 1
                except:
                    (dirpath , filename) = os.path.split(file)
                    _dirpath = dirpath[8:] #  like : HexRaysPyTools/callbacks
                    path_rplc = _dirpath.replace("/",".") # like : HexRaysPyTools.callbacks
                    #now finstr is like : actions (or dir.module)
                    py_path  = path_rplc + "." + finstr # like : HexRaysPyTools.callbacks.actions
                    try:
                        idx = dfn[py_path]
                        homeless_flag = 0
                        print(idx)
                        graph_im[idx][i] = 1
                    except:
                        pass
                        
                    #now we hope to handle with a dir_moudule like : HexRaysPyTools.callbacks
                    init_py_path = "workdir/" + finstr.replace("." , "/") + "/__init__.py"  # like : workdir/HexRaysPyTools/callbacks/__init__.py
                    init_py_dir  = "workdir/" + finstr.replace("." , "/")
                    try:
                        f_init_py = open(init_py_path , 'r')
                        print("__init__.py opened")
                        while 1:
                            strl_i = f_init_py.readline()
                            str_import_i = strl_i.find("import")
                            str_from_i   = strl_i.find("from")
            
                            if str_import_i == -1 and str_from_i == -1 and ord(strl_i[0]) != 0x0d and ord(strl_i[1]) != 0x0a:
                                break
            
                            if str_from_i   != -1:
                                str_import_i = -1
                                newstr_i    = strl_i[str_from_i+5:]
                                space_pos_i = newstr_i.find(" ")
                                if space_pos_i != -1:
                                    finstr_i    = newstr_i[0:space_pos_i]
                                else:
                                    finstr_i    = newstr_i[:-2]
                                print(finstr_i) 
                                try:
                                    idx = dfn[finstr_i]
                                    homeless_flag = 0
                                    print(idx)
                                    graph_im[idx][i] = 1
                                except:
                                    (dirpath_i , filename_i) = os.path.split(init_py_path)
                                    _dirpath_i = dirpath_i[8:] #  like : HexRaysPyTools/callbacks
                                    path_rplc_i = _dirpath_i.replace("/",".") # like : HexRaysPyTools.callbacks
                                    #now finstr_i is like : actions (or dir.module)
                                    py_path  = path_rplc_i + "." + finstr_i # like : HexRaysPyTools.callbacks.actions
                                    try:
                                        idx = dfn[py_path]
                                        homeless_flag = 0
                                        print(idx)
                                        graph_im[idx][i] = 1
                                    except:
                                        pass
                                    pass
                                if homeless_flag == 1:
                                    homeless.append(finstr + "###" +  init_py_path)
                                else:
                                    homeless_flag = 1
                            
                            if str_import_i != -1:
                                newstr_i    = strl_i[str_import_i+7:]
                                space_pos_i = newstr_i.find(" ")
                                if space_pos_i != -1:
                                    finstr_i    = newstr_i[0:space_pos_i]
                                else:
                                    finstr_i    = newstr_i[:-2]
                                print(finstr_i) 
                                try:
                                    idx = dfn[finstr_i]
                                    homeless_flag = 0
                                    print(idx)
                                    graph_im[idx][i] = 1
                                except:
                                    (dirpath_i , filename_i) = os.path.split(init_py_path)
                                    _dirpath_i = dirpath_i[8:] #  like : HexRaysPyTools/callbacks
                                    path_rplc_i = _dirpath_i.replace("/",".") # like : HexRaysPyTools.callbacks
                                    #now finstr_i is like : actions (or dir.module)
                                    py_path  = path_rplc_i + "." + finstr_i # like : HexRaysPyTools.callbacks.actions
                                    try:
                                        idx = dfn[py_path]
                                        homeless_flag = 0
                                        print(idx)
                                        graph_im[idx][i] = 1
                                    except:
                                        pass
                                    pass
                                if homeless_flag == 1:
                                    homeless.append(finstr + "###" +  init_py_path)
                                else:
                                    homeless_flag = 1
                                
                    except:
                        pass                        
                        
                    pass
                    
                if homeless_flag == 1:
                    homeless.append(finstr + "###" +  file)
                else:
                    homeless_flag = 1
                    
        f.close()    
     
    #print(homeless)
    _homeless = list(set(homeless))
    _homeless.sort()
    print("=====================homeless import=====================")
    for i in _homeless:
        print(i)
    return graph_im


def manu_add_import(dfn):
    idx_import   = raw_input("python path of import:")
    idx_imported = raw_input("python path of imported:")
    pred = dfn[idx_imported]
    next = dfn[idx_import]
    return (pred , next)


def circle_preprocessor(graph_im , n):
    nodes = []
    flag  = 1
    is_clear = 1
    
    for i in range(n):
        nodes.append(i)
    
    
    while 1:
        is_clear = 1
        _nodes = nodes[:]
        for i in nodes:
            for j in nodes:
                if graph_im[j][i] == 1:
                    flag = 0
                    break
            if flag:
                is_clear = 0
                for j in nodes:
                    graph_im[i][j] = 0
                nodes.remove(i)
            flag = 1
        if is_clear == 1:
           break
    
    while 1:
        is_clear = 1
        _nodes = nodes[:]
        for i in nodes:
            for j in nodes:
                if graph_im[i][j] == 1:
                    flag = 0
                    break
            if flag:
                is_clear = 0
                for j in nodes:
                    graph_im[j][i] = 0
                nodes.remove(i)
            flag = 1
        if is_clear == 1:
            break

def DFS_circle_search(graph_im , nodes):

    
    #for i in nodes:
        
    pass
    
    