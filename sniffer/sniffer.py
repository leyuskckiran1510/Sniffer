import os
import re
import optparse
import re

def dry(i,**dic):
    mk=dic.keys()
    try:
        for j in os.listdir(i):
            a=(i+f"/{j}")
            if ("." in a) and ("text" in mk or "re" in mk) :
                try:
                    with open(f"{i}/{j}","r") as fl:
                        data=fl.read()
                    if dic["text"] in data:
                        print((i+f"/{j}").replace("/","\\"))
                    if "re" in mk:
                        if re.findall(dic["re"],data):
                            print(a.replace("/","\\"))
                except :
                    pass
            if "ls" in mk:
                print(a.replace("/","\\"))
            if ("ext" in mk) and (a.split('.')[-1] in dic["ext"]):
                print(a.replace("/","\\"))
            n_dic=[f"{i}='{dic[i]}'," for i in dic.keys()]
            #print('dry(i+f"/{j}",'+''.join(n_dic)+")")
            eval('dry(i+f"/{j}",'+''.join(n_dic)+")")#,n_dic)
            
                
    except Exception as e:
        #print(e)
        pass
    
def main(data):
    lis=['ext','text','re','ls']
    caller=''
    for i in lis:
        a=eval(f'data.{i}')
        if a:
            caller+=","+f"{i}='{a}'"
    caller=caller+")"
    if data.dir:
        try:
            di=f"{data.dir}"
            eval(f"dry('{di}'{caller}")
        except Exception as e:
            print("Error :- \n\t",e)
    else:
        di=f"./"
        eval(f"dry('{di}'{caller}")
        


if __name__=="__main__":
    parser=optparse.OptionParser()
    parser.add_option('-p','--path',dest='dir',help='-p X:/foldewr1/folder2   or  --path X:/root      "if left blank it will start from the current dir" ')
    parser.add_option('-e','--extension',dest='ext',help='-e .mp4,.jpg')
    parser.add_option('-t','--text',dest='text',help='-t "hello"  or   --text "import"\n\t used for searching the provided text inside the files in the given dir files and return path to it')
    parser.add_option('-r','--regex',dest='re',help='-r "[a-zA-Z]{5}[\-\+][0-9]{2}" For using pattren for regex search')
    parser.add_option('-l','--ls',dest='ls',help='-ls  "Will list all the subdir and dir from the given path "')
    parser.add_option('-g','--example',dest='ex',help='-e  "will give some sample examples "')
    option,args=parser.parse_args()
    if option.ex:
        print("Examples")
    else:
        main(option)












    
