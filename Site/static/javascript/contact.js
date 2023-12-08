document.addEventListener("DOMContentLoaded", () => {

    let contact_form = document.querySelector('#contact-form')
    let contact_message = document.querySelector('#contact-message');
    contact_message.setAttribute('style', 'display: none;');

    contact_form.onsubmit = () => {
        let name = contact_form.querySelector("[name='name']");
        let email = contact_form.querySelector("[name='email']");
        let phone = contact_form.querySelector("[name='phone']");
        let message = contact_form.querySelector("[name='message']");
        fetch('/contact_mail', {
            method: "POST",
            body: JSON.stringify({
                'name' : name.value,
                'email' : email.value,
                'phone' : phone.value,
                'message' : message.value,
            }),
        })
        .then(response => response.json())
        .then(result => {
            contact_message.innerHTML = result;
        });
        contact_message.removeAttribute('style');
        return false;
    }

});