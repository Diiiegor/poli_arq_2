import './components/App.css'
import Product from "./components/Product.jsx";
import {useEffect, useState} from "react";

function App() {
    const [products, setProducts] = useState([]);
    useEffect(() => {
        const fetchProducts = async () => {
            const response = await fetch('http://localhost:5000/api/products').then(resp => resp.json());
            setProducts(response);
        };

        fetchProducts();
    }, []);
    return (
        <>
            <div className="producs-list">
                {products.map((product) => (<Product key={product.id} product={product}/>))}
            </div>
        </>
    )
}

export default App
