
/**
 * 
 * Function to check if the input is valid and valid
 * Else parse and convert the data to good str if possible 
 */
const checkAndStripAlphaNum = (value) => {
    let str;

    switch(typeof value){
        case 'number':
            str = value.toString()
            break;
        case 'object':
            str = JSON.stringify(value)
            break;
        case 'string':
            str = value;
            break;
        case 'boolean':
            str = null;
    }

    if(str === null || str === undefined ){
        return null;
    } else if (str.length === 0) {
        return "";
    } else {
        const PATTERN = `'/[\W_ ]/g',""`;

        let newStr = str.toLowerCase().replace(PATTERN)

        return newStr;
    }
}


const isPalindrom = (value) => {
    let str = checkAndStripAlphaNum(value);

    if(str === null ) return false;

    checker = str.split('').reverse().join('') === str

    if (checker) {
        console.log('Is Palindrom');
    } else {
        console.log('Is not palindrom');
    }
    
    return checker;
}

// test
let text = 'BB'
isPalindrom(text)