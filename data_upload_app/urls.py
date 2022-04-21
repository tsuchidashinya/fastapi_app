from controllers import *

app.add_api_route('/', index)
app.add_api_route('/admin', admin)
app.add_api_route('/view', style)
app.add_api_route('/style_main', style_main)