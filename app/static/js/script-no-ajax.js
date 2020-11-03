var stripe = Stripe(checkout_public_key);

const button = document.querySelector('#Comprar');

button.addEventListener('click',event =>{
    stripe.redirectToCheckout({
        sessionId:checkout_session_id
    }).then(function(result){

    });
})
  