from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from mongoengine import connect


class IndexView(TemplateView):
    template_name = "d3/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['asd'] = "123"
        context['current_page'] = "d3-index"
        return context

# mongoclient = connect('kevin', host='192.168.8.170', port=27017)
# mongoclient = connect('kevin', host='mongodb://192.168.8.170:27017/kevin')
# testdb = mongoclient.get_database('test')
# person = {
#     'name': "John Doe",
#     'skills': ["Javascript", "CSS", "HTML"],
#     'work': None
# }

# from .models import Poll, Choice

# Poll(question="What is wrong with you?").save()
# poll = Poll.objects(question__contains="What").first()
# choice = Choice(choice_text="I'm at DjangoCon.fi", votes=23)
# poll.choices.append(choice)
# poll.save()


# for poll in Poll.objects(question__startswith="W"):
#     print len(poll.choices),
#     print poll.choices
