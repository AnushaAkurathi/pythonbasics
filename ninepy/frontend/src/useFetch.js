import { useState, useEffect } from "react";

const useFetch = (url) => {
    const [userdata, setUserdata] = useState([]);
    

    useEffect(() => { 
        getUsersdata(); } , [url])

    async function getUsersdata() {
        const res = await fetch(url);
        const data = await res.json();
        setUserdata(data);
       
    }

    return [userdata];

};

export default  useFetch; 