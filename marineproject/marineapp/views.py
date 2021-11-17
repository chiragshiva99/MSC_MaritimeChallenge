from django.shortcuts import render, redirect
from django.http import response, FileResponse, HttpResponse
from django.views.generic import View, TemplateView, CreateView, FormView
from django.views.generic.edit import FormView
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
import io
from .forms import *
#from reportlab.pdfgen import canvas
from results.models import *

# from verify_email.email_handler import send_verification_email  #MIGHT HAVE ERROR
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import get_user_model
from django_email_verification import send_email


class SignUpView(CreateView):
    template_name = "signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy("marineapp:hrdashboard")

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")

        user = User.objects.create_user(username, email, password)
        form.instance.user = user

        login(self.request, user)

        return super().form_valid(form)


class LogInView(FormView):
    template_name = "login.html"
    form_class = LogInForm
    success_url = reverse_lazy("marineapp:maindashboard")

    def form_valid(self, form):
        uname = form.cleaned_data.get("username")
        pword = form.cleaned_data.get("password")
        usr = authenticate(username=uname, password=pword)

        # if form.is_valid():
        #     inactive_user = send_verification_email(request, form)
        #     inactive_user.cleaned_data['email']
        # Output : test-user123@gmail.com

        if usr is not None and usr.customer:
            login(self.request, usr)
        else:
            return render(self.request, self.template_name, {
                "form": self.form_class,
                "error": "Invalid Credentials"
            })

        return super().form_valid(form)


class LogOutView(View):
    def get(self, request):
        logout(request)
        return redirect("marineapp:login")


class MainDashboardView(TemplateView):
    template_name = "maindashboard.html"


class HRDashboardView(TemplateView):
    template_name = "hrdashboard.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['names_list'] = Customer.objects.all()
        context['scores_list'] = Result.objects.all()

        return context



class TraineeDashboardView(TemplateView):
    template_name = "traineedashboard.html"


class TrainerDashboardView(TemplateView):
    template_name = "trainerdashboard.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['lesson1_list'] = LessonMaterialModule1.objects.all()
        context['lesson2_list'] = LessonMaterialModule2.objects.all()
        context['lesson3_list'] = LessonMaterialModule3.objects.all()
        context['lesson4_list'] = LessonMaterialModule4.objects.all()
        context['lesson5_list'] = LessonMaterialModule5.objects.all()

        return context

class DeleteRowView(TemplateView):
    template_name = "trainerdashboard.html"

    def get(self,request,module,topic):
        module = int(module)
        if module == 1:
            record = LessonMaterialModule1.objects.filter(pk=topic)
        elif module == 2:
            record = LessonMaterialModule2.objects.filter(pk=topic)
        elif module == 3:
            record = LessonMaterialModule3.objects.filter(pk=topic)
        elif module == 4:
            record = LessonMaterialModule4.objects.filter(pk=topic)
        elif module == 5:
            record = LessonMaterialModule5.objects.filter(pk=topic)
        
        record.delete()
        return redirect("marineapp:trainerdashboard")
    
    # def delrec(request, id):
#     delrow = LessonMaterialModule1.objects.get(id=id)
#     delrow.delete()
#
#     context['lesson1_list'] = LessonMaterialModule1.objects.all()

# def delrec(request, id):
#     delrow = LessonMaterialModule1.objects.get(id=id)
#     delrow.delete()
#     context['lesson1_list'] = LessonMaterialModule1.objects.all()


# class Quiz1View(CreateView):
#     template_name = "quiz1.html"
#     form_class = Quiz1Form
#     success_url = reverse_lazy("marineapp:trainerdashboard")

#     def form_valid(self, form):
#         return super().form_valid(form)


# class Quiz1QuestionView(CreateView):
#     template_name = "quiz1question.html"
#     form_class = QuestionQuiz1Form
#     second_form_class = AnswerQuiz1Form
#     success_url = reverse_lazy("marineapp:trainerdashboard")

#     def form_valid(self, form):
#         return super().form_valid(form)

# class Quiz1AnswerView(CreateView):
#     template_name = "quiz1questionanswer.html"
#     form_class = AnswerQuiz1Form
#     success_url = reverse_lazy("marineapp:trainerdashboard")  ############

    def form_valid(self, form):
        return super().form_valid(form)


class MatchInstructionView(TemplateView):
    template_name = "matchinstruction.html"


class HangmanInstructionView(TemplateView):
    template_name = "hangmaninstruction.html"

class InsideShipView(TemplateView):
    template_name = "Inside_Ship.html"
    pass


class OutsideShipView(TemplateView):
    template_name = "Outside_Ship.html"
    pass


class VirtualTourView(TemplateView):
    template_name = "virtualtourmain.html"
    pass


class LessonMaterialModule1View(CreateView):
    template_name = "lessonmaterialmodule1.html"
    form_class = Module1LessonForm
    success_url = reverse_lazy('marineapp:trainerdashboard')

    def form_valid(self, form):

        return super().form_valid(form)

    def Upload_pdf(request):
        if request.method == "POST":
            t = request.FILES["lesson_module1"]
        return response(request, "lessonmaterialmodule1.html", t)


class Module1LessonView(TemplateView):
    template_name = "module1lesson.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['lesson1_list'] = LessonMaterialModule1.objects.all()

        return context


class LessonMaterialModule2View(CreateView):
    template_name = "lessonmaterialmodule2.html"
    form_class = Module2LessonForm
    success_url = reverse_lazy('marineapp:trainerdashboard')

    def form_valid(self, form):

        return super().form_valid(form)

    def Upload_pdf(request):
        if request.method == "POST":
            t = request.FILES["lesson_module2"]
        return response(request, "lessonmaterialmodule2.html", t)


class Module2LessonView(TemplateView):
    template_name = "module2lesson.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['lesson2_list'] = LessonMaterialModule2.objects.all()

        return context


class LessonMaterialModule3View(CreateView):
    template_name = "lessonmaterialmodule3.html"
    form_class = Module3LessonForm
    success_url = reverse_lazy('marineapp:trainerdashboard')

    def form_valid(self, form):

        return super().form_valid(form)

    def Upload_pdf(request):
        if request.method == "POST":
            t = request.FILES["lesson_module3"]
        return response(request, "lessonmaterialmodule3.html", t)


class Module3LessonView(TemplateView):
    template_name = "module3lesson.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['lesson3_list'] = LessonMaterialModule3.objects.all()

        return context



class LessonMaterialModule4View(CreateView):
    template_name = "lessonmaterialmodule4.html"
    form_class = Module4LessonForm
    success_url = reverse_lazy('marineapp:trainerdashboard')

    def form_valid(self, form):

        return super().form_valid(form)

    def Upload_pdf(request):
        if request.method == "POST":
            t = request.FILES["lesson_module4"]
        return response(request, "lessonmaterialmodule4.html", t)


class Module4LessonView(TemplateView):
    template_name = "module4lesson.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['lesson4_list'] = LessonMaterialModule4.objects.all()

        return context


class LessonMaterialModule5View(CreateView):
    template_name = "lessonmaterialmodule5.html"
    form_class = Module5LessonForm
    success_url = reverse_lazy('marineapp:trainerdashboard')

    def form_valid(self, form):

        return super().form_valid(form)

    def Upload_pdf(request):
        if request.method == "POST":
            t = request.FILES["lesson_module5"]
        return response(request, "lessonmaterialmodule5.html", t)


class Module5LessonView(TemplateView):
    template_name = "module5lesson.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['lesson5_list'] = LessonMaterialModule5.objects.all()

        return context


class MatchGameView(TemplateView):
    template_name = "matchgame.html"


class HangmanGameView(TemplateView):
    template_name = "hangmangame.html"


# class VerificationView(TemplateView):
#     #Template_name = "my_custom_email_message.html"
#     pass


# @csrf_exempt
def sendEmail(request):  #add 'form' if required
    # username = form.cleaned_data.get("username")
    username = request.POST.get('username')
    password = request.POST.get("password")
    email = request.POST.get("email")
    user = get_user_model().objects.create(username=username,
                                           password=password,
                                           email=email)
    user.is_active = False
    # sendConfirm(user)
    send_email(user)
    send_email(user, custom_salt=my_custom_key_salt)
    return render(request, 'confirm_template.html')


class MyClassView(FormView):
    def form_valid(self, form):
        user = form.save()
        returnVal = super(MyClassView, self).form_valid(form)
        send_email(user)
        return returnVal


class EngineRoomView(TemplateView):
    template_name = "engine_room.html"
