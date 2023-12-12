
/**
 * Wite a program that prints the numbers from 1 to 100 .
 * But for multiple of three (3) print [Fizz] instead of the number
 * and for multiple of five (5) print [Buzz]
 * For number are multiple of both three and five print FizzBuzz
 */
function fbFun(){

    // buucle
    for (i = 1; i <= 10; i++){
        
        let output = ''
        let text1  = 'Fizz'
        let text2  =  'Buzz'

        if (i % 3 == 0) {
            output = text1
            console.log(output);
        }

        if (i % 5 == 0) {
            output = text2    
            console.log(output);
        }

        if ((i % 3 == 0) && (i % 5 == 0)) {
            output += text2 
            console.log(output);
        }
        else {
            console.log(i);
        }

        output = '';
    }
}

fbFun();