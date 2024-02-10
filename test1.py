@app.route("/page")
def page():

    name = request.values.get('name')

    output = Jinja2.from_string('Hello ' + name + '!').render()

    return output
