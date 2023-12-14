/**
 * Day 2 
 * Factorial using recursive function 
 * Until the value is not equal to zero, the recursive function will call itself. 
 * Factorial can be calculated using the following recursive formula. 
 *  n! = n * (n – 1)!
 *  n! = 1 if n = 0 or n = 1
 */
function factorial(number) {
    if (number == 0 || number == 1) {
        return 1;
    }

    return number * factorial(number - 1);
}

function computeFactorial() {
    console.log('Factorial using recursive function');

    const readLine =
        require('readline')
            .createInterface({
                input: process.stdin,
                output: process.stdout
            });     

    readLine.question('Please enter a number: ', number => {
        console.log('The factorial of this number is ' + factorial(number));
        readLine.close()
    })
}

//computeFactorial();
module.exports = computeFactorial();
