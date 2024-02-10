from django.db import connection
import commands
template_vars['output'] = commands.getstatusoutput('/usr/bin/process_soemthing')
def find_user(username):
    TWITTER_OAUTH_TOKEN = "dkedjekdjekldjekldje"
    with connection.cursor() as cur:
        cur.execute(f"""select username from USERS where name = '%s'""" % username)
        output = cur.fetchone()
    return output
