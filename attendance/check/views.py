from django.shortcuts import render, redirect
from django.contrib.auth import logout 
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth import login as auth_login
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
from .models import User
from .models import UserGroup
from .models import Class
from .models import Attendance80131337
from .models import Attendance801Elite
from .models import AccAtt801
from django.contrib.auth import authenticate


#31337ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

@ensure_csrf_cookie
def login_view(request):
    if request.method == "POST":
        id = request.POST["id"]
        password = request.POST["password"]
        try:
            user = User.objects.get(id=id)
            if check_password(password, user.password):
                request.session['user_id'] = user.id
                if user.usergroup.group == 'professor':
                    return redirect("check:attendance")
                elif user.usergroup.group == 'student':
                    return redirect("check:student_main")
                else:
                    messages.error(request, "유저 그룹이 잘못되었습니다.")
            else:
                messages.error(request, "아이디나 비밀번호가 틀렸습니다.")
        except User.DoesNotExist:
            messages.error(request, "아이디나 비밀번호가 틀렸습니다.")
    return render(request, "check/login/login.html")

def logout_view(request):
    logout(request)
    return redirect('check:login')  # 로그인 페이지로 리다이렉션

#@login_required
def student_main(request):
    user = User.objects.get(id=request.session['user_id'])
    lectures = Class.objects.all()

    # 강의 별로 사용자의 출석 데이터를 가져옵니다.
    attendance_data = []
    for lecture in lectures:
        data = AccAtt801.objects.filter(stu=user, subject=lecture).first()
        if data is not None:
            attendance_data.append({
                'lecture': data.subject.subject,
                'acc_att_score': data.acc_att_score,
            })

    context = {
        'user': user,
        'lectures': lectures,
        'attendance_data': attendance_data,
    }

    return render(request, 'check/student/student_main.html', context)




from .models import Class

def student_att_view(request):
    user = User.objects.get(id=request.session['user_id'])
    lectures = Class.objects.all()
    context = {
        'user': user,
        'lectures': lectures,
    }


    return render(request, 'check/student/student_att.html', context)

#@login_required
def professor_main(request):
    user = User.objects.get(id=request.session['user_id'])
    lectures = Class.objects.all()
    attendance_data = AccAtt801.objects.filter(stu=user)
    
    attendance_data = [
        {
            'lecture': data.subject.subject,
            'acc_att_score': data.acc_att_score,
        }
        for data in attendance_data
    ]
    
    context = {
        'user': user,
        'lectures': lectures,
        'attendance_data': attendance_data,  # Pass attendance_data to the context
    }
    return render(request, 'check/professor/professor_main.html', context)

#@login_required
def professor_stack(request):
    user = User.objects.get(id=request.session['user_id'])
    lectures = Class.objects.all()

    context = {
        'user': user,
        'lectures': lectures,
    }

    return render(request, 'check/professor/professor_stack.html', context)

@ensure_csrf_cookie
def find_id(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        usermajor = request.POST.get('usermajor')
        if name and usermajor:
            try:
                user = User.objects.get(username=name,  usermajor=usermajor)
                return render(request, 'check/find_id/find_id_result.html', {'user': user})
            except User.DoesNotExist:
                messages.error(request, '일치하는 사용자가 없습니다.')
                return redirect('check:find_id')
        else:
            messages.error(request, '모든 필드를 입력해주세요.')
            return redirect('check:find_id')
    return render(request, 'check/find_id/find_id.html')


def find_id_result(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        id = request.POST.get('id')
        try:
            user = User.objects.get(username=username, id=id)
            return render(request, 'check/find_id/find_id_result.html', {'user': user})
        except User.DoesNotExist:
            messages.error(request, '해당 계정이 존재하지 않습니다.')
            return redirect('check:find_id')
    else:
        messages.error(request, '잘못된 접근입니다.')
        return redirect('check:find_id')

def password_reset_user(request):
    if request.method == 'POST':
        id = request.POST['id']
        username = request.POST['username']

        try:
            user = User.objects.get(id=id, username=username)
            # 사용자가 확인되었을 경우, 비밀번호 재설정 페이지로 리디렉션합니다.
            return redirect('check:password_reset_reset', user_id=user.id)  # user_id를 URL에 포함시킬 예정입니다.
        except User.DoesNotExist:
            messages.error(request, '아이디와 이메일이 일치하는 사용자를 찾을 수 없습니다.')

    return render(request, 'check/password_reset/password_reset_user.html')

def password_reset_reset(request, user_id):
    user = User.objects.get(pk=user_id)

    if request.method == 'POST':
        password = request.POST.get('password')
        password_confirmation = request.POST.get('password_confirmation')

        if password != password_confirmation:
            messages.error(request, '비밀번호가 일치하지 않습니다.')
        else:
            user.password = make_password(password)  # 직접 password 필드를 수정
            user.save()
            messages.success(request, '비밀번호가 성공적으로 변경되었습니다. 새 비밀번호로 로그인해주세요.')
            return redirect('check:login')

    return render(request, 'check/password_reset/password_reset_reset.html')



def register(request):
    if request.method == 'POST':
        id = request.POST['id']
        username = request.POST['username']
        usermajor = request.POST['usermajor']
        usergroup_name = request.POST['usergroup']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        if password == password_confirm:
            if User.objects.filter(id=id).exists():
                messages.error(request, '이미 존재하는 아이디입니다.')
                return redirect('check:register')
            else:
                usergroup, created = UserGroup.objects.get_or_create(group=usergroup_name)
                hashed_password = make_password(password)  # 암호화된 비밀번호 생성
                user = User.objects.create_user(id=id, password=hashed_password, username=username, usermajor=usermajor, usergroup=usergroup)
                user.save()
                messages.success(request, '회원가입이 완료되었습니다.')
                return redirect('check:login')
        else:
            messages.error(request, '비밀번호가 일치하지 않습니다.')
            return redirect('check:register')
    else:
        return render(request, 'check/register/register.html')


def agreement(request):
    return render(request, 'check/register/agreement.html')


def attendance_view(request):
    attendance_list = Attendance801Elite.objects.all()
    user = User.objects.get(id=request.session['user_id'])

    context = {
        'attendance_list': attendance_list,
        'user': user,
    }

    return render(request, 'check/attendance/attendance.html', context)

def attendance_view1(request):
    attendance_elite = Attendance801Elite.objects.all()
    user = User.objects.get(id=request.session['user_id'])

    context = {
        'attendance_elite': attendance_elite,
        'user': user,
    }

    return render(request, 'check/attendance/attendance_elite.html', context)



from django.contrib.auth import logout


def api_view(request):
    # Attendance 객체를 모두 가져옵니다.
    attendance_list = Attendance80131337.objects.all()

    # 각각의 상태에 대한 학생 수를 계산합니다.
    total = attendance_list.count()
    attendance_count = attendance_list.filter(attendance_status='출석').count()
    late = attendance_list.filter(attendance_status='지각').count()
    absent = attendance_list.filter(attendance_status='결석').count()
    leave = attendance_list.filter(attendance_status='이탈').count()

    # 전체 출석 정보를 가져옵니다.
    attendance_info = list(attendance_list.values('student_name','student_id','attendance_status', 'class_time', 'class_name'))

    # JsonResponse 객체를 만들어 반환합니다.
    return JsonResponse({
        'total': total, 
        'attendance_count': attendance_count, 
        'late': late, 
        'absent': absent,
        'leave': leave,
        'attendance': attendance_info,
    })

def api_view1(request):
    # Attendance 객체를 모두 가져옵니다.
    attendance_list = Attendance801Elite.objects.all()

    # 각각의 상태에 대한 학생 수를 계산합니다.
    total = attendance_list.count()
    attendance_count = attendance_list.filter(attendance_status='출석').count()
    late = attendance_list.filter(attendance_status='지각').count()
    absent = attendance_list.filter(attendance_status='결석').count()
    leave = attendance_list.filter(attendance_status='이탈').count()

    # 전체 출석 정보를 가져옵니다.
    attendance_info = list(attendance_list.values('student_name','student_id','attendance_status', 'class_time', 'class_name'))

    # JsonResponse 객체를 만들어 반환합니다.
    return JsonResponse({
        'total': total, 
        'attendance_count': attendance_count, 
        'late': late, 
        'absent': absent,
        'leave': leave,
        'attendance': attendance_info,
    })


from django.http import JsonResponse
from .models import AccAtt801
from django.core import serializers

def api_view2(request):
    # AccAtt801 모델의 모든 객체를 가져옵니다.
    acc_att_801_data = AccAtt801.objects.all()

    # 객체를 JSON으로 변환합니다.
    json_data = serializers.serialize('json', acc_att_801_data)

    # JsonResponse 객체를 반환합니다.
    return JsonResponse(json_data, safe=False)









    


