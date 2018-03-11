from django.http import JsonResponse

import json
import makEasy

prj_folder=u'/home/worksite/PyApp/makEasy/Projects/'

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