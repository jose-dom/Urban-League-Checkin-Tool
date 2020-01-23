from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from visitors.models import Visitor, Visit
from django.contrib import messages
import uuid

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'view/home.html', context)


@login_required
def analytics(request):
    context = {
        'results': Visit.objects.all(),
    }
    return render(request, 'view/analytics.html', context)

##2019 Data
@login_required
def reports(request):
    data = [
            "Job Placement Assistance",
            "Resume Preparation",
            "Mock Interviewing",
            "Construction",
            "Pre-Apprenticeship",
            "Microsoft Office Certification",
            "Public Income Benefits Screening",
            "Employment Services and Career Improvement",
            "Financial Workshop",
            "Financial Coaching",
            "Start Saving on a Shoestring",
            "Your Choices and Your Cha-CHING!!",
            "Early Career Guide to Becoming Financially Fit",
            "MoneyWISE is a Family Affair)","Be a Budget BOSS",
            "Managing Credit and Debt - The RIGHT Way","What's in YOUR B.A.G.?  Planning, Saving and Getting Resources for Your  Big, Audacious Goals",
            "Miss Independent:  A Womans Guide to Saving and Investing",
            "Protecting Your Assets; Protecting Your Family",
            "Your Financially Ever After","Rental Counseling",
            "Homebuyer Counseling",
            "Foreclosure Counseling",
            "High School Equivalency Program",
            "Job Readiness for Teens",
            "Early Childhood Center",
            "Newark Kids Code",
            "Youth Programs",
            "Adult Programs",
            "Early Head Start",
    ]
    count = [
        Visit.objects.filter(purpose="Job Placement Assistance").count(),
        Visit.objects.filter(purpose="Resume Preparation").count(),
        Visit.objects.filter(purpose="Mock Interviewing").count(),
        Visit.objects.filter(purpose="Construction").count(),
        Visit.objects.filter(purpose="Pre-Apprenticeship").count(),
        Visit.objects.filter(purpose="Microsoft Office Certification").count(),
        Visit.objects.filter(purpose="Public Income Benefits Screening").count(),
        Visit.objects.filter(purpose="Employment Services and Career Improvement").count(),
        Visit.objects.filter(purpose="Financial Workshop").count(),
        Visit.objects.filter(purpose="Financial Coaching").count(),
        Visit.objects.filter(purpose="Start Saving on a Shoestring").count(),
        Visit.objects.filter(purpose="Your Choices and Your Cha-CHING!!").count(),
        Visit.objects.filter(purpose="Early Career Guide to Becoming Financially Fit").count(),
        Visit.objects.filter(purpose="MoneyWISE is a Family Affair)").count(),
        Visit.objects.filter(purpose="Be a Budget BOSS").count(),
        Visit.objects.filter(purpose="Managing Credit and Debt - The RIGHT Way").count(),
        Visit.objects.filter(purpose="What's in YOUR B.A.G.?  Planning, Saving and Getting Resources for Your  Big, Audacious Goals").count(),
        Visit.objects.filter(purpose="Miss Independent:  A Womans Guide to Saving and Investing").count(),
        Visit.objects.filter(purpose="Protecting Your Assets; Protecting Your Family").count(),
        Visit.objects.filter(purpose="Your Financially Ever After").count(),
        Visit.objects.filter(purpose="Rental Counseling").count(),
        Visit.objects.filter(purpose="Homebuyer Counseling").count(),
        Visit.objects.filter(purpose="Foreclosure Counseling").count(),
        Visit.objects.filter(purpose="High School Equivalency Program").count(),
        Visit.objects.filter(purpose="Job Readiness for Teens").count(),
        Visit.objects.filter(purpose="Early Childhood Center").count(),
        Visit.objects.filter(purpose="Newark Kids Code").count(),
        Visit.objects.filter(purpose="Youth Programs").count(),
        Visit.objects.filter(purpose="Adult Programs").count(),
        Visit.objects.filter(purpose="Early Head Start").count(),
    ]
    date = [
        Visit.objects.filter(date__startswith="01/").count(),
        Visit.objects.filter(date__startswith="02/").count(),
        Visit.objects.filter(date__startswith="03/").count(),
        Visit.objects.filter(date__startswith="04/").count(),
        Visit.objects.filter(date__startswith="05/").count(),
        Visit.objects.filter(date__startswith="06/").count(),
        Visit.objects.filter(date__startswith="07/").count(),
        Visit.objects.filter(date__startswith="08/").count(),
        Visit.objects.filter(date__startswith="09/").count(),
        Visit.objects.filter(date__startswith="10/").count(),
        Visit.objects.filter(date__startswith="11/").count(),
        Visit.objects.filter(date__startswith="012/").count(),
    ]
    time = [
        Visit.objects.filter(time__startswith="03:",time__endswith="AM").count(),
        Visit.objects.filter(time__startswith="04:",time__endswith="AM").count(),
        Visit.objects.filter(time__startswith="05:",time__endswith="AM").count(),
        Visit.objects.filter(time__startswith="06:",time__endswith="AM").count(),
        Visit.objects.filter(time__startswith="07:",time__endswith="AM").count(),
        Visit.objects.filter(time__startswith="08:",time__endswith="AM").count(),
        Visit.objects.filter(time__startswith="09:",time__endswith="AM").count(),
        Visit.objects.filter(time__startswith="10:",time__endswith="AM").count(),
        Visit.objects.filter(time__startswith="11:",time__endswith="AM").count(),
        Visit.objects.filter(time__startswith="12:",time__endswith="PM").count(),
        Visit.objects.filter(time__startswith="01:",time__endswith="PM").count(),
        Visit.objects.filter(time__startswith="02:",time__endswith="PM").count(),
        Visit.objects.filter(time__startswith="03:",time__endswith="PM").count(),
        Visit.objects.filter(time__startswith="04:",time__endswith="PM").count(),
        Visit.objects.filter(time__startswith="05:",time__endswith="PM").count(),
        Visit.objects.filter(time__startswith="06:",time__endswith="PM").count(),
        Visit.objects.filter(time__startswith="07:",time__endswith="PM").count(),
        Visit.objects.filter(time__startswith="08:",time__endswith="PM").count(),
        Visit.objects.filter(time__startswith="09:",time__endswith="PM").count(),
        Visit.objects.filter(time__startswith="10:",time__endswith="PM").count(),
    ]
    gender = [
        Visit.objects.filter(gender="Male").count(),
        Visit.objects.filter(gender="Female").count(),
        Visit.objects.filter(gender="Other").count(),
    ]
    major = [
        Visit.objects.filter(major_purpose="Employment Programs").count(),
        Visit.objects.filter(major_purpose="Workforce Training Programs").count(),
        Visit.objects.filter(major_purpose="Financial Opportunity Center").count(),
        Visit.objects.filter(major_purpose="Workshops").count(),
        Visit.objects.filter(major_purpose="Housing").count(),
        Visit.objects.filter(major_purpose="Young Adults Program").count(),
        Visit.objects.filter(major_purpose="Youth Education").count(),
        Visit.objects.filter(major_purpose="Volunteering").count(),
        Visit.objects.filter(major_purpose="Other").count(),
    ]
    ethnicity = [
        Visit.objects.filter(race="White").count(),
        Visit.objects.filter(race="Black/Afro American").count(),
        Visit.objects.filter(race="Hispanic").count(),
        Visit.objects.filter(race="Asian").count(),
        Visit.objects.filter(race="Mixed").count(),
        Visit.objects.filter(race="Other").count(),
    ]
    household_income = {
        Visit.objects.filter(household_income="under $25,000").count(),
        Visit.objects.filter(household_income="$25,000 - $35,000").count(),
        Visit.objects.filter(household_income="$35,000 - $45,000").count(),
        Visit.objects.filter(household_income="$45,000 - $55,000").count(),
        Visit.objects.filter(household_income="$55,000 - $65,000").count(),
        Visit.objects.filter(household_income="$65,000 - $75,000").count(),
        Visit.objects.filter(household_income="$75,000 - $85,000").count(),
        Visit.objects.filter(household_income="over $85,000").count(),
    }
    context = {
        'total': Visit.objects.count(),
        'count': count,
        'date': date,
        'time': time,
        'major': major,
        'gender': gender,
        'ethnicity': ethnicity,
        'income': household_income,
        'friend': Visit.objects.filter(referral="Friend").count(),
        'online': Visit.objects.filter(referral="Online Advertisement").count(),
        'other': Visit.objects.filter(referral="Other").count(),
        'results': Visit.objects.all()
    }
    return render(request, 'view/reports.html', context)


class VisitorListView(ListView):
    model = Visit
    template_name = 'view/analytics.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'results'
    ordering = ['-date','-time']
    paginate_by = 15

class PostListView(ListView):
    model = Post
    template_name = 'view/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'view/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
