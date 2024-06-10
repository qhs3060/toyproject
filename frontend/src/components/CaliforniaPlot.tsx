import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { ScatterChart, Scatter, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';

const CaliforniaPlot: React.FC = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    const backendUrl = process.env.REACT_APP_BACKEND_URL || 'http://127.0.0.1:8000';
    axios.get(`${backendUrl}/california/original`)
      .then(response => {
        console.log("California data:", response.data); // 데이터 확인
        setData(response.data);
      })
      .catch(error => {
        console.error("Error fetching the California data", error);
      });
  }, []);

  return (
    <div>
      <h2>California House Data</h2>
      <ScatterChart
        width={800}
        height={400}
        margin={{ top: 20, right: 20, bottom: 20, left: 20 }}
      >
        <CartesianGrid />
        <XAxis type="number" dataKey="longitude" name="Longitude" />
        <YAxis type="number" dataKey="latitude" name="Latitude" />
        <Scatter name="House" data={data} fill="#8884d8" />
        <Tooltip cursor={{ strokeDasharray: '3 3' }} />
        <Legend />
      </ScatterChart>
    </div>
  );
}

export default CaliforniaPlot;
