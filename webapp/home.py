import justpy as jp
from webapp import layout
from webapp import page


class Home(page.Page):
	path = '/'

	@classmethod
	def serve(cls, request):
		wp = jp.QuasarPage(tailwind=True)
		lay = layout.DefaultLayout(a=wp)
		container = jp.QPageContainer(a=lay)
		div = jp.Div(a=container,
		             classes='bg-gray-200 p-2')
		jp.Div(a=div,
		       text='This Is The Home Page',
		       classes='text-4xl m-2')
		jp.Div(a=div,
		       text="""My name is Huynh Nhu and I come from Can Tho province. 
					   I'm am a student of the Can Tho university. 
					   I hope that I can build the house for my parents.
					   They will live with me forever.
					   Then I will get married with a beautiful girl and has a cute children.
					   For me,I want to have more than one money source and main job I like to work.
					   That is my dream.""",
		       classes='text-lg')
		return wp
