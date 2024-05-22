from django.shortcuts import render, redirect
from django.contrib import messages

# import todo form and models
from .models import Todo, task_done

###############################################


def index(request):

	task_done_list = task_done.objects.order_by("-date")
	item_list = Todo.objects.order_by("-date")
	if request.method == "POST":
			title = request.POST.get("title")
			details = request.POST.get("details")
			so = Todo(title=title, details=details)
			so.save()
			messages.info(request, "Task added !!!")
			return redirect('index')

	page = {
		"list": item_list,
		"title": "TODO LIST",
		"task_done_list": task_done_list
	}
	return render(request, 'index.html', page)

# if user clicks done than the item will be marked as done and moved to done model
def done(request, item_id):
	item = Todo.objects.get(id=item_id)
	donelist = task_done(title=item.title, details=item.details)
	donelist.save()
	item.delete()
	messages.info(request, "item marked as done !!!")
	return redirect('index')
	


### function to remove item, it receive todo item_id as primary key from url ##
def remove(request, item_id):
	item = Todo.objects.get(id=item_id)
	item.delete()
	messages.info(request, "item removed !!!")
	return redirect('index')

def remove_done(request, item_id):
	item = task_done.objects.get(id=item_id)
	item.delete()
	messages.info(request, "item removed !!!")
	return redirect('index')