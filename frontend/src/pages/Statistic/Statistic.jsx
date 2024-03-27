import { useEffect, useState } from "react";
import './Statistic.css'
import Card from 'react-bootstrap/Card';
import ListGroup from 'react-bootstrap/ListGroup';

const Statistic = () => {
   const [statistic, setStatistic] = useState({})

   useEffect(() => {
      fetch('http://localhost:8000/api/v1/statistics/')
      .then(response => response.json())
      .then(data => setStatistic(data))
   }, [])
   
   return (
      <>
         {
            statistic && statistic.unrented_intervals && (
               <div>
               <h3>Интервал между {statistic.start_date} - {statistic && statistic.end_date}</h3>
               <div>
                  <h4 className='statistic-title'>Арендованные продукты</h4>
                  <div className='statistic-inner'>
                     {statistic.total_cost.map((item) => 
                        (
                           <Card style={{ width: '18rem' }}>
                              <Card.Header>{item.product__name}</Card.Header>
                              <ListGroup variant="flush">
                              <ListGroup.Item>Полная арендная цена : {item.total_cost}₸</ListGroup.Item>
                              <ListGroup.Item>Период между {item.order__start_date.replaceAll('-', '.')} - {item.order__end_date.replaceAll('-', '.')}</ListGroup.Item>
                              </ListGroup>
                           </Card>
                        )
                     )}
                  </div>
                  <h4 className='statistic-title'>Неарендованные продукты</h4>
                  <div className='statistic-inner'>
                     {
                        statistic.unrented_intervals.map((item) => (
                           <>
                              <Card style={{ width: '18rem' }}>
                                 <Card.Header>Продукты : {item.unrented_products.map(item => {
                                    if(item === 1){
                                       return 'Laptop '
                                    } else if(item === 2){
                                       return 'Mobile Phone'
                                    }
                                 })}</Card.Header>
                                 <ListGroup variant="flush">
                                 <ListGroup.Item>Период между {item.start_date} - {item.end_date}</ListGroup.Item>
                                 </ListGroup>
                              </Card>
                           </>
                        ))
                     }
                  </div>
               </div>
            </div>
            )
         } 
      </>
   );
}

export default Statistic