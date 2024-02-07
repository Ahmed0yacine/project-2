from kivy.lang import Builder

from kivymd.app import MDApp

gg= '''
Screen
	MDFloatingActionButtonSpeedDial
		data: app.row
		rotation_root_button: True
		
'''
class MyApp(MDApp):
	row= {
		'text': 'gg'
	}
	
	def build(self):
		return Builder.load_string(gg)
		
MyApp().run()