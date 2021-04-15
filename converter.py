#!/usr/bin/env python3

import re
import sys
import argparse
import os

parser = argparse.ArgumentParser(description='Convert individual org files or directory to Obsidian.md format')
parser.add_argument('PATH', help='path to the file or directory')
parser.add_argument('-d', '--directory', help='convert all the org-files in a specific directory instead of a single file', required=False, default=[], action= 'store_true')
parser.add_argument('-o', '--output_directory', help='directory where to place the new file(s), defaults to same directory as the file', required=False, default=[], action='store')
parser.add_argument('-r', '--recursive', help='recursively convert all files in a directory, requires -d', required=False, default=[], action='store_true')
parser.add_argument('-w', '--wiki', help='Convert org links to [[wiki]] links, otherwise converts them to []() markdown links', action='store_true')


def read_file(path):
    with open(path, "r") as f:
        oldlines = f.readlines()
    return oldlines 

        
def convert_link(line):
    if(re.findall(r"\[\[file:([^\]]+)\]\[[^\]]+\]\]", line)):
        print("ha")
        line=re.sub("\.org", ".md", line)
        line=re.sub(r"\[\[file:([^\]]+)\]\[[^\]]+\]\]", r"[[\1]]", line)
    return line

def convert_math(line):
    if(line[0]=="\\"):
        if(line[1]=="]" or line[1]=="["):
            line[:1]="$$"
        elif(line[1]=="(" or line[1]==")"):
            line[:1]="$"
        elif(line[1]=="b"):
            line="$$"+line
        elif(line[1]=="e"):
            line=line+"$$"
    return line

def convert_file(lines):
    newlines=[]
    for i, line in enumerate(lines):
        if(line[0]=="#"):
            if(line[2:12]=="roam_tags:"):
                tags=re.findall(r"\s[^\s]+\s", line)
                line=""
                for tag in tags:
                    line+="#"+tag[1:-1]+" "
                line+="\n"
            else:
                line=""
        elif(line[0]=="*"):
            line= re.sub("\*", "#", line)
        elif(line[0]=="\\"):
            if(line[1]=="]" or line[1]=="["):
                line=re.sub(r"\\[\[\]]", "$$", line)
            elif(line[1]=="(" or line[1]==")"):
                line=re.sub(r"\\[\(\)]", "$", line)
            elif(line[1]=="b"):
                line="$$\n"+line
            elif(line[1]=="e"):
                line=line+"$$"
        line=convert_link(line)
        newlines.append(line)
    return newlines

def writefile(path, lines, output):
    if(output):
        if(os.path.isdir(output)!=True):
            os.mkdir(output)
        filename=re.findall(r"[^/]+\.org", path)[0]
        with open(output + "/" + filename[:-3] + "md", "w") as f:
            f.writelines(lines)
    else:
         with open(path[:-3] + "md", "w") as f:
            f.writelines(lines)


            
def shebang(path, output):
    org=read_file(path)
    new = convert_file(org)
    writefile(path, new, output)

def main():    
    argument = parser.parse_args()
    path=argument.PATH
    output=argument.output_directory
    if(argument.directory):
        if(argument.recursive):
            for root, dirs, files in os.walk(path):
                for file in files:
                    if file.endswith(".org"):
                        shebang(path +"/"+file, output)
        else:
            for file in os.listdir(path):
                if file.endswith(".org"):
                    shebang(path+"/"+file, output)
    else:
        shebang(path, output)
main()
    
