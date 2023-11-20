
from flask import  Flask


class miPrograma:

	def _init_(self):

		self.app=flask(_name_)

		self.app.add_url_rule('/nuevo', view_func=self.agregar)

        #iniciar el servidor
		self.app.run(debug=True)
	def agregar (self):
		
		return render_template('nuevoEstudiante.html')


miPrograma=programa()