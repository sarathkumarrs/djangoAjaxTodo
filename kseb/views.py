from django.shortcuts import render
from django.views.generic import View
from kseb.models import Task
from kseb.forms import TaskForm
from django.shortcuts import redirect
from django.http import JsonResponse
from django.forms.models import model_to_dict 

# Create your views here.
class TaskList(View):
    def get(self, request):
        form = TaskForm()
        tasks = Task.objects.all()
        return render(request,'index.html',{'form':form, 'tasks':tasks})
    def post(self,request):
        form = TaskForm(request.POST)

        if form.is_valid():
            new_task = form.save()
            return JsonResponse({'task':model_to_dict(new_task)}, status=200)

        else:
            return redirect('task_list_url')

class TaskCompleate(View):
    def post(self, request,id):
        task = Task.objects.get(id=id)
        task.compleated = True
        task.save()
        return JsonResponse({'task':model_to_dict(task)},status=200)


class TaskDelete(View):
    def post(self,request,id):
        task = Task.objects.get(id=id)
        task.delete()
        return JsonResponse({'result':'ok'}, status=200)