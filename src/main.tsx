import * as React from 'react';
import ReactDOM from 'react-dom/client';
import GraphComponent from './GraphComponent.tsx';
import data from './dados.json';  // Importe seus dados
import Chart from './ReCharts.tsx';
import './index.css';

const root: ReactDOM.Root = ReactDOM.createRoot(document.getElementById('root') as HTMLElement);

const App: React.FC = () => {
  return (
    <div>
      <h1>Gráfico de Mestrado e Doutorado por Ano</h1>
      <GraphComponent data={data} />
    </div>
  );
};

export default App;


root.render(<React.StrictMode><Chart/></React.StrictMode>);