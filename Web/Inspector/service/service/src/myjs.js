function my_animation(){
    let start = Date.now();
    let timer = setInterval(function () {
        let timePassed = Date.now() - start;

        train.style.left = timePassed / 5 + 'px';

        if (timePassed > 2000)
            clearInterval(timer);

    }, 20);
}

/* Javascript helps to enhance the webpage. Anyways part 3/3 of the flag: _pur4_luck?} */
