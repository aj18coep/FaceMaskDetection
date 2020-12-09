import Gtk
w=Gtk.Window()
table=Gtk.Table(5,5,True)
tb=Gtk.Entry()
class Window:
	def __init__(self):
		self.turn=False
	def equalclicked(self,widget):
		m=tb.get_text()
		m=str(op.calc(m))
		tb.set_text(m)
		self.turn=True
	def buttonclicked(self,widget):
		if self.turn==True:
			tb.set_text("")
			self.turn=False
		m=tb.get_text()
		m=m+widget._value
		tb.set_text(m)
	def clear(self,widget):
		tb.set_text("")
		self.turn=False
	def back(self,widget):
		m=tb.get_text()
		m=m[:-1]
		tb.set_text(m)
x=Window()

zero=Gtk.Button(label='0')
one=Gtk.Button(label='1')
two=Gtk.Button(label='2')
three=Gtk.Button(label='3')
four=Gtk.Button(label='4')
five=Gtk.Button(label='5')
six=Gtk.Button(label='6')
seven=Gtk.Button(label='7')
eight=Gtk.Button(label='8')
nine=Gtk.Button(label='9')
add=Gtk.Button(label='+')
sub=Gtk.Button(label='-')
mul=Gtk.Button(label='X')
div=Gtk.Button(label='/')
equ=Gtk.Button(label='=')
