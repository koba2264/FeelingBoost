import { animate } from 'https://cdn.jsdelivr.net/npm/animejs/+esm';


// console.log(1);
const circle1Elm = document.querySelector('.circle1');
const circle2Elm = document.querySelector('.circle2');
const circle3Elm = document.querySelector('.circle3');
const circle4Elm = document.querySelector('.circle4');
const circle5Elm = document.querySelector('.circle5');
const resultElm = document.querySelector('.result');

animate(circle1Elm, {
    duration: 2000,
    scale: [1, .98, 1],
    loop: true,
});


circle3Elm.addEventListener('click', () => {
    circle3Elm.innerHTML="";
    circle1Elm.style.zIndex = 2;
    circle4Elm.style.zIndex = 1;
    window.setTimeout(() => {
        resultElm.style.zIndex = 2;
        circle5Elm.style.zIndex = 2;
        animate(resultElm, {
            duration: 800,
            scale: 16
        });
        animate(circle5Elm, {
            duration: 900,
            scale: 10
        });
    },300)
    animate(circle1Elm, {
        duration: 800,
        delay: 150,
        scale: 2.5,
    });
    animate(circle2Elm, {
        duration: 2200,
        delay: 250,
        scale: 10,
    });
    animate(circle3Elm, {
        duration: 2200,
        delay: 250,
        scale: 10,
    });
    animate(circle4Elm, {
        duration: 1700,
        delay: 150,
        scale: 40,
    });
})