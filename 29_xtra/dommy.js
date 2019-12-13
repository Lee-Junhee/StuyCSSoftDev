var changeHeading = function(e) {
	var h = document.getElementById("h");
	var header = (e['type'] == 'mouseout')? 'Hello World': e['target'].innerHTML;
	h.innerHTML = header;
};

var removeItem = function(e) {
	e['target'].remove();
};

var lis = document.getElementsByTagName("li");

for(var i = 0; i < lis.length; i++) {
	lis[i].addEventListener("mouseover", changeHeading); 
	lis[i].addEventListener("mouseout", changeHeading);
	lis[i].addEventListener("click", removeItem);
};

var addItem = function(e) {
	var list = document.getElementById('thelist');
	var item = document.createElement('li');
	item.innerHTML = "WORD";
	item.addEventListener('click', removeItem);
	list.appendChild(item);
};

var button = document.getElementById("b");
button.addEventListener('click', addItem);

var fib = function(n) {
	if (n < 2) {
		return 1;
	}else {
		return fib(n - 1) + fib(n - 2);
	}
};

var addFib = function(e) {
	console.log(e);
	var fiblist = document.getElementById("fiblist");
	var elements = fiblist.getElementsByTagName("li");
	var entry = document.createElement("li");
	entry.innerHTML = fib(elements.length);
	fiblist.appendChild(entry);
};

var addFib2 = function(e) {
	console.log(e);
	var fiblist = document.getElementById("fiblist");
	var elements = fiblist.getElementsByTagName("li");
	var entry = document.createElement("li");
	entry.innerHTML = (elements.length < 2)? 1: Number(elements[elements.length - 1].innerHTML) + Number(elements[elements.length - 2].innerHTML);
	fiblist.appendChild(entry);
};

var fb = document.getElementById("fb");
fb.addEventListener("click", addFib2);
