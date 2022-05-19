import justpy as jp


@jp.SetRoute('/')
def home():
	wp = jp.QuasarPage(tailwind=True)
	div = jp.Div(a=wp,
	             classes='bg-gray-200 h-screen')
	div1 = jp.Div(a=div,
	              classes='grid grid-cols-3 gap-2 p-4')
	in_1 = jp.Input(a=div1,
	                placeholder='Enter First Value',
	                classes='form-input')
	in_2 = jp.Input(a=div1,
	                placeholder='Enter Second Value',
	                classes='form-input')
	d_output = jp.Div(a=div1,
	                  text='Result Here',
	                  classes='text-gray-600')
	jp.Div(a=div1,
	       text='Just Another Div',
	       classes='text-gray-600')
	jp.Div(a=div1,
	       text='Yet Another Div',
	       classes='text-gray-600')

	div2 = jp.Div(a=div,
	              classes='grid gird-cols-2 gap-4')
	jp.QBtn(a=div2,
	        label='Calculate',
	        color='yellow',
	        icon='map',
	        classes='border border-blue-500 m-2 py-1 px-4 rounded '
	                'text-blue-600 hover:bg-red-500 hover:text-white',
	        click=sum_up,
	        in1=in_1,
	        in2=in_2,
	        d=d_output)
	jp.QLinearProgress(a=div2,
	                   rounded=True,
	                   striped=True,
	                   reversed=True,
	                   indeterminate=True,
	                   color='green')
	jp.Div(a=div2,
	       text='I Am A Cool Interactive Div',
	       classes='hover:bg-red-500',
	       mouseenter=mouse_enter,
	       mouseleave=mouse_leave
	       )
	return wp


def sum_up(widget, msg):
	sum_it = (float(widget.in1.value) + float(widget.in2.value))
	widget.d.text = sum_it


def mouse_enter(widget, msg):
	widget.text = 'A Mouse Has Entered'


def mouse_leave(widget, msg):
	widget.text = 'A Mouse Has Left'


jp.justpy()
jp.justpy(port=8003)
