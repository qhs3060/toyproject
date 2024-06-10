import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { ScatterChart, Scatter, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';

const IrisPlot: React.FC = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    const backendUrl = process.env.REACT_APP_BACKEND_URL || 'http://127.0.0.1:8000';
    axios.get(`${backendUrl}/iris/original`)
      .then(response => {
        console.log("Iris data:", response.data); // 데이터 확인
        setData(response.data);
      })
      .catch(error => {
        console.error("Error fetching the Iris data", error);
      });
  }, []);

  return (
    <div>
      <h2>Iris Data</h2>
      <ScatterChart
        width={800}
        height={400}
        margin={{ top: 20, right: 20, bottom: 20, left: 20 }}
      >
        <CartesianGrid />
        <XAxis type="number" dataKey="sepal_length" name="Sepal Length" />
        <YAxis type="number" dataKey="sepal_width" name="Sepal Width" />
        <Scatter name="Iris" data={data} fill="#82ca9d" />
        <Tooltip cursor={{ strokeDasharray: '3 3' }} />
        <Legend />
      </ScatterChart>
    </div>
  );
}

export default IrisPlot;
