import React from 'react';
import CaliforniaPlot from './CaliforniaPlot';
import IrisPlot from './IrisPlot';

const App: React.FC = () => {
  return (
    <div className="App">
      <h1>Data Visualization</h1>
      <CaliforniaPlot />
      <IrisPlot />
    </div>
  );
}

export default App;
