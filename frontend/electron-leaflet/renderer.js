window.addEventListener('DOMContentLoaded', () => {
  const map = L.map('map').setView([51.505, -0.09], 13);

  const mapAgeInput = document.getElementById('mapAge');
  const dataRangeInput = document.getElementById('dataRange');

  mapAgeInput.addEventListener('change', () => {
    console.log(`Map Age: ${mapAgeInput.value}`);
  });

  dataRangeInput.addEventListener('input', () => {
    console.log(`Data Range: ${dataRangeInput.value}`);
  });

  // Função para buscar os dados da API utilizando Axios
  const fetchData = async () => {
    try {
      const response = await axios.get('http://localhost:8000/timescale');
      const data = response.data;

      const select = document.getElementById('mapAge');
      select.innerHTML = ''; // Limpa as opções existentes

      // Itera sobre os dados e cria uma nova opção para cada item
      data.items.forEach(item => {
        const option = document.createElement('option');
        option.value = item.value;
        option.text = item.label;
        select.add(option);
      });
    } catch (error) {
      console.error('Erro:', error);
    }
  };

  fetchData();

  const tileLayers = [
    'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
    'https://s3.amazonaws.com/wri-tiles/global-landcover/{z}/{x}/{y}.png'
  ];

  L.tileLayer(tileLayers[0], {
    attribution: '&copy; <a href="https://github.com/vinihss">Vinicius Heleno</a> contributors'
  }).addTo(map);
});
