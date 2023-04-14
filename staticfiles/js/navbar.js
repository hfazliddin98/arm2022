'use strict';

const btnDrop = document.getElementById('user-div');

const dropdownMenu = document.getElementById('dropdown_menu');

const userName = document.getElementById('user-name');
const userNameNew = document.getElementById('user-nameNew');

const userLastName = document.getElementById('user-lastName');
const userLastNameNew = document.getElementById('user-lastNameNew');



btnDrop.addEventListener('click', (e) => {
    if (dropdownMenu.classList.value.includes('d-none')) {
        dropdownMenu.classList.remove('d-none')
    } else {
        dropdownMenu.classList.add('d-none')
    }

    // dropdownMenu.classList.toggle('d-none')
})

document.addEventListener('click', (e) => {
    if (e.target.classList.value.includes('b_1') || e.target.classList.value == ('b_2') || e.target.classList.value == ('b_3') || e.target.classList.value == ('b_4') || e.target.classList.value == ('b_5') || e.target.classList.value == ('b_6') || e.target.classList.value == ('b_7') || e.target.classList.value.includes('a_1') || e.target.classList.value.includes('a_2') || e.target.classList.value.includes('a_3') || e.target.classList.value.includes('a_4') || e.target.classList.value.includes('a_5')) {
    
    } else {
        dropdownMenu.classList.add('d-none')
    }
    console.log(e.target);
})


