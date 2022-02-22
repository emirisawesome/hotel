import React from 'react';
import { Route, Routes } from 'react-router-dom';
import Footer from './comonents/Footer/Footer';
import Header from './comonents/Header/Header';
import Main from './pages/Main/Main';

const App = () => {
  return (
    <>
      <Header />
      <main>
        <Routes>
          <Route path='/' element={<Main />} />
        </Routes>
      </main>
      <Footer />

    </>
  );
};

export default App;