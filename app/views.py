from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Nono'}  #dummy user   	
    posts =[
        {
	      'author': {'nickname': 'John'},
	      'body': 'A lovely dat in New York City!'
	    },
        {
	      'author': {'nickname':'Bob'},
          'body': 'Excited about movie night tonight!'
	     },
	     {
	      'author': {'nickname':'Alice'},
          'body': '20 things to do with chickpeas'
	     },
	     {
	      'author': {'nickname':'Carol'},
          'body': 'It ain\'t enough' 
	     },
	     {
	      'author': {'nickname':'Nono'},
          'body': '20 exiting applications of topology'
	     }
	    ]

    return render_template('index.html', 
                            title='ZAP!',
		                    user=user,
					        posts=posts) 
