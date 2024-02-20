// # Q23) Conditional Tests: Write a series of conditional tests. Print a statement describing each test and your prediction for the results of each test. Your code should look something like this:
// #let car = 'subaru';
// #console.log("Is car == 'subaru'? I predict True.")
// #console.log(car == 'subaru')
// #• Look closely at your results, and make sure you understand why each line evaluates to True or False.
// #• Create at least 10 tests. Have at least 5 tests evaluate to True and another 5 tests evaluate to False.
// Equlaity test 1
var num1 = 5;
var num2 = 5;
console.log("Is num1 == num2? I predict true.");
console.log(num1 == num2);
// Equlaity test 2
var str1 = 'hello';
var str2 = 'hello';
console.log("Is str1 == str2? I predict True.");
console.log(str1 == str2);
// Equality test 3
var num5 = 15;
var num6 = 10;
console.log("Is num5 > num6? I predict True.");
console.log(num5 > num6);
// Equality test 4
var str3 = 'apple';
var str4 = 'banana';
console.log("Is str3 != str4? I predict True.");
console.log(str3 != str4);
// Equality test 5
var num7 = 8;
var num8 = 12;
console.log("Is num7 < num8? I predict True.");
console.log(num7 < num8);
// Inequality test 1
var obj1 = { name: 'John' };
var obj2 = { name: 'John' };
console.log("Is obj1 === obj2? I predict False.");
// Inequality test 2
var num15 = 20;
var num16 = 20;
console.log("Is num15 < num16? I predict False.");
console.log(num15 < num16);
// Inequality test 3
var num13 = 10;
var num14 = 10;
console.log("Is num13 > num14? I predict False.");
console.log(num13 > num14);
// Inequality test 4
var str5 = 'hello';
var str6 = 'world';
console.log("Is str5 == str6? I predict False.");
console.log(str5 == str6);
// Inequality test 5
var str19 = 'apple';
var str20 = 'apple';
console.log("Is str19 != str20? I predict False.");
console.log(str19 != str20);
// Q24) You don’t have to limit the number of tests you create to 10. If you want to try more comparisons, write more tests. Have at least one True and one False result for each of the following:
// • Tests for equality and inequality with strings
// • Tests using the lower case function
// • Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
// • Tests using "and" and "or" operators
// • Test whether an item is in a array
// • Test whether an item is not in a array
// Test 1: Equality check between strings
var str18 = 'hello';
var str28 = 'hello';
console.log("Is str1 == str2? I predict True.");
console.log(str1 == str2);
// Test 2: Inequality check between strings
var str33 = 'apple';
var str44 = 'banana';
console.log("Is str3 != str4? I predict True.");
console.log(str3 != str4);
// Test 3: Lowercase function test
var word = 'HELLO';
var lowercaseWord = word.toLowerCase();
console.log("Is lowercaseWord === 'hello'? I predict True.");
console.log(lowercaseWord === 'hello');
// Test 4: Numerical tests
var num11 = 10;
var num22 = 5;
console.log("Is num1 > num2? I predict True.");
console.log(num1 > num2);
console.log("Is num1 < num2? I predict False.");
console.log(num1 < num2);
console.log("Is num1 >= num2? I predict True.");
console.log(num1 >= num2);
console.log("Is num1 <= num2? I predict False.");
console.log(num1 <= num2);
console.log("Is num1 === num2? I predict False.");
console.log(num1 === num2);
// Test 5: "And" and "Or" operator tests
var a = true;
var b = false;
console.log("Is a && b? I predict False.");
console.log(a && b);
console.log("Is a || b? I predict True.");
console.log(a || b);
// Test 6: Test whether an item is in an array
var array = [1, 2, 3, 4, 5];
console.log("Is 3 in array? I predict True.");
console.log(array.includes(3));
// Test 7: Test whether an item is not in an array
console.log("Is 6 not in array? I predict True.");
console.log(!array.includes(6));
// Q25) Alien Colors #1: Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
// • Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
// • Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)
// Version 1: Passes the if test (Door_color is 'green'):
var Door_color = 'green';
if (Door_color === 'green') {
    console.log("The player just earned 5 points.");
}
// Version 2: Fails the if test (alien_color is not 'green'):
var alien_color = 'yellow';
if (alien_color === 'green') {
    console.log("The player just earned 5 points.");
}
// • If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
// • If the alien’s color isn’t green, print a statement that the player just earned 10 points.
// • Write one version of this program that runs the if block and another that runs the else block.
// Version 1: Runs the if block (house's color is green):
var house_color = 'green';
if (house_color === 'green') {
    console.log("The player just earned 5 points for shooting the alien.");
}
else {
    console.log("The player just earned 10 points.");
}
// Version 2: Runs the else block (wall's color isn't green):
var wall_color = 'red';
if (wall_color === 'green') {
    console.log("The player just earned 5 points for shooting the alien.");
}
else {
    console.log("The player just earned 10 points.");
}
// Q27) Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-else chain.
// • If the alien is green, print a message that the player earned 5 points.
// • If the alien is yellow, print a message that the player earned 10 points.
// • If the alien is red, print a message that the player earned 15 points.
// • Write three versions of this program, making sure each message is printed for the appropriate color alien.
// Version 1: Ball is green (player earns 5 points):
var Ball_color = 'green';
if (Ball_color === 'green') {
    console.log("The player earned 5 points.");
}
else if (Ball_color === 'yellow') {
    console.log("The player earned 10 points.");
}
else if (Ball_color === 'red') {
    console.log("The player earned 15 points.");
}
// Version 2: bat is yellow (player earns 10 points):
var bat_color = 'yellow';
if (bat_color === 'green') {
    console.log("The player earned 5 points.");
}
else if (bat_color === 'yellow') {
    console.log("The player earned 10 points.");
}
else if (bat_color === 'red') {
    console.log("The player earned 15 points.");
}
// Version 3: wicket is red (player earns 15 points):
var wicket_color = 'red';
if (wicket_color === 'green') {
    console.log("The player earned 5 points.");
}
else if (wicket_color === 'yellow') {
    console.log("The player earned 10 points.");
}
else if (wicket_color === 'red') {
    console.log("The player earned 15 points.");
}
// Q28) Write an if-else chain that determines a person’s stage of life. Set a value for the variable age, and then:
// • If the person is less than 2 years old, print a message that the person is a baby.
// • If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
// • If the person is at least 4 years old but less than 13, print a message that the person is a kid.
// • If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
// • If the person is at least 20 years old but less than 65, print a message that the person is an adult.
// • If the person is age 65 or older, print a message that the person is an elder.
var age = 30;
if (age < 2) {
    console.log("The person is a baby.");
}
else if (age >= 2 && age < 4) {
    console.log("The person is a toddler.");
}
else if (age >= 4 && age < 13) {
    console.log("The person is a kid.");
}
else if (age >= 13 && age < 20) {
    console.log("The person is a teenager.");
}
else if (age >= 20 && age < 65) {
    console.log("The person is an adult.");
}
else {
    console.log("The person is an elder.");
}
// Q29) Favorite Fruit: Make a array of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your array.
// • Make a array of your three favorite fruits and call it favorite_fruits.
// • Write five if statements. Each should check whether a certain kind of fruit is in your array. If the fruit is in your array, the if block should print a statement, such as You really like bananas!
// Create an array of favorite fruits
var favorite_fruits = ['apple', 'banana', 'mango'];
// Check if 'apple' is in the array
if (favorite_fruits.includes('apple')) {
    console.log("You really like apples!");
}
// Check if 'banana' is in the array
if (favorite_fruits.includes('banana')) {
    console.log("You really like bananas!");
}
// Check if 'mango' is in the array
if (favorite_fruits.includes('mango')) {
    console.log("You really like mangoes!");
}
// Check if 'strawberry' is in the array
if (favorite_fruits.includes('strawberry')) {
    console.log("You really like strawberries!");
}
// Check if 'kiwi' is in the array
if (favorite_fruits.includes('kiwi')) {
    console.log("You really like kiwis!");
}
// Q30) Hello Admin: Make a array of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the array, and print a greeting to each user:
// • If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
// • Otherwise, print a generic greeting, such as Hello Eric, thank you for logging in again.
// Array of usernames
var usernames = ['admin', 'john', 'alice', 'eric', 'sophia'];
// Loop through the array and print greetings
for (var i = 0; i < usernames.length; i++) {
    // Check if the username is 'admin'
    if (usernames[i] === 'admin') {
        console.log("Hello admin, would you like to see a status report?");
    }
    else {
        console.log("Hello " + usernames[i] + ", thank you for logging in again.");
    }
}
