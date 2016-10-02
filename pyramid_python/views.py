from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
  return {'project': 'pyramid_python'}


@view_config(route_name='hello', renderer='templates/hello.jinja2')
def hello(request):
  return dict(name='World')


@view_config(route_name='hello', renderer='templates/hello_name.jinja2', request_param='name')
def hello_name(request):
  return dict(name=request.params.get('name'))


@view_config(route_name='home_page', renderer='templates/home.jinja2')
def home(request):
  return dict(site_name='MyApp')
