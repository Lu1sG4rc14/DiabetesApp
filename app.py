#  PROYECTO CONSOLIDACION STREAMLIT: FUNCION app.py

# Importaciones
import streamlit as st
import streamlit.components.v1 as stc
from streamlit_extras.stylable_container import stylable_container
from eda_app import run_eda_app
from ml_app import run_ml_app

# Función main()
def main():
	st.set_page_config(page_title='Diabetes App')
	
	menu = ["Home", "EDA", "ML", "Info"]
	opcion = st.sidebar.selectbox("Menu", menu)

	st.html("""	 
		<style>
			.container {
				background-color: blue;
				border-radius: 15px;
				padding: 20px;
				color: white;
				width: 800px;
				margin: 20px auto;
				text-align: center;
			}
			.title {
				font-size: 24px;
				font-weight: bold;
				margin-bottom: 10px;
			}
			.description {
				font-size: 16px;
			}
		</style>
		<body>
			<div class="container">
				<div class="title">App para la detección temprana de DM</div>
				<div class="description">(Diabetes Mellitus)</div>
			</div>
		</body>
	""")
		
	if opcion == 'Home':	

		st.markdown("### Home")
		st.markdown("### App para la detección temprana de DM")
		st.markdown("Dataset que contiene señales y sintomas que pueden indicar diabetes o posibilad de diabetes")
		
		st.divider()

		st.markdown("### Fuente de Datos")
		st.code("- https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset")

		st.divider()

		st.markdown("### Contenidos de la App")
		st.code("- EDA Section: Análisis exploratorio de los datos")
		st.code("- ML Section: Predicción de Diabetes basada en ML (Machine Learning)")

	elif opcion == 'EDA':
		run_eda_app()
	elif opcion == 'ML':
		run_ml_app()
	elif opcion == 'Info':
		stc.iframe("https://es.wikipedia.org/wiki/Diabetes_mellitus", height=800, width=800, scrolling=True)


if __name__ == '__main__':
	main()