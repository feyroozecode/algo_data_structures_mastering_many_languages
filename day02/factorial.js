/**
 * Day 2 
 * 
 */

const { log } = require('console');

function factorial(number) {
    if (number == 0 || number == 1) {
        return 1;
    }

    return number * factorial(number - 1);
}

function compute() {
     
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

compute();