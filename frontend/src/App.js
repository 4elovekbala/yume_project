import './App.css';
import {
  Routes,
  Route,
  Link
} from "react-router-dom";
import { LinkContainer } from 'react-router-bootstrap'
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import Order from './pages/Order/Order';
import Product from './pages/Product/Product';
import Statistic from './pages/Statistic/Statistic';

function App() {
  return (
    <div className="App">
      <div className='navbar'>
        <Navbar expand="lg" className="bg-body-tertiary" data-bs-theme="dark" style={{ borderRadius: '10px' }}>
          <Container>
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav">
              <Nav className="me-auto">
                <LinkContainer to='/products'>
                  <Nav.Link>Products</Nav.Link>
                </LinkContainer>
                <LinkContainer to="/orders">
                  <Nav.Link>Orders</Nav.Link>
                </LinkContainer>
                <LinkContainer to="/statistics">
                  <Nav.Link>Statistic</Nav.Link>
                </LinkContainer>
              </Nav>
            </Navbar.Collapse>
          </Container>
        </Navbar>
      </div>
      <Routes>
        <Route path='/' />
        <Route path="/products" element={<Product />} />
        <Route path="/orders" element={<Order />} />
        <Route path="/statistics" element={<Statistic />} />
      </Routes>
    </div>
  );
}

export default App;
