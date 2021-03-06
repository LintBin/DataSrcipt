#!/usr/bin/env python3
import os,os.path  
import string,base64
import string
def main():
    tableName=input("请输入数据表名:")
    typeDir={}
    typeDir=check(typeDir)
    f=open("inserData.sql",'w')
    #tableName="tablename"
    #typeDir={'stringDir': {'color': {'type': 'string', 'setNum': 'color', 'addself': '2'}, 'docu': {'type': 'string', 'beginNum': '20', 'addself': '1'}}, 'intDir': {'flag': {'type': 'int', 'setNum': 0, 'addself': '2'}, 'myid': {'type': 'int', 'beginNum': '1000', 'addself': '1'}}}
    sqlAmount=int(input("需要生成多少条sql语句？"))
    i=0
    while i<sqlAmount:
        sql=createSQL(tableName,typeDir,str(i))
        f.write(sql+"\n")
        print(str(i))
        print(sql)
        i=i+1
    f.close()
    print(typeDir)


#递归，检查是否需要输入字段
def check(typeDir):
    flag=input("是否还有列要输入，是则输入'y'，没有则输入'n':")
    if flag=="y":
        print("1--int型")
        print("2---字符型(包括char和carchar)")
        print("3---data型")
        columnType=input("选择所需要添加字段的类型:")
        columnNum=input("此字段需要多少个？:")
        columnDir={}
        if columnType=="1":
            #多次输入需要的字段名,每一个字段配一个字典
            i=0
            while i<int(columnNum):
                i=i+1
                columnNmae=input("请输入字段名:")
                #inpitColumn是字段名，而intDeal返回的是其相对应的字典
                columnDir[columnNmae]=intDeal()
            typeDir["intDir"]=columnDir
            check(typeDir)
            return typeDir
        if columnType=="2":
            i=0
            while i<int(columnNum):
                i=i+1
                columnNmae=input("请输入字段名:")
                columnDir[columnNmae]=stringDeal()
            typeDir["stringDir"]=columnDir
            check(typeDir)
            return typeDir
    if flag=="n":
        return typeDir
    else:
        return typeDir
    
def createSQL(tableName,typeDir,numStr):
    sql="insert into "+tableName+"("
    typeNameDir=typeDir.keys()
    typeNameList=list(typeNameDir)
    i=0
    num=len(typeNameList)
    columnAll=[]
    while i<num:
        partColumn=list(typeDir[typeNameList[i]].keys())
        for part in partColumn:
            columnAll.append(part)
        i=i+1
    #columnName=typeDir[typeNameList[0]]
    print(columnAll)
    for element in columnAll:
        sql=sql+element+","
    sql=sql[:-1]
    #到此得到<<insert into tablename(column1,column2,```) values('>>
    sql=sql+")"+"values('"
    #partTypeDir就是columnDir
    for partTypeDir in typeDir:
        typeDir[partTypeDir]
        for columnName in typeDir[partTypeDir]:
            columnValue=valuesDeal(typeDir[partTypeDir][columnName],int(numStr),columnName)
            sql=sql+str(columnValue)+"','"
            
    sql=sql[:-2]+");"
    return sql

#列为int型时的处理
def intDeal():
    print("1--自增")
    print("2--设置固定值")
    detailDir={}
    detailDir["type"]="int"
    addself=input("是否自增：")
    if addself=="1":
        beginNumStr=input("自增开始数值:")
        beginNumInt=int(beginNumStr)
        detailDir["addself"]="1"
        detailDir["beginNum"]=beginNumStr
        return detailDir
        
    if addself=="2":
        setNumStr=input("数值固定为:")
        setNumInt=int(setNumStr)
        detailDir["addself"]="2"
        detailDir["setNum"]=setNumInt
        return detailDir

#列为string型时的处理
def stringDeal():
    print("1--字段名加自增的数字")
    print("2--设置固定值")
    detailDir={}
    detailDir["type"]="string"
    addself=input("是否固定")
    if addself=="1":
        beginNumStr=input("自增开始数值:")
        detailDir["addself"]="1"
        detailDir["beginNum"]=beginNumStr
        return detailDir
    if addself=="2":
        setNumStr=input("数值固定为:")
        detailDir["addself"]="2"
        detailDir["setNum"]=setNumStr
        return detailDir

#处理values的值
def valuesDeal(columnType,num,columnName):
    if columnType["type"]=="int":
        if columnType["addself"]=="1":
            returnNum=int(columnType["beginNum"])+num
            returnNumStr=str(returnNum)
            return returnNum
        if columnType["addself"]=="2":
            return columnType["setNum"]
        return ""
    if columnType["type"]=="string":
        if columnType["addself"]=="1":
            returnNum=int(columnType["beginNum"])+num
            return columnName+str(returnNum)
        if columnType["addself"]=="2":
            return columnType["setNum"]

    
if __name__=='__main__':
    main()
