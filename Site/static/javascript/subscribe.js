document.addEventListener("DOMContentLoaded", () => {

    let subscription_form = document.querySelector("#subscription-form");
    let subscribe_message = document.querySelector("#subscribe-message");
    subscribe_message.setAttribute('style', 'display: none;');
    
    subscription_form.onsubmit = () => {
        let name = subscription_form.querySelector("[name='name']").value;
        let email = subscription_form.querySelector("[name='email']").value;
        let events = subscription_form.querySelector("[name='events']").checked;
        let newsletter = subscription_form.querySelector("[name='newsletter']").checked;
        fetch('/subscribe', {
            method: "POST",
            body: JSON.stringify({
                "name" : name,
                "email" : email,
                "events" : events,
                "newsletter" : newsletter,
            }),
        })
        subscribe_message.removeAttribute('style');
        return false;
    }

});