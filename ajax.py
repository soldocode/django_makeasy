from django.http import JsonResponse

def new(request):
    if request.method == "POST":
        data = {"message": "Funziona"}
        return JsonResponse(data)