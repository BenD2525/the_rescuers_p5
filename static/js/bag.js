const addButton = document.getElementById("add-bag");

if (addButton != null){ 
addButton.addEventListener('click', function(){
    let productId = this.dataset.product
    let action = this.dataset.action
    console.log('product ID: ',productId,'Action: ',action)
})}

function updateOrder(productId, action){
    const url = '/update_bag/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
        body.JSON.stringify({'productID: ', productId, 'Action: ', action})
    })
    
}