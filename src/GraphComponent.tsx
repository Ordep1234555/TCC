import React, { useState, useEffect } from 'react';
import { Bar } from 'react-chartjs-2';

interface DataEntry {
  ano: number;
  mestrado: number;
  doutorado: number;
}

interface GraphComponentProps {
  data: DataEntry[];
}

const GraphComponent: React.FC<GraphComponentProps> = ({ data }) => {
  const [chartData, setChartData] = useState({});
  const [selectedType, setSelectedType] = useState('both');

  useEffect(() => {
    const filteredData = data.filter((entry: { mestrado: number; doutorado: number; }) => {
      if (selectedType === 'both') {
        return true;
      } else if (selectedType === 'mestrado') {
        return entry.mestrado > 0;
      } else if (selectedType === 'doutorado') {
        return entry.doutorado > 0;
      }
      return true;
    });

    const years = filteredData.map((entry: { ano: number; }) => `${entry.ano}`);
    const mestradoData = filteredData.map((entry: { mestrado: number; }) => entry.mestrado);
    const doutoradoData = filteredData.map((entry: { doutorado: number; }) => entry.doutorado);

    setChartData([{
      labels: years,
      datasets: [
        {
          label: 'Mestrado',
          backgroundColor: 'rgba(75,192,192,0.2)',
          borderColor: 'rgba(75,192,192,1)',
          borderWidth: 1,
          hoverBackgroundColor: 'rgba(75,192,192,0.4)',
          hoverBorderColor: 'rgba(75,192,192,1)',
          data: mestradoData,
        },
        {
          label: 'Doutorado',
          backgroundColor: 'rgba(255,99,132,0.2)',
          borderColor: 'rgba(255,99,132,1)',
          borderWidth: 1,
          hoverBackgroundColor: 'rgba(255,99,132,0.4)',
          hoverBorderColor: 'rgba(255,99,132,1)',
          data: doutoradoData,
        },
      ],
    }]);
  }, [data, selectedType]);

  const options = {
    scales: {
      x: { stacked: true },
      y: { stacked: true },
    },
  };

  return (
    <div>
      <select onChange={(e) => setSelectedType(e.target.value)}>
        <option value="both">Ambos</option>
        <option value="mestrado">Mestrado</option>
        <option value="doutorado">Doutorado</option>
      </select>
      <Bar data={chartData} options={options} />
    </div>
  );
};

export default GraphComponent;