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
var projectile = [-1, -1, 1, 1];


//element initialization
const c = document.getElementById("arena");
const ctx = c.getContext("2d");
ctx.fillStyle = "#0000ff";
ctx.strokeStyle = "#000000";

const start = document.getElementById("enable");
const stop = document.getElementById("disable");
const emergency = document.getElementById("estop");

//const logo = new Image();
//logo.src = "";

//animation code
const dot = function() {
	ctx.clearRect(0, 0, 600, 600);
	ctx.beginPath();
	ctx.arc(300, 300, 300 * (1 + Math.sin(Math.PI * timestamp * speed)) / 2, 0, Math.PI * 2);
	ctx.fill();
	ctx.stroke();
	ctx.closePath();
	timestamp += 1;
	currentFrame = window.requestAnimationFrame(animate);
}

const propulse = function() {
	ctx.clearRect(0, 0, 600, 600);
	//ctx.drawImage();
	ctx.arc(projectile[0], projectile[1], , 0, Math.PI * 2);
	if (projectile[0] >= 600) {
		projectile[3] = -1;
	}
	if (projectile[0] <= 0) {
		projectile[3] = 1;
	}
	if (projectile[1] >= 600) {
		projectile[4] = -1;
	}
	if (projectile[1] <= 0) {
		projectile[4] = 1;
	}
	currentFrame = window.requestAnimationFrame();
}
	

const auton = function() {
	start.removeEventListener("click", auton);
	stop.addEventListener("click", disable);
	window.cancelAnimationFrame(currentFrame);
	window.requestAnimationFrame(dot);
}

const teleop = function() {
	start.addEventListener("click", enable);
	stop.addEventListener("click", disable);
	window.cancelAnimationFrame(currentFrame);
	projectile[0] = Math.random() * 600;
	projectile[1] = Math.random() * 600;
	window.requestAnimationFrame(propulse);
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
	begin.removeEventListener("click", teleop);
}



//button event handlers
start.addEventListener("click", auton);
begin.addEventListener("click", teleop);
emergency.addEventListener("click", estop);
