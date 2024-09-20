const Product = ({product}) => {

    const stock = () => {
        if (product.inventory) {
            const spanClass = product.inventory.stock > 0 ? 'span-success' : 'span-danger'

            return (
                <>
                    <div className="stock-container">
                        <span>
                            <p>Stock {product.inventory.stock}</p>
                        </span>
                        <span className={spanClass}>
                            <p>{product.inventory.stock > 0 ? 'In Stock' : 'Out of stock'}</p>
                        </span>
                    </div>
                </>
            )
        } else {
            return (
                <>
                    <div className="stock-container">
                        <span><p>Stock 0</p></span>
                        <span className="span-danger"><p>Out of stock</p></span>
                    </div>
                </>)
        }
    }

    return (
        <div className="product-card">
            <div>
                <img
                    src={product.image}
                    alt=""/>
            </div>
            <div className="product-body">
                <p className="product-title">{product.name}</p>
                <p className="product-description">
                    {product.description}
                </p>
                {stock()}
            </div>
            <div className="product_id">
                ID: {product.id}
            </div>
        </div>
    );
}

export default Product;