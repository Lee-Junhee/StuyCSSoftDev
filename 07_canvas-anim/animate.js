/*
 * PoA: Junhee Lee, Pratham Rawat
 * SoftDev2 pd1
 * K07 :: Animation
 * 2020-02-12
 */


//global variable initalization
var timestamp = 0;


//element initialization
const c = document.getElementById("arena");
const ctx = c.getContext("2d");
const animate = document.getElementById("enable");
const stop = document.getElementById("disable");
const emergency = document.getElementById("estop");

//animation code
const enable = function() {
	animate.removeEventListener("click", enable);
	stop.addEventListener("click", disable);
}

const disable = function() {
	stop.removeEventListener("click", disable);
	animate.addEventListener("click", enable);
}

//estop code
const estop = function() {
	animate.removeEventListener("click", enable);
	stop.removeEventListener("click", disable);
}



//button event handlers
animate.addEventListener("click", enable);
emergency.addEventListener("click", estop);
