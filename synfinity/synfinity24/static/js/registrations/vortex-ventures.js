const nextButton = document.querySelector('.btn-next');
const prevButton = document.querySelector('.btn-prev');
const submitButton = document.querySelector('.btn-submit');
const steps = document.querySelectorAll('.form-step');
const form_steps = document.querySelectorAll('.step');
let active = 1;

nextButton.addEventListener('click', () => {
    active++;
    if(active > steps.length){
        active = steps.length;
    }
    updateProgress();
})

prevButton.addEventListener('click', () => {
    active--;
    if (active < 1){
        active = 1;
    }
    updateProgress();
})

const updateProgress = () => {
    console.log('steps.length =>' + steps.length);
    console.log('active =>' + active);

    steps.forEach((step, i) => {
        if (i == (active-1)){
            step.classList.add('active');
            form_steps[i].classList.add('active');
            console.log('i =>' +i);
        } else {
            step.classList.remove('active');
            form_steps[i].classList.remove('active');
        }
    });

    if (active == 1){
        prevButton.disabled = true;
    } else if (active == steps.length){
        nextButton.disabled = true;
        confirmData();
    } else{
        prevButton.disabled = false;
        nextButton.disabled = false;
    }
}

const confirmData = () => {
    sklName = document.getElementById('sklName').value;
    sklEmail = document.getElementById('sklEmail').value;
    accTeach = document.getElementById('accTeach').value;
    teamName = document.getElementById('teamName').value;
    std1Name = document.getElementById('std1Name').value;
    std1Class = document.getElementById('std1Class').value;
    std2Name = document.getElementById('std2Name').value;
    std2Class = document.getElementById('std2Class').value;
    std3Name = document.getElementById('std3Name').value;
    std3Class = document.getElementById('std3Class').value;
    std4Name = document.getElementById('std4Name').value;
    std4Class = document.getElementById('std4Class').value;
    teamEmail = document.getElementById('teamEmail').value;
    teachEmail = document.getElementById('teachEmail').value;

    document.getElementById('sklNameR').innerHTML = sklName;
    document.getElementById('sklEmailR').innerHTML = sklEmail;
    document.getElementById('accTeachR').innerHTML = accTeach;
    document.getElementById('teamNameR').innerHTML = teamName;
    document.getElementById('std1NameR').innerHTML = std1Name;
    document.getElementById('std1ClassR').innerHTML = std1Class;
    document.getElementById('std2NameR').innerHTML = std2Name;
    document.getElementById('std2ClassR').innerHTML = std2Class;
    document.getElementById('std3NameR').innerHTML = std3Name;
    document.getElementById('std3ClassR').innerHTML = std3Class;
    document.getElementById('std4NameR').innerHTML = std4Name;
    document.getElementById('std4ClassR').innerHTML = std4Class;
    document.getElementById('teamEmailR').innerHTML = teamEmail;
    document.getElementById('teachEmailR').innerHTML = teachEmail;
}

updateProgress();