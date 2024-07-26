function flipCard() {
    const card = document.querySelector('.card');
    card.classList.toggle('flipped');
}

function playAudio() {
    const audioPlayer = document.getElementById('audioPlayer');
    audioPlayer.play();
}


document.querySelectorAll('.known').forEach(button => {
    button.addEventListener('click', function() {
        this.parentElement.style.display = 'none';
    });
});

document.querySelectorAll('.unknown').forEach(button => {
    button.addEventListener('click', function() {
        alert('Try again!');
    });
});
