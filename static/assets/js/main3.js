document.addEventListener('DOMContentLoaded', function () {
    const titles = document.querySelectorAll('.custom-title');
    const contents = document.querySelectorAll('.custom-content');

    titles.forEach(title => {
        title.addEventListener('mouseover', function () {
            const target = this.getAttribute('data-target');
            contents.forEach(content => {
                if (content.id === target) {
                    content.style.display = 'block';
                } else {
                    content.style.display = 'none';
                }
            });
        });
    });
});






// const btns = document.querySelectorAll(".btn-what-people-say-slider");
// const slideRow = document.getElementById("slide-row");
// const main = document.querySelector(".what-people-say");

// let currentIndex = 0;

// function updateSlide() {
//   const mainWidth = main.offsetWidth;
//   const translateValue = currentIndex * -mainWidth;
//   slideRow.style.transform = `translateX(${translateValue}px)`;

//   btns.forEach((btn, index) => {
//     btn.classList.toggle("active", index === currentIndex);
//   });
// }

// btns.forEach((btn, index) => {
//   btn.addEventListener("click", () => {
//     currentIndex = index;
//     updateSlide();
//   });
// });

// window.addEventListener("resize", () => {
//   updateSlide();
// });






$(document).ready(function () {
    $('.category-header').on('click', function () {
        $('.content-column-header').removeClass('active');
        const target = $(this).data('target');
        $(`#${target}`).addClass('active');
    });

    $('.subcategory').on('click', function (e) {
        e.preventDefault();
        const target = $(this).data('target');
        $(`#${target}`).addClass('active');
    });

    $('.subcategory').hover(function () {
        const target = $(this).data('target');
        $(`#${target}`).siblings('.content-column-header').removeClass('active');
        $(`#${target}`).addClass('active');
    });
});





















