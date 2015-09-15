from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse

from .models import Poll, Choice

def index(request):
  latest_question_list = Poll.objects.order_by('-pub_date')[:5]
  template = loader.get_template("polls/index.html")
  context = RequestContext( request, {
    'latest_question_list':latest_question_list,
  })  
  return HttpResponse(template.render(context))

def detail(request, poll_id):
  question = get_object_or_404(Poll, pk=poll_id)
  return render(request, 'polls/detail.html', {'question':question})

def results(request, poll_id):
    question = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

# Create your views here.
