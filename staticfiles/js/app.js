'use strict'
const inpId = document.getElementById('inp-id')
const inpPassw = document.getElementById('inp-passw')
const btn = document.getElementById('btn')
const forms = document.querySelectorAll('#form')
const noneBe1 = document.querySelector('#none_1')
const noneBe2 = document.querySelector('#none_2')
const eye = document.querySelector('#eye_pass')
const error = document.querySelector('#xato')

//regEX
const regEX_id = /^[0-9]{12}$/;
const regEX_passw = /^[a-zA-Z0-9]{6,12}$/;
const regEX_boshH = /^[a-zA-Z]$/;

    //input Id
inpId.addEventListener('keyup', e => {
    if (regEX_id.test(inpId.value)){
        inpId.classList.add('is-valid')
        inpId.classList.remove('is-invalid')
        noneBe1.classList.add('d-none')
    }else{
        inpId.classList.add('is-invalid')
        inpId.classList.remove('is-valid')
        noneBe1.classList.add('d-none')
    }
})

    //input Password
inpPassw.addEventListener('keyup', e => {
    if (regEX_boshH.test(inpPassw.value.charAt())) {
        if (regEX_passw.test(inpPassw.value)){
            inpPassw.classList.add('is-valid')
            inpPassw.classList.remove('is-invalid')
            noneBe2.classList.add('d-none')
            eye.classList.remove('d-none')
            eye.classList.add('d-inline-block')
        }else{
            inpPassw.classList.add('is-invalid')
            inpPassw.classList.remove('is-valid')
            noneBe2.classList.add('d-none')
            eye.classList.remove('d-none')
            eye.classList.add('d-inline-block')
        }
    }else{
        inpPassw.classList.add('is-invalid')
        noneBe2.classList.add('d-none')
        eye.classList.remove('d-none')
        eye.classList.add('d-inline-block')
    }
})
    //icon eye
eye.addEventListener('click', e => {
    if(inpPassw.getAttribute('type') == "password"){
        inpPassw.setAttribute('type', 'text')
    }else if(inpPassw.getAttribute('type') == "text"){
        inpPassw.setAttribute('type', 'password')
    }
})



function xatolik() {
    if(error.textContent.includes('xato')) {
        inpId.classList.add('is-invalid')
        inpPassw.classList.add('is-invalid')
    }
}
xatolik()




