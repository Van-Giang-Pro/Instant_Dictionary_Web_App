import justpy as jp
import definition
from webapp import layout
from webapp import page
from webapp import page
import requests


class Dictionary(page.Page):
	path = '/dictionary'

	@classmethod
	def serve(cls, request):
		wp = jp.QuasarPage(tailwind=True)
		lay = layout.DefaultLayout(a=wp)
		container = jp.QPageContainer(a=lay)
		div = jp.Div(a=container,
		             classes='bg-gray-200 p-2')
		jp.Div(a=div,
		       text='Instant English Dictionary',
		       classes='text-4xl m-2')
		jp.Div(a=div,
		       text='Get the definition of any English word instantly as you type',
		       classes='text-lg m-2')
		input_div = jp.Div(a=div, classes="grid grid-cols-3")

		output_div = jp.Div(a=div,
		                    classes='m-2 p-2 text-lg border-2 h-52 border-gray-400 w-1/2 ')
		input_box = jp.Input(a=input_div,
		                     placeholder='Type in a wore here',
		                     width='100%',
		                     outputdiv=output_div,
		                     classes='m-2 bg-gray-200 border-2 border-gray-400 rounded w-2/5 focus:outline-none '
		                             'focus:border-purple-400 py-2 px-4 focus:bg-white')
		input_box.on('input', cls.get_definition)
		print(cls, request)
		return wp

	@staticmethod
	def get_definition(widget, msg):
		req = requests.get(f"http://127.0.0.1:8000/api?w={widget.value}")
		data = req.json()
		widget.outputdiv.text = " ".join(data['definition'])

