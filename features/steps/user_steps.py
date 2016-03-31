from colab.accounts.models import User

@given(u'The user "{username}" with the password "{password}" that is "{status}"')
def create_user(context, username, password, status):
    
    user = User()
    user.username = username
    user.set_password(password)
    user.email = "usertest@colab.com.br"
    user.id = 1
    user.twitter = "usertestcolab"
    user.facebook = "usertestcolab"
    user.first_name = "USERtestCoLaB"
    user.last_name = "COLAB"
    user.needs_update = False
    
    if status == "active":
        user.is_active = True
    else:
        user.is_active = False
    
    user.save()