
from googletrans import Translator
from . import globals
import json
from django.shortcuts import render,redirect
from django.http import HttpResponse
urls = globals.urlSideMapList()

class TranslatorFun:
    def Translate(self,text,dest,src='en'):
        trans=Translator()
        lang=trans.detect(text)
        t=trans.translate(text,dest=dest,src=src)
        return t
    
    def EnglishToOther(self,request,indi_id,dest,htmlFile):
        link_string1,link_string2=ArrangeSideMapForWebpage.arrange(self,indi_id,3,'AT')
        if request.method=="POST":
            text=request.POST.get('text','default')
            t = self.Translate(text,dest)
            alt=True
            param={"ortext":text,"text":t.text,"alt":alt,'link_string1':link_string1,'link_string2':link_string2}
            resp = render(request,htmlFile,param)
            return resp
        param={'link_string1':link_string1,'link_string2':link_string2}
        resp = render(request,htmlFile,param)
        return resp
    
    def HindiToOther(self,request,indi_id,dest,src,htmlFile):
        link_string1,link_string2=ArrangeSideMapForWebpage.arrange(self,indi_id,3,'AT')
        if request.method == "POST":
            text = request.POST['text']
            if text =="":
                res=json.dumps({'ConTex': ""},default=str)
            else:
                t = self.Translate(text,dest,src=src)
                res=json.dumps({'ConTex': t.text},default=str)
            resp=HttpResponse(res) 
            return resp 
        param={'link_string1':link_string1,'link_string2':link_string2}
        resp=render(request,htmlFile,param)
        return resp


class ArrangeSideMapForWebpage:
  

    def arrange(self,indi_id,grp_id,same_grps_id):
        links_strings_1=[]
        links_strings_2=[]
        for link in range(len(urls)):

            if urls[link][3] == same_grps_id:
                if urls[link][2] == grp_id:
                    if urls[link][4]!= indi_id:
                        links_strings_1.append([urls[link][0],urls[link][1]])
                    pass
                else:
                    links_strings_2.append([urls[link][0],urls[link][1]])
        return links_strings_1,links_strings_2




