document.addEventListener("DOMContentLoaded", () => {
    console.log("DOCUMENT READY!!!!!");
  
    
    // PAINTING VIEW:

    // let mini_nav = document.querySelector('#mini-nav');

    let paintings = document.querySelectorAll('.painting-blurb');
    paintings.forEach(p => {
        p.addEventListener("click", view_painting);
    });
    
    let painting_view = document.querySelector('#painting-view');
    let painting = painting_view.querySelector('#view-painting-image');
    
    painting_view.querySelector('i').addEventListener("click", close_view_painting);
    
    let selected;
    let image;
    
    function view_painting(event) {
        let artist_email = painting_view.querySelector('#artist_email');
    
        let painting_id = event.target.getAttribute('data-id');
        selected = event.target.getAttribute('data-id');
        image = document.querySelector(`img[data-id="${selected}"]`);
        disableScroll();
        painting.append(image);

        fetch(`/painting_data/${painting_id}`)
        .then(response => response.json())
        .then(result => {
            artist_email.innerHTML = result;
        });

        painting_view.setAttribute('style', 'display: flex;');
        // mini_nav.style.display = "none";
    }
    

    function close_view_painting() {
        painting_view.setAttribute('style', 'display: none;');
        // mini_nav.style.display = "flex";
        enableScroll();
        document.querySelector(`.painting[data-id="${selected}"]`).append(image);
    }
      
    
    // controll scrolling when panels are opened and closed:
    let scrollable = true;
    let scrollTop;
    let scrollLeft;
    function disableScroll() {   
        scrollTop = window.scrollY || document.documentElement.scrollTop;
        scrollLeft = window.scrollX || document.documentElement.scrollLeft;
        scrollable = false;
    }
    
    function enableScroll() {
        // window.onscroll = function() {};
        scrollable = true;
    }

    // if any scroll is attempted, set this to the previous value
    window.onscroll = function() {
        if (scrollable == false) {
            window.scrollTo(scrollLeft, scrollTop);
        }
    };

});
 