
import React, { useEffect } from 'react';
import { MapContainer, TileLayer } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import { Container, TextField, Box } from '@mui/material';

export const App = () => {
  useEffect(() => {
    // Lógica adicional, se necessário
  }, []);

  return (
    <Container>
      <Box display="flex" flexDirection="column" alignItems="flex-start" mt={2}>
        <TextField label="Idade do Mapa" variant="outlined" margin="normal" />
        <TextField label="Intervalo de Idade dos Dados" variant="outlined" margin="normal" />
      </Box>
      <Box mt={2} height="80vh">
        <MapContainer center={[51.505, -0.09]} zoom={13} style={{ height: '100%', width: '100%' }}>
          <TileLayer
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            attribution="&copy; <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a> contributors"
          />
        </MapContainer>
      </Box>
    </Container>
  );
};
        