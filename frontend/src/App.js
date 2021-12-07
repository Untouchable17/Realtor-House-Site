import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link} from 'react-router-dom';


import HouseList from './components/HouseList';
import HouseDetail from './components/HouseDetail';


function App() {


  return (
    <Router>
        <Routes>
          <Route path="/houses" element={<HouseList/>} />
          <Route path="/house/:slug" element={<HouseDetail/>}/>
        </Routes>
    </Router>

  );
}

export default App;


//<div className="App">
//    <HouseList />
//</div>
//const App = () => (
//
////    <Router>
////        <Layout>
////            <Routes>
////                <Route exact path="/" element={<Home/>} />
////                <Route exact path="/about" element={<About/>} />
////                <Route exact path="/contact" element={<Contact/>} />
////                <Route exact path="/houses" element={<Houses/>} />
////                <Route exact path="/house/:id" element={<HouseDetail/>} />
////                <Route element={NotFound} />
////            </Routes>
////        </Layout>
////    </Router>
//);
//
//export default App;