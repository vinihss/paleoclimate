import React, { useState } from 'react';
import { AppBar, Toolbar, Typography, Select, MenuItem, FormControl, InputLabel, Grid, Box } from '@mui/material';
import Map from './components/Map';
import { geologicalEras, humanDates } from './data/timeData';

function App() {
    const [geologicalEra, setGeologicalEra] = useState('');
    const [humanDate, setHumanDate] = useState('');

    return (
        <div>
            <AppBar position="static">
                <Toolbar>
                    <Typography variant="h6">Paleoclimate Map Viewer</Typography>
                </Toolbar>
            </AppBar>

            <Box p={2}>
                <Grid container spacing={2}>
                    <Grid item xs={12} md={4}>
                        <FormControl fullWidth>
                            <InputLabel>Geological Era</InputLabel>
                            <Select
                                value={geologicalEra}
                                onChange={(e) => setGeologicalEra(e.target.value)}
                            >
                                {geologicalEras.map((era) => (
                                    <MenuItem key={era.value} value={era.value}>{era.label}</MenuItem>
                                ))}
                            </Select>
                        </FormControl>
                    </Grid>

                    <Grid item xs={12} md={4}>
                        <FormControl fullWidth>
                            <InputLabel>Human Date</InputLabel>
                            <Select
                                value={humanDate}
                                onChange={(e) => setHumanDate(e.target.value)}
                            >
                                {humanDates.map((date) => (
                                    <MenuItem key={date.value} value={date.value}>{date.label}</MenuItem>
                                ))}
                            </Select>
                        </FormControl>
                    </Grid>

                    <Grid item xs={12}>
                        <Map geologicalEra={geologicalEra} humanDate={humanDate} />
                    </Grid>
                </Grid>
            </Box>
        </div>
    );
}

export default App;
