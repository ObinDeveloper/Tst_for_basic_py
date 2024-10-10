// sample.js

const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

readline.question('Enter the first number: ', (firstNumber) => {
    readline.question('Enter the second number: ', (secondNumber) => {
        const sum = parseInt(firstNumber) + parseInt(secondNumber);
        console.log(`The sum of ${firstNumber} and ${secondNumber} is: ${sum}`);
        readline.close();
    });
});
