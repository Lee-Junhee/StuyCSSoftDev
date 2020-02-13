/*
 * PoA: Junhee Lee, Pratham Rawat
 * SoftDev2 pd1
 * K07 :: Animation
 * 2020-02-12
 */


//global variable initalization
var timestamp = 0;
const speed = 0.01;
var currentFrame;


//element initialization
const c = document.getElementById("arena");
const ctx = c.getContext("2d");
ctx.fillStyle = "#0000ff";
ctx.strokeStyle = "#000000";

const start = document.getElementById("enable");
const stop = document.getElementById("disable");
const emergency = document.getElementById("estop");

//animation code
const animate = function() {
	ctx.clearRect(0, 0, 600, 600);
	ctx.beginPath();
	ctx.arc(300, 300, 300 * (1 + Math.sin(Math.PI * timestamp * speed)) / 2, 0, Math.PI * 2);
	ctx.fill();
	ctx.stroke();
	ctx.closePath();
	timestamp += 1;
	currentFrame = window.requestAnimationFrame(animate);
}

const enable = function() {
	start.removeEventListener("click", enable);
	stop.addEventListener("click", disable);
	window.requestAnimationFrame(animate);
}

const disable = function() {
	stop.removeEventListener("click", disable);
	start.addEventListener("click", enable);
	window.cancelAnimationFrame(currentFrame);
}

//estop code
const estop = function() {
	disable();
	start.removeEventListener("click", enable);
	stop.removeEventListener("click", disable);
}



//button event handlers
start.addEventListener("click", enable);
emergency.addEventListener("click", estop);
