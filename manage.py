#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.dev")
    os.environ['SECRET_KEY'] = '%m8=8s^p9!%f724p0so-te!hd#z5nik&$2ev91ct)vc3cbq-2&'
    os.environ['GOOGLE_OAUTH2_CLIENT_ID'] = '265798863135-2a1eaa757f5bs80iqgjhfd8vhi5rtbbs.apps.googleusercontent.com'
    os.environ['FACEBOOK_APP_ID'] = '1435142220033329'
    os.environ['FACEBOOK_API_SECRET'] = 'f969c16a7db301072662fd137651340f'
    os.environ['GOOGLE_OAUTH2_CLIENT_SECRET']  = 'E8XyZY6PYnL99Ngx6T-_Alkt'
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
