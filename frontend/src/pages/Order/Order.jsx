import './Order.css';
import { useEffect, useState } from "react";
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import { getNameFromId } from '../../utils'


const Order = () => {
   const [order, setOrder] = useState([])
   const [product, setProduct] = useState([])

   useEffect(() => {
      fetch('http://localhost:8000/api/v1/orders/')
      .then(response => response.json())
      .then(data => setOrder(data))
   }, [])

   useEffect(() => {
      fetch('http://localhost:8000/api/v1/products/')
      .then(response => response.json())
      .then(data => setProduct(data))
   }, [])


   return (
      <div className="order-wrapper">
         <h2 className='order-title'>
            Аренды
         </h2>
         <div className="order-inner">
            {
               order.map((item, index) => (
                  <Card style={{ width: '18rem' }}>
                     <Card.Body>
                        <Card.Title>{
                           item.products.map(item => getNameFromId(item, product))
                        }</Card.Title>
                        <Card.Text style={{ fontSize: '12px'}}>
                           Период аренды : {item.start_date.replaceAll('-', '.')} - {item.end_date.replaceAll('-', '.')}
                        </Card.Text>
                        <Card.Text style={{ fontSize: '12px'}}>
                           Общая стоимость аренды : {item.total_cost}₸
                        </Card.Text>
                     </Card.Body>
                  </Card>
                  )
               )
            }
         </div>
      </div>

      
   );
}


export default Order;