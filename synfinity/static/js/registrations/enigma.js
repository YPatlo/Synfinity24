const nextButton = document.querySelector('.btn-next');
const prevButton = document.querySelector('.btn-prev');
const submitButton = document.querySelector('.btn-submit');
const steps = document.querySelectorAll('.form-step');
const form_steps = document.querySelectorAll('.step');
let active = 1;

submitButton.addEventListener('click', () => {
    window.location.href = "https://synfinity.gsshsr.in/registrations/success";
})

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
        nextButton.disabled = false;
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
    std1Name = document.getElementById('std1Name').value;
    std1Class = document.getElementById('std1Class').value;
    teamEmail = document.getElementById('teamEmail').value;
    teachEmail = document.getElementById('teachEmail').value;

    const data =[sklName,sklEmail,accTeach,std1Name,std1Class,teamEmail,teachEmail];

    for(let j = 0; j < data.length; j++){
        if (data[j] == null || data[j] == ""){
            alert("Please fill the form properly. The incorrectly filled inputs are highlighted in red.");
            active = 1;
            updateProgress();
            break;
        }
    }

    document.getElementById('sklNameR').innerHTML = sklName;
    document.getElementById('sklEmailR').innerHTML = sklEmail;
    document.getElementById('accTeachR').innerHTML = accTeach;
    document.getElementById('std1NameR').innerHTML = std1Name;
    document.getElementById('std1ClassR').innerHTML = std1Class;
    document.getElementById('teamEmailR').innerHTML = teamEmail;
    document.getElementById('teachEmailR').innerHTML = teachEmail;
}

updateProgress();
