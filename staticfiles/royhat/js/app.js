'use strict'
const form = document.querySelector('#form')

const selectDAT = document.querySelector('#select-lavozim')
const dekDiv = document.querySelector('#dekanat-div')
const ArmDiv = document.querySelector('#ARM-div')
const TalDiv = document.querySelector('#Talaba-div')

const inpId = document.getElementById('inp-id')
const inpEmail = document.getElementById('email-kirit')
const boshHarf = document.querySelectorAll('.bosh-harf')

const inpPassw = document.getElementById('inp-passw-1')
const inpPassw2 = document.getElementById('inp-passw-2')

const personImg = document.querySelector('#person-img')


const keyPass = document.querySelector('#key')
const eyePass = document.querySelector('#eye_pass')
const keyPass2 = document.querySelector('#key-pass-2')
const eyePass2 = document.querySelector('#eye_pass-2')


//regEX
const regEX_id = /^[0-9]{12}$/;
const regEX_passw = /^[a-zA-Z0-9]{6,12}$/;
const regEX_boshH = /^[a-zA-Z]$/;
const regEX_harfKatta = /^[A-Z]$/;
const emailRegEX =  /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/ 

dekDiv.classList.add('d-none')
ArmDiv.classList.add('d-none')
TalDiv.classList.add('d-none')

function name() {
    if(selectDAT.value == 1) {
        dekDiv.classList.remove('d-none')
        ArmDiv.classList.add('d-none')
        TalDiv.classList.add('d-none')
    } else if (selectDAT.value == 2){
        dekDiv.classList.add('d-none')
        ArmDiv.classList.remove('d-none')
        TalDiv.classList.add('d-none')
    } else if (selectDAT.value == 3){
        dekDiv.classList.add('d-none')
        ArmDiv.classList.add('d-none')
        TalDiv.classList.remove('d-none')
    }
}
selectDAT.addEventListener('click', (e)=>{
    name()
})
    //Hems id
inpId.addEventListener('keyup', e => {
    if (regEX_id.test(inpId.value)){
        inpId.classList.add('is-valid')
        inpId.classList.remove('is-invalid')
        personImg.classList.add('d-none')
    }else{
        inpId.classList.add('is-invalid')
        inpId.classList.remove('is-valid')
        personImg.classList.add('d-none')
    }
})
    //Email
inpEmail.addEventListener('keyup', ()=>{
    if(emailRegEX.test(inpEmail.value)) {
        inpEmail.classList.add('is-valid')
        inpEmail.classList.remove('is-invalid')
    } else {
        inpEmail.classList.add('is-invalid')
        inpEmail.classList.remove('is-valid')
    }
})

    //input Password
inpPassw.addEventListener('keyup', e => {
    if (regEX_boshH.test(inpPassw.value.charAt())) {
        if (regEX_passw.test(inpPassw.value)){
            inpPassw.classList.add('is-valid')
            inpPassw.classList.remove('is-invalid')
            keyPass.classList.add('d-none')
            eyePass.classList.remove('d-none')
            eyePass.classList.add('d-inline-block')
        }else{
            inpPassw.classList.add('is-invalid')
            inpPassw.classList.remove('is-valid')
            keyPass.classList.add('d-none')
            eyePass.classList.remove('d-none')
            eyePass.classList.add('d-inline-block')
        }
    }else{
        inpPassw.classList.add('is-invalid')
        keyPass.classList.add('d-none')
        eyePass.classList.remove('d-none')
        eyePass.classList.add('d-inline-block')
    }
})
    // inp Pass 2
inpPassw2.addEventListener('keyup', e => {
   if (inpPassw.value == inpPassw2.value){
        if (regEX_boshH.test(inpPassw2.value.charAt())) {
            if (regEX_passw.test(inpPassw2.value)){
                inpPassw2.classList.add('is-valid')
                inpPassw2.classList.remove('is-invalid')
                keyPass2.classList.add('d-none')
                eyePass2.classList.remove('d-none')
                eyePass2.classList.add('d-inline-block')
            }else{
                inpPassw2.classList.add('is-invalid')
                inpPassw2.classList.remove('is-valid')
                keyPass2.classList.add('d-none')
                eyePass2.classList.remove('d-none')
                eyePass2.classList.add('d-inline-block')
            }
        }else{
            inpPassw2.classList.add('is-invalid')
            keyPass2.classList.add('d-none')
            eyePass2.classList.remove('d-none')
            eyePass2.classList.add('d-inline-block')
        }
   } else {
        inpPassw2.classList.add('is-invalid')
        inpPassw2.classList.remove('is-valid')
        keyPass2.classList.add('d-none')

   }
})

    //icon eye
eyePass.addEventListener('click', e => {
    if(inpPassw.getAttribute('type') == "password"){
        inpPassw.setAttribute('type', 'text')
    }else if(inpPassw.getAttribute('type') == "text"){
        inpPassw.setAttribute('type', 'password')
    }
})

 //icon eye 2
 eyePass2.addEventListener('click', e => {
    if(inpPassw2.getAttribute('type') == "password"){
        inpPassw2.setAttribute('type', 'text')
    }else if(inpPassw2.getAttribute('type') == "text"){
        inpPassw2.setAttribute('type', 'password')
    }
})

boshHarf.forEach( (e)=> {
    e.addEventListener('keyup', (j)=>{
        if(regEX_harfKatta.test(e.value.charAt())) {
            e.classList.add('is-valid')
            e.classList.remove('is-invalid')
        } else {
            e.classList.add('is-invalid')
            e.classList.remove('is-valid')
        }
    })
})