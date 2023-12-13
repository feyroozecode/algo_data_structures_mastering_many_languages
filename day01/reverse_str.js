
/**
 * Reverse an String with js reverser
 */

function reverserV1(str){

    return str.split('').reverse().join('')

}

  // reverse with creating my own reverse fun
function reverserV2(str) {

    let reversed = ''

    /// show a char reversed 
    for (let char of str) {
        reversed = char + reversed;
    }

     console.log(reversed);
    //return reversed;
}

// start fun
let text = 'Assalam Aleykoum '

reverserV2(text)