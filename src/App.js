
import logo from './logo.svg';
import './App.css';

function App() {
  function activateLasers(e) {
    e.preventDefault();
    fetch('/api').then(res => res.json()).then(data => {
      console.log(data.msg)
      if (data.msg === 0)
        alert('Succesfully wrote to the database!')
      else
        alert('Uh-oh... A problem ocurred')
    });
  };
  
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1>Hello!</h1>
        <h2>This app calls a Python API to write to mongoDB</h2>
        <button onClick={activateLasers}>
          Call API
        </button>
      </header>
    </div>
  );
}

export default App;
