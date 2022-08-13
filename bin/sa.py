import re,sys,os

def openreadtabs(file):
    _path_,__tmp=os.path.split(file)
    path=_path_[:-6]
    #print(path)
    if not os.path.isdir(path+"httabs\\"):
        os.system("mkdir "+path+"httabs\\")
    __tmp=(__tmp.split('.'))[0]
    ##print(path+"httabs\\"+__tmp+".html")
    
    ## Html source code
    try:
        with open("./source.html","r") as _f:
            _code = _f.read()    
    except:
        _code = """---
layout: false
--- 
<!--
%s
-->
<meta charset="UTF-8">
<html>
    <head>
        <script>
            var qyu=document.getElementsByName("www");
            var sh=%s;
            function switchargs(args){
                for(var i=0;i<qyu.length;i++){
                    qyu[i].className="not";
                }document.getElementById(args).className="enabled";
                document.getElementById("text").innerText=sh[args-1];
            }
        </script>
    </head>
    <body>
        <table class="_tabs">
            <tr>
                %s
            </tr>
        </table>
        <style>
            .textarea p{
                border: 2px;
                border-style: groove;
                border-color: #444444;
                font-size: 18px; 
                padding: 7px;
                padding-top: 6px;
                margin: 0px;
            }
            table._tabs{
                display : table;
                border-collapse :separate;
                border-spacing: 2px; 
                border-color: grey;
                border-collapse : separate;
            }
            table tr td button{
                padding: 8px;
                font-size: 20px;
                border-top: 0px;
                border-left: 0px;
                border-right: 0px;
                border-color: #617eff;
            }
            table tr td button.enabled{
                background-color: rgb(192, 192, 192);
                color: #2242d0;
            }
            table tr td button.not{
                border-bottom: 0px;
            }
        </style>
        <div class="textarea">
        <p id="text">
            Click a tab button to view
        </p>
        </div>
    </body>
</html>

        """
    try:
        with open(file,"r") as f:
            _file_getch = f.read()
    except:
        #print("plugin-tabs: File not found")
        return 0
    if "<!--tabencoded-->" in _file_getch:
        #print("plugin-tabs: Already encoded! please delete the <!--tabencoded--> to regenerate")
        return 0
    m = _file_getch.split('\n')
    
    fgetch = _file_getch.split("\n")
    startre = re.compile("!!! \w+")
    titlere = re.compile("\+\+\+\+\w+")
    std = -1
    edd = -1
    solutions = []
    tmp = -1
    ttitle = ""
    
    if fgetch[-1] == '':
        fgetch.pop()
    for i in range(len(fgetch)):
        if startre.match(fgetch[i]):
            std = i
        elif fgetch[i] == "++++":
            edd = i
    if (std == -1 or edd == -1):
        ##print("plugin-tabs: No tabs found")
        return 0
    fgetch = fgetch[std+1:edd]
    for i in fgetch:
        if titlere.match(i):
            if (tmp != -1):
                solutions[tmp][1] = solutions[tmp][1][:-1]
            ttitle = i[4:]
            tmp += 1
            solutions.append([])
            solutions[tmp].append(ttitle)
            solutions[tmp].append("")
            continue
        solutions[tmp][1] += (i+'\n')
    solutions[-1][1] = solutions[-1][1][:-1]
    
    
    btnformat = """<td><button onclick = 'switchargs("{}")' class = "disabled" id = "{}" name = "www">{}</button></td>"""
    tabformat = """<style>
    iframe{
        height: auto;
        width: auto;
    }
</style>
<iframe src="%s"></iframe>\n"""
    btns = """"""
    io = []
    for i in range(len(solutions)):
        btns += (btnformat.format(i+1,i+1,solutions[i][0]))
        io.append(solutions[i][1])
    
    
    code = _code%(_file_getch,str(io),btns)
    ###print(code)
    m = m[:std]+(tabformat%("\\httabs\\"+__tmp+".html")).split('\n')+m[edd+1:]+["\n"]+"<!--tabencoded-->".split("\n")
    r = ''
    for i in range(len(m)):
        r += m[i]
        r += '\n'
    with open(file,"w") as f:
        f.write(r)
    with open(path+"httabs\\"+__tmp+".html","w") as f:
        f.write(code)    
    #print("plugin-tabs: Encode success")
qre = sys.argv
if len(qre) == 1:
    print("plugin-tabs: No args supplied")
else:
    openreadtabs(qre[1])


