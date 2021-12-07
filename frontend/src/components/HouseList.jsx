import React, {useState, useEffect} from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

function Houses() {

    const [houses, setHouses] = useState([])


    useEffect( () => {
        axios({
            method: "GET",
            url: "http://127.0.0.1:8000/api/strainer/"
        }).then(response => {
            setHouses(response.data)
            console.log(response.data);
        })

    }, [])

    return (
        <div className="App">
          <h1>Test Houses</h1>
            {houses.map(house => (
                    <div className="col-md-4" key={house.id}>
                        <h4>{house.title}</h4>
                        <p>{house.description}</p>
                        <p>{house.id}</p>
                        <Link to={{pathname: `/house/${house.slug}`, fromDashboard: false}}>Детальнее</Link>
                    </div>
                ))}
        </div>
    );


}

export default Houses;