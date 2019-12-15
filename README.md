# Magpie_CircleImportCheck
A tool to check circle-import in python project.(written in python)

## How to use it?

### 1.Create a workdir

    Create a dir named 'workdir' in the current dir of magpie.py.
  
    Copy ur target project into workdir

### 2.Run magpie.py with python2.7

    Linux required:we invoke system("reset") for screen clearing.
  
    Or change the source code by yourself. 

### 3.Handle with the 'homeless' case

    There are some cases which cannot be deal with by our tool, cus some moudules imported in some PYFILEs cannot be found in the workdir.
  
    Some are reasonable, others are due to the tool less than perfect, and we need to manually work with the latter case.
  
  ##### #1 Some are modules in LIB, which obviously cannot be found in the workdir.Just ignore it.
  
  ##### #2 Some are bad result.Like, there is a line that "#we need import it to make sure..." , and a result "it" will come out.Just ignore it.
  
  #### #3 Remaining are due to the tool less than perfect.Like, "from ..core.api import" or "import .graph".Solution: open the corresponding PYFILE to find out the true python-import-path of both the IMPORTED FILE and the IMPORTER FILE(like 'test.api.graph').
  
### 4.Get result

    You will get a result of import-relation showing as M->N.It contains two forms both in nodes index and import-path.
    You can further manually identify the circle.
    
### 5.Deficiency and prospect
    
    Ⅰ. Deficiency mention above(homeless problem).
    
    Ⅱ. A case like:
        #this is a project new.
        import a
        from b import x
    The tool cannot recognize the 'import' cus "#this is a project new." breaks the handling in current file.
    
    Ⅲ. A case like:
        #import a
        import b
    "a" will be recognized.We haven't deal with a comment.
    
    Ⅳ. We hope to auto-output circles in the future.(use DFS and so on)
    
    Ⅴ. We hope to auto-split the circle-import module one-time.
