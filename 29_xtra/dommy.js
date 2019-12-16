//Pratham Rawat and Junhee Lee
// SoftDev1 pd1
// K29 -- Sequential Progression, Search of the Witch
// 2020-15-10

var lis = document.getElementsByTagName("li");

var mouseover = function(e) {

	console.log(e['target'].innerHTML);
	document.getElementById("h").innerHTML = e['target'].innerHTML;
};

var mouseout = function(e) {
	console.log(e['target'].innerHTML);
	document.getElementById("h").innerHTML = "Hello World!";
};

var click = function(e) {
	console.log(e['target'].innerHTML);
	e['target'].remove();
};

for(var i = 0; i < lis.length; i++) {
	lis[i].addEventListener("mouseover", mouseover);
	lis[i].addEventListener("mouseout", mouseout);
	lis[i].addEventListener("click", click);
};

document.getElementById("b").addEventListener("click", function(e) {
	var newItem = document.createElement("li");
	newItem.innerHTML = "WORD";
	document.getElementById("thelist").appendChild(newItem);
	newItem.addEventListener("mouseover", mouseover);
	newItem.addEventListener("mouseout", mouseout);
	newItem.addEventListener("click", click);
	newItem.scrollIntoView();
});

var fibarray = [0n,1n,1n];
var fibcounter = 0;
var fibonacci = function(n) {
  if (n < 3) return fibarray[n];
  if (fibarray[n]) return fibarray[n];
  fibarray[n] = fibonacci(n - 1) + fibonacci(n - 2);
  return fibarray[n]
};

var fibonacciButWorse = function(first, second, n) {
	if(n == 0) return second;
	return fibonacciButWorse(second, first + second, n - 1);
}

var primeArray = [3n]
var primeCounter = 0;
var nextPrime = function() {
	var n = BigInt(primeArray[primeCounter]) + 2n;
	while(!isPrime(n)) {
		n += 2n;
	}
	primeArray.push(n);
	primeCounter += 1;
	console.log(n);
	return n;
}

var isPrime = function(n) {
	for(var i = 2n; i < n / 2n; i += 1n) {
		if(n % i == 0) return false;
	}
	return true;
}

document.getElementById("fb").addEventListener("click", function(e) {
	var newItem = document.createElement("li");
	newItem.innerHTML = fibonacci(fibcounter);
	fibcounter++;
	document.getElementById("fiblist").appendChild(newItem);
	newItem.scrollIntoView();
});

document.getElementById("pb").addEventListener("click", function(e) {
	var newItem = document.createElement("li");
	newItem.innerHTML = nextPrime();
	document.getElementById("primelist").appendChild(newItem);
	newItem.scrollIntoView();
});
