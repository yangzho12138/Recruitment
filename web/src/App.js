import { Routes, Route } from 'react-router-dom'
import { Header } from './components/Header';
import { Home } from './screens/Home';
import { Signin } from './screens/Signin';
import { Register } from './screens/Register';
import { Resume } from './screens/Resume';

function App() {
  return (
    <>
      <Header />
      <Routes>
        <Route path='/' element={<Home/>}/>
        <Route path='/signin' element={<Signin/>}/>
        <Route path='/register' element={<Register/>}/>
        <Route path='/resume' element={<Resume />} />
      </Routes>
    </>
  );
}

export default App;
