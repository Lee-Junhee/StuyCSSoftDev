//Team B-Button Warriors - Eric Lam & Junhee Lee
//SoftDev pd1
//K13 -- Ask Circles [Change || Die]
//2020-03-30

//initialization
const pic = document.getElementById("vimage");
const button = document.getElementById("clear");
const DOT_RADIUS = 10;
const DOT_COLOR_0 = "black";
const DOT_COLOR_1 = "red";

/* var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
c.setAttribute("cx", 0);
c.setAttribute("cy", 0);
c.setAttribute("r", 100);
c.setAttribute("fill", "red");
c.setAttribute("stroke", "black");
pic.appendChild(c); */

const draw = function(e) {
	if (e.target == pic){
		let x = e.offsetX;
		let y = e.offsetY;
		let dot = document.createElementNS("http://www.w3.org/2000/svg", "circle");
		dot.setAttribute("cx", x);
		dot.setAttribute("cy", y);
		dot.setAttribute("r", DOT_RADIUS);
		dot.setAttribute("fill", DOT_COLOR_0);
		pic.appendChild(dot);
		dot.addEventListener("mousedown", color);
	}
};

const color = function(e) {
	this.removeEventListener("mousedown", color);
	this.setAttribute("fill", DOT_COLOR_1);
	this.addEventListener("mousedown", die);
}

const die = function(e) {
}

const clear = function(e) {
	pic.innerHTML = '';
};

pic.addEventListener("mousedown", draw);
button.addEventListener("click", clear);
