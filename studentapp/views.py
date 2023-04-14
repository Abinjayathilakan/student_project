from django.shortcuts import render,redirect
from studentapp.models import StudentDetails

# Create your views here.
def index(request):
    return render(request,'student.html')
def add_student(request):
    if request.method=="POST":
        sname=request.POST['Student_name']
        add=request.POST['Address']
        age=request.POST['Age']
        mail=request.POST['Email']
        jd=request.POST['Joining_date']
        quali=request.POST['Qualification']
        gen=request.POST['Gender']
        number=request.POST['Mobile_number']
        student=StudentDetails(Student_name=sname,Address=add,Age=age,Email=mail,Joining_date=jd,Qualification=quali,Gender=gen,Mobile_number=number)
        student.save()
        return redirect('show_students')

def show_students(request):
    students=StudentDetails.objects.all()
    return render(request,'show_students.html',{'student':students})

def editpage(request,pk):
    std=StudentDetails.objects.get(id=pk)
    return render(request,'edit.html',{"students":std})
    
def edit_student_details(request, pk):
    if request.method == "POST":
        std = StudentDetails.objects.get(id=pk)
        std.Student_name = request.POST.get('s_name')
        std.Address = request.POST.get('Add')
        std.Age = request.POST.get('age')
        std.Email = request.POST.get('mail')
        std.Joining_date = request.POST.get('date')
        std.Qualification = request.POST.get('Quali')
        std.Gender = request.POST.get('Gen')
        std.Mobile_number = request.POST.get('number')
        std.save()
        return redirect('show_students')
    else:
        std = StudentDetails.objects.get(id=pk)
        return render(request, 'edit.html', {'std': std})
    
def deletepage(request,pk):
    delete_student=StudentDetails.objects.get(id=pk)
    delete_student.delete()
    return redirect('show_students')


def linkpage(request):
    link=StudentDetails.objects.all()
    return render(request,'linkpage.html',{'std':link})

def link_student(request,pk):
    std=StudentDetails.objects.get(id=pk)
    return render(request,'viewpage.html',{"student":std})    




# def stud_page(request):
#     student=Student.objects.all()
#     return render(request,"studpage.html",{'std':student})
# def student_detail(request,id):
#     std=Student.objects.get(id=id)
#     return render(request, 'student_detail.html',{'student':std})