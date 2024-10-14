import folium

# Localização central do mapa (Brasil)
mapa = folium.Map(location=[-15, -50], zoom_start=4)

# Adicionando os pontos
for d in dados:
    folium.Marker(
        location=[d["latitude"], d["longitude"]],
        popup=f"Bacia: {d['bacia']}, Paleoclima: {d['paleoclima']}",
        icon=folium.Icon(color="blue" if d["paleoclima"] == "h" else "green")
    ).add_to(mapa)

# Salvar o mapa em um arquivo HTML
mapa.save("mapa_paleoclima.html")

# Exibir o mapa no Jupyter Notebook (se aplicável)
