

// document.querySelectorAll('.nav-link').forEach(anchor => {
//     anchor.addEventListener('click', function (e) {
//         e.preventDefault();
//         document.querySelector(this.getAttribute('href')).scrollIntoView({
//             behavior: 'smooth'
//         });
//     });
// });




document.addEventListener('DOMContentLoaded', function () {
    const addMoreButton = document.getElementById('add-more-btn');
    const showLessButton = document.getElementById('show-less-btn');
    const productCards = document.querySelectorAll('.product-card');
    
    const visibleCards = 3;  

    if (productCards.length > visibleCards) {
        for (let i = visibleCards; i < productCards.length; i++) {
            productCards[i].classList.add('d-none');
        }
        addMoreButton.style.display = 'inline-block';  
    }

    addMoreButton.addEventListener('click', function () {
        // Show all products
        productCards.forEach(card => {
            card.classList.remove('d-none');
        });

        addMoreButton.style.display = 'none';
        showLessButton.style.display = 'inline-block';
    });

    showLessButton.addEventListener('click', function () {
        for (let i = visibleCards; i < productCards.length; i++) {
            productCards[i].classList.add('d-none');
        }

        showLessButton.style.display = 'none';
        addMoreButton.style.display = 'inline-block';
    });
});




document.getElementById("see-more-btn-video").addEventListener("click", function() {
    var hiddenVideos = document.querySelectorAll(".video.hidden");
    hiddenVideos.forEach(function(video) {
        video.classList.remove("hidden");
    });
    this.style.display = "none";
    document.getElementById("see-less-btn-video").style.display = "inline-block";
});

document.getElementById("see-less-btn-video").addEventListener("click", function() {
    var visibleVideos = document.querySelectorAll(".video");
    visibleVideos.forEach(function(video, index) {
        if (index >= 2) {
            video.classList.add("hidden");
        }
    });
    document.getElementById("see-more-btn-video").style.display = "inline-block";
    this.style.display = "none";
});










function addToCart() {
    alert("Product added to cart.");
}






























































