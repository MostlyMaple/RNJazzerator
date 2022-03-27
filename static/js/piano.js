"use strict";
let noteString = "";
let notesRemain = 170;
document.getElementById("notesPlayed").innerHTML = noteString; 
document.getElementById("counter").innerHTML = notesRemain;

window.addEventListener("keydown", (e) => {
const key = document.querySelector(`.key[data-note="${e.key}"]`);
const audio = document.querySelector(`audio[data-note="${e.key}"]`);
if (notesRemain != 0){
if (e.target.getAttribute("keydown") == audio.getAttribute("keydown")) {
noteString += event.key;
notesRemain--;
document.getElementById("notesPlayed").innerHTML = noteString;
document.getElementById("counter").innerHTML = notesRemain;
  }
}
if (!audio) return;
audio.currentTime = 0;
audio.play();
key.classList.add("playing");
});

window.addEventListener("click", (e) => {
  const sounds = document.querySelectorAll("audio[data-note]");
  sounds.forEach((sound) => {
    //if(notesRemain != 0){
    if (e.target.getAttribute("data-note") == sound.getAttribute("data-note")) {
      noteString += e.target.getAttribute("data-note");
      notesRemain --;
      document.getElementById("notesPlayed").innerHTML = noteString;
      document.getElementById("counter").innerHTML = notesRemain;
      console.log(notesRemain);
      console.log(noteString);
      sound.currentTime = 0;
      sound.play();
  }
  });
});

const keys = document.querySelectorAll(".key");
keys.forEach((key) => key.addEventListener("transitionend", removeStyle));

function removeStyle() {
  this.classList.remove("playing");
}

// loader
$(window).on("load", () => {
  setTimeout(removeLoader, 1600);
});

function removeLoader() {
  $("#loadingDiv").fadeOut(500, () => {
    $("#loadingDiv").remove();
  });
}
