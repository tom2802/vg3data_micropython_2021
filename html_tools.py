def render_template_string(template_string, **kwargs):
    s = template_string
    for k in kwargs:
        s = s.replace('{{ ' + k + ' }}', str(kwargs[k]))
    return s

def render_template(filename, **kwargs):
    with open(filename) as template:
        s = render_template_string(template.read(), **kwargs)
    return s


def test_render_template_string():
    t = '<h1>Hello {{ name }}</h1'
    h = render_template_string(t, name='Tom')

#test_render_template_string()