import './Product.css';
import { useEffect, useState } from "react";
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';


const Product = () => {
   const [product, setProduct] = useState([])

    useEffect(() => {
      fetch('http://localhost:8000/api/v1/products/')
      .then(response => response.json())
      .then(data => setProduct(data))
    }, [])

   return (
      <div className="product-wrapper">
         <h2 className="product-title">Продукты</h2>
         <div className="product-inner">
            {
               product.map((item, index) => (
                     <Card style={{ width: '18rem' }}>
                        <Card.Body>
                           <Card.Title>{item.name}</Card.Title>
                           <Card.Text style={{ fontSize: '12px'}}>
                              Цена : {item.price}₸
                           </Card.Text>
                        </Card.Body>
                        <Card.Footer>
                           <Button variant="primary">Арендовать</Button>
                        </Card.Footer>
                     </Card>
                  )
               )
            }
         </div>
      </div>
   );
}


export default Product;