/*
 * PoA: Junhee Lee, Pratham Rawat
 * SoftDev2 pd1
 * K07 :: Animation
 * 2020-02-12
 */


//global variable initalization
var timestamp = 0;
const dspeed = 0.01;
const pspeed = 1;
var currentFrame;
var projectile = [-1, -1, 1, 1];


//element initialization
const c = document.getElementById("arena");
const ctx = c.getContext("2d");
ctx.fillStyle = "#0000ff";
ctx.strokeStyle = "#000000";

const start = document.getElementById("enable");
const stop = document.getElementById("disable");
const propulsion = document.getElementById("projectile");
const emergency = document.getElementById("estop");

const logo = new Image();
logo.src = "FIRST.jpg";
const height = 27;
const width = 105;

//animation code
const dot = function() {
	ctx.clearRect(0, 0, 600, 600);
	ctx.beginPath();
	ctx.arc(300, 300, 300 * (1 + Math.sin(Math.PI * timestamp * dspeed)) / 2, 0, Math.PI * 2);
	ctx.fill();
	ctx.stroke();
	ctx.closePath();
	timestamp += 1;
	currentFrame = window.requestAnimationFrame(dot);
}

const propulse = function() {
	projectile[0] += projectile[2] * pspeed;
	projectile[1] += projectile[3] * pspeed;
	console.log("P1" + projectile[0]);
	console.log("P2" + projectile[1]);
	ctx.clearRect(0, 0, 600, 600);
	ctx.drawImage(logo, projectile[0], projectile[1], 70, 18);
	//ctx.beginPath();
	//ctx.arc(projectile[0], projectile[1], 20, 0, Math.PI * 2);
	//ctx.fill();
	//ctx.stroke();
	//ctx.closePath();
	if (projectile[0] >= 600 - width) {
		projectile[2] = -2;
	}
	if (projectile[0] <= 0) {
		projectile[2] = 2;
	}
	if (projectile[1] >= 600 - height) {
		projectile[3] = -1;
	}
	if (projectile[1] <= 0) {
		projectile[3] = 1;
	}
	currentFrame = window.requestAnimationFrame(propulse);
}


const auton = function() {
	start.removeEventListener("click", auton);
	stop.addEventListener("click", disable);
	window.cancelAnimationFrame(currentFrame);
	window.requestAnimationFrame(dot);
}

const teleop = function() {
	start.addEventListener("click", auton);
	stop.addEventListener("click", disable);
	window.cancelAnimationFrame(currentFrame);
	projectile[0] = Math.random() * (600 - width);
	projectile[1] = Math.random() * (600 - height);
	projectile[2] = 2;
	projectile[3] = -1;
	window.requestAnimationFrame(propulse);
}

const disable = function() {
	stop.removeEventListener("click", disable);
	start.addEventListener("click", auton);
	window.cancelAnimationFrame(currentFrame);
}

//estop code
const estop = function() {
	disable();
	start.removeEventListener("click", enable);
	stop.removeEventListener("click", disable);
	propulsion.removeEventListener("click", teleop);
}



//button event handlers
start.addEventListener("click", auton);
propulsion.addEventListener("click", teleop);
emergency.addEventListener("click", estop);
