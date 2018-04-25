from django.http import JsonResponse

import json
import makEasy
import jsonpickle

me_folder=u'/home/worksite/PyApp/makEasy/'
prj_folder=me_folder+'Projects/'


def new(request):
    if (request.method == "POST" and request.POST['prj_name']):
        prj_name=request.POST['prj_name']
        prj=makEasy.projectLibrary[prj_name]
        prj_path=prj.Path

        # load form structure
        f = open(prj_folder+prj_path+'/form.json', 'r')
        data=json.load(f)
        f.close()

        # load js functions
        f = open(prj_folder+prj_path+'/project.js', 'r')
        prj_script=f.read()
        f.close()

        # load project default data
        f = open(prj_folder+prj_path+'/data.json', 'r')
        prj_data=json.load(f)
        f.close()

        data = dict(prj_name=prj_name,
                    form_data=data["form_data"],
                    prj_script=prj_script,
                    prj_data=prj_data,
                    prj_title=prj.Title)

        return JsonResponse(data)


def getJson(request):
    path=me_folder+request.POST['jsonPath']
    source={}
    #load json structure
    f = open(path, 'r')
    source=f.read()
    f.close()
    data= dict(source=source,path=path)
    #data=dict(msg='Chiamata eseguita',source={})
    return  JsonResponse(data)


def createItem(request):
    meItem='{}'
    if request.POST['name']:
        prj_data=json.loads(request.POST['jsonstring'])
        item=makEasy.newItemFromProject(request.POST['name'],prj_data)
        meItem=jsonpickle.encode(item)
    return JsonResponse(dict(meItem=meItem))


def exportDXF(request):
    dxf=''
    if request.POST['name']:
        data=json.loads(request.POST['jsonstring'])
        item=makEasy.newItemFromProject(request.POST['name'],data['data_form'])
        wf=item.WorkFlow
        for ws in wf:
            if ws.Work.Class=='PlasmaCut':
                dxf=ws.getDXF()
    return JsonResponse(dict(dxf=[dxf]))

