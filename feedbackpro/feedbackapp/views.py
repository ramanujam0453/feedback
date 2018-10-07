from django.shortcuts import render
from .models import EmpFeedBack
from .forms import EmpFeedBackForm
from .serializer import EmpFeedBackSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


# creating APIView for serialization of table data to jason format
class FeedbackView(APIView):
    def get(self, request):
        fb = EmpFeedBack.objects.all()
        serializer = EmpFeedBackSerializer(fb, many=True)
        return Response(serializer.data)


# view to store data in the database
def feedback_view(request):
    form = EmpFeedBackForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        eid = form.cleaned_data.get('eid')
        fbeid = form.cleaned_data.get('fbeid')
        rating = form.cleaned_data.get('rating')
        feedback = form.cleaned_data.get('feedback')
        fb_user = EmpFeedBack.objects.create(eid=eid, fbeid=fbeid, rating=rating, feedback=feedback)
        print(fb_user)
        return render(request, 'thanks.html')
    return render(request, 'feedback.html', {'form': form})
