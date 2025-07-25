import { animate } from 'https://cdn.jsdelivr.net/npm/animejs/+esm';


// console.log(1);
const circle1Elm = document.querySelector('.circle1');
const circle2Elm = document.querySelector('.circle2');
const circle3Elm = document.querySelector('.circle3');
const circle4Elm = document.querySelector('.circle4');
const circle5Elm = document.querySelector('.circle5');
const resultElm = document.querySelector('.result');
const result2Elm = document.querySelector('.result2');



animate(circle1Elm, {
    duration: 2000,
    scale: [1, .98, 1],
    loop: true,
});

const html = `<img class="back-img" src="{{ url_for('gacha.static', filename='gacha/img/left.png') }}" alt="←">`;


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
        // 被った場合の処理
        if (resultElm.classList.contains('overlapping')) {
            window.setTimeout(() => {
                animate(resultElm, {
                    duration: 800,
                    rotateY: '90deg',
                    easing: 'cubicBezier(.64,.64,.37,.08)'
                });
            },1200);
            window.setTimeout(() => {
                result2Elm.style.display = 'block';
                animate(result2Elm, {
                    duration: 800,
                    rotateY: ['-90deg','0deg'],
                    easing: 'cubicBezier(.37,.08,.64,.64)'
                });
            },2000)
        }
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
    window.setTimeout(() => {
        const backElm = document.getElementById('back');
        backElm.style.display = 'block';
        if (!resultElm.classList.contains('overlapping')) {
            const newElm = document.getElementById('new');
            newElm.style.display = 'block';
            animate(newElm, {
                duration: 800,
                scale: [0,1.1,1],
                easing: 'easeOutBack'
            });
        }
        backElm.addEventListener('click', () => {
            // history.back();
            window.location.href = '/mypage';
        })
    },1100)
})