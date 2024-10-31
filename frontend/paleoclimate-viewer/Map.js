import React, { useEffect } from 'react';
import 'ol/ol.css';
import { Map as OlMap, View } from 'ol';
import TileLayer from 'ol/layer/Tile';
import OSM from 'ol/source/OSM';

const Map = ({ geologicalEra, humanDate }) => {
    useEffect(() => {
        const map = new OlMap({
            target: 'map',
            layers: [
                new TileLayer({
                    source: new OSM(),
                }),
            ],
            view: new View({
                center: [0, 0],
                zoom: 2,
            }),
        });

        // Update map layers based on geologicalEra and humanDate here

        return () => map.setTarget(null);
    }, [geologicalEra, humanDate]);

    return <div id="map" style={{ width: '100%', height: '500px' }} />;
};

export default Map;
