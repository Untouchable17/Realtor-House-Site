import React, {useState, useEffect} from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

function HouseDetail() {

    const {slug} = useParams();
    const [house, setHouse] = useState([])


    console.log(house)

    useEffect( () => {
        axios({
            method: "GET",
            url: `http://127.0.0.1:8000/api/strainer/${slug}/`
        }).then(response => {
            setHouse(response.data)
            console.log(response)

        })
    }, [slug])

    return (
        <div className="App">
          <h1>Test House Detail</h1>
            {house.title}
        </div>
    );


}

export default HouseDetail;