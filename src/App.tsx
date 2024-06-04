import React from 'react';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import { Bar } from 'react-chartjs-2';

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

export const options = {
  responsive: true,
  plugins: {
    legend: {
      position: 'top' as const,
    },
    title: {
      display: true,
      text: 'Conclusões por Ano',
    },
  },
};

const labels = ["1974", "1975", "1976", "1977", "1978", "1979", "1980", "1981", "1982", "1983",
"1984", "1985", "1986", "1987", "1988", "1989", "1990", "1991", "1992", "1993",
"1994", "1995", "1996", "1997", "1998", "1999", "2000", "2001", "2002", "2003",
"2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013",
"2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023",
"2024"];

export const data = {
  labels,
  datasets: [
    {
      label: 'Mestrado',
      data: [992, 1227, 1485, 1789, 2042, 2268, 2588, 2495, 2645, 2702, 2719, 2834, 2855, 3109, 3411, 4036, 4603, 5291, 6086, 6356, 6852, 8119, 9320, 10862, 12243, 14440, 18273, 20006, 24068, 25899, 24693, 27562, 28958, 30265, 33275, 36325, 38381, 40590, 43961, 45888, 46634, 47814, 49373, 48033, 48420, 47317, 36859, 22398, 137, 3, 0],
      backgroundColor: 'rgba(255, 99, 132, 0.5)',
    },
    {
      label: 'Doutorado',
      data: [297, 284, 290, 361, 404, 511, 708, 771, 840, 946, 981, 1187, 1212, 1247, 1427, 1593, 1731, 2013, 2503, 2604, 3053, 3515, 4077, 4465, 4928, 5624, 6226, 6977, 7864, 9181, 9363, 10269, 10641, 11209, 12041, 12773, 13170, 14238, 16085, 17401, 19161, 20609, 22209, 22936, 23901, 24330, 18861, 13311, 535, 3, 2],
      backgroundColor: 'rgba(53, 162, 235, 0.5)',
    },
  ],
};

export function App() {
  return (
    <div style={{ width: '100%', height: '100vh' }}>
      <Bar options={options} data={data} />
    </div>
  );
}
