var fact = function(n) {
	return (n > 1)? fact(n - 1) * n:1;
};

var fib = function(n) {
	return (n > 2)? fib(n-1) + fib(n-2): 1;
};

var gcd = function(a, b) {
	if (b > a) {
		var c = a;
		a = b;
		b = c;
	}
	a %= b;
	return (a == 0)? b: gcd(a, b);
}

var students = ["bob", "alice"];

var randomStudent = function() {
	return students[Math.floor(students.length * Math.random())];
};
