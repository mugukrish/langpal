from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from account.models import UserAccountModel

def pass_user_profile_detials_tobase(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user)
        user_details = UserAccountModel.objects.get(user_name=user)
        return {"current_user":user_details}
    return {"current_user":None}