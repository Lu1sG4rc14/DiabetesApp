# PROYECTO DE CONSOLIDACION STREAMLIT: FUNCION eda_app.py

# Importaciones: streamlit, pandas, matplotlib, seaborn
import streamlit as st
import pandas as pd
import matplotlib as plt
import seaborn as sb
import plotly.graph_objects as go

# Función principal que emplearemos en la APP
def run_eda_app():
	menu = ["Descriptivo", "Gráfico"]
	opcion = st.sidebar.selectbox("SubMenu", menu)

	st.markdown("### Sección EDA")
	data = pd.read_csv("data/diabetes_data_upload.csv")
	data2 = pd.read_csv("data/diabetes_data_upload_clean.csv")

	if opcion == 'Descriptivo':
		st.markdown("### Análisis Descriptivo")

		st.write(data.head(10))

		with st.expander("Tipos de datos"):    
			st.dataframe(data.dtypes)
    
		with st.expander("Resumen descriptivo"):    
			st.dataframe(data2.describe())

		with st.expander("Distribución por género (Gender)"):    
			gender_count = (
				data["Gender"]
				.value_counts()
			)
			
			st.dataframe(gender_count)
    
		with st.expander("Distribución por clase/label (Class)"):    
			class_count = (
				data["class"]
				.value_counts()
			)
			
			st.dataframe(class_count)

	elif opcion == 'Gráfico':
		st.markdown("### Análisis Gráfico")

		col1 , col2 = st.columns([3,2])
		with col1:
			with st.expander("Gráfico de distribución por género (Gender)"):
				fig = go.Figure()
				gender_count = (
					data["Gender"]
					.value_counts()
					.reset_index()
					.rename(columns={"Gender": "Gender", "count": "Count"})
				)

				fig.add_trace(go.Bar(x=gender_count.Gender, y=gender_count.Count))
				st.plotly_chart(fig)
		
		with col2:
			with st.expander("Distribución por género (Gender)"):
				gender_count = (
				data["Gender"]
				.value_counts()
				)
				st.dataframe(gender_count)

		col3 , col4 = st.columns([3,2])
		with col3:
			with st.expander("Gráfico de distribución por clase (Class)"):
				fig = go.Figure()
				gender_count = (
					data["class"]
					.value_counts()
					.to_frame()
					.reset_index()
					.rename(columns={"class": "Class", "count": "Count"})
				)

				fig.add_trace(go.Bar(x=gender_count.Class, y=gender_count.Count))
				st.plotly_chart(fig)
		
		with col4:
			with st.expander("Distribución por clase (Class)"):
				gender_count = (
				data["class"]
				.value_counts()
				)
				st.dataframe(gender_count)

		with st.expander("Gráfico de distribución por edades (Age)"):
			bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, float('inf')]
			labels = ["Less than 10", "10-20", "20-30", "30-40", "40-50", "50-60", "60-70", "70-80", "80 and more"]

			fig = go.Figure()

			age_count = (
				pd.cut(data['Age'], bins=bins, labels=labels, right=False)
				.value_counts()
				.sort_index()
				.reset_index()
				.rename(columns={'Age': 'Age Range', 'count': 'Count'})
			)
			
			fig.add_trace(go.Bar(x=age_count['Age Range'],y=age_count.Count))
			st.plotly_chart(fig)			
			
		with st.expander("Detección de Outliers"):
			fig = go.Figure()
			fig.add_trace(go.Box(x=data['Gender'], y=data['Age']))
			st.plotly_chart(fig)
		
		with st.expander("Gráfico de Correlación"):    
			import numpy as np
			corr = data2.corr()

			fig = go.Figure()
			fig.add_trace(go.Heatmap(x=corr.columns, y=corr.columns,z=corr.values))
				 
			st.plotly_chart(fig)








