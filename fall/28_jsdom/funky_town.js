var foo = function(){
  console.log("foo");
}

//factorial
var fact = function(n){
  if(n < 2){
    return 1;
  }
  return n * fact(n-1);
}

//fact button stuff:
var fact_button = document.getElementById("fact");
var fact_arg = document.getElementById("fact_arg");
var fxn_fact = function(){
  var input = parseInt(fact_arg.value);
  if (isNaN(input)) {
    console.log("Invalid input: " + fact_arg.value);
    fact_arg.value = "";
  }else {
    fact_arg.value = "";
    console.log("fact(" + input + "): " + fact(input));
  }
}
fact_button.addEventListener("click", fxn_fact);

//fibbonaci
var fib = function(n){
  if(n == 0){
    return 0;
  }
  if(n <= 2){
    return 1;
  }
  return fib(n-1) + fib(n-2)
}
var fiblist = [0, 1];
var fib2 = function(n){
  if (n < 0){
    return 0;
  }
  if (!(n in fiblist)){
    fiblist[n] = fib2(n - 1) + fib2(n - 2);
  }
  return fiblist[n];
}

//fib button stuff
var fib_button = document.getElementById("fib");
var fib_arg = document.getElementById("fib_arg");
var fxn_fib = function(){
  var input = parseInt(fib_arg.value);
  if (isNaN(input)) {
    console.log("Invalid input: " + fib_arg.value);
    fib_arg.value = "";
  }else {
    fib_arg.value = "";
    console.log("fib(" + input + "): " + fib2(input));
  }
}
fib_button.addEventListener("click", fxn_fib);

//gcd
var gcd = function(a,b){
  if(a%b == 0) {
    return b;
  }
  return gcd2(b,a%b);
}

//gcd button stuff
var gcd_button = document.getElementById("gcd");
var gcd_arg1 = document.getElementById("gcd_arg1");
var gcd_arg2 = document.getElementById("gcd_arg2");
var fxn_gcd = function() {
  var input1 = parseInt(gcd_arg1.value);
  if (isNaN(input1)) {
    console.log("Invalid input: " + gcd_arg1.value);
    gcd_arg1.value = "";
  }else {
    gcd_arg1.value = "";
    var input2 = parseInt(gcd_arg2.value);
    if (isNaN(input2)){
      console.log("Invalid input: " + gcd_arg2.value);
      gcd_arg2.value = "";
    }else {
      gcd_arg2.value = "";
      console.log("gcd(" + input1 +", " + input2 + "): " + gcd(input1, input2));
    }
  }
}
gcd_button.addEventListener("click", fxn_gcd);

//randomStudent
listOfStudents = ["alice","bob","carl","dave"]
var randomStudent = function(students){
  return students[Math.floor(Math.random() * students.length)];
}

//rand button stuff
var rand_button = document.getElementById("rand");
var rand_arg = document.getElementById("rand_arg");
var fxn_rand = function(){
  var raw_input = rand_arg.value;
  var input = raw_input.split(",");
  rand_arg.value = "";
  console.log(randomStudent(input));
}
rand_button.addEventListener("click", fxn_rand);
