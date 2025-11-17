import pandas as pd
import streamlit as st
import plotly.express as px

# Importando dados
df = pd.read_csv('./casas_final.csv')

# Configuração da página
st.set_page_config(
    page_title='Preços das casas',
    page_icon='🏠',
    layout='wide'
)

# Condeudo principal
st.title("Influência no preço das casas")
st.markdown("Dashboard feito para desafio técnico da Cati Jr, Analisando fatores que influenciam no preço das casas")

# Metricas Principais
st.subheader("Metricas gerais")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Média dos preços", f"{df['PrecoVenda'].mean():.2f}")
col2.metric("Menor preço", f"{df['PrecoVenda'].min():.2f}")
col3.metric("Maior preço", f"{df['PrecoVenda'].max():.2f}")
col4.metric("Desvio padrão", f"{df['PrecoVenda'].std():.2f}")

st.markdown("---")

#Principais informações sobre Preço venda
st.subheader("Informações sobre preço venda")
col_graf1, col_graf2 = st.columns(2)

with col_graf1:
   grafico_hist = px.histogram(
            df,
            x='PrecoVenda',
            nbins=30,
            title="Distribuição de Preços",
            labels={'PrecoVenda': 'Preços', 'count': ''}
   )
   grafico_hist.update_layout(title_x=0.1)
   st.plotly_chart(grafico_hist, use_container_width=True)

with col_graf2:
   grafico_box = px.box(
            df,
            x='PrecoVenda',
            title='Distribuição de Preços'
   )
   grafico_box.update_layout(title_x=0.1)
   st.plotly_chart(grafico_box, use_container_width=True)

st.markdown("---")
st.subheader("Informações sobre Vizinhança")

#Informações gerais sobre o Dataset
col_graf1, col_graf2 = st.columns(2)

media_por_bairro = df.groupby('Vizinhanca')['PrecoVenda'].mean().reset_index()
media_por_bairro = media_por_bairro.sort_values(
    by='PrecoVenda',
    ascending = False
)
with col_graf1:
  grafico_boxplot = px.bar(
      media_por_bairro,
      x='PrecoVenda',
      y='Vizinhanca',
      title='Distribuição de Preços por Vizinhança',
      color='Vizinhanca'
  )
  grafico_boxplot.update_layout(title_x=0.1)
  st.plotly_chart(grafico_boxplot, use_container_width=True)

media_por_bairro = df.groupby('Vizinhanca')['QualidadeGeral'].mean().reset_index()
media_por_bairro = media_por_bairro.sort_values(
    by='QualidadeGeral',
    ascending = False
)
with col_graf2:
  grafico_boxplot2 = px.bar(
      media_por_bairro,
      x='QualidadeGeral',
      y='Vizinhanca',
      title='Distribuição de Vizinhanca por Qualidade',
      color='Vizinhanca'
  )
  grafico_boxplot2.update_layout(title_x=0.1)
  st.plotly_chart(grafico_boxplot2, use_container_width=True)

grafico_dispercao_zoneamento = px.scatter(
    df,
    x='PrecoVenda',
    y='Zoneamento',
    title='Preços por Zoneamento',
    color='Zoneamento'
  )
grafico_dispercao_zoneamento.update_layout(title_x=0.1)
st.plotly_chart(grafico_dispercao_zoneamento, use_container_width=True)
