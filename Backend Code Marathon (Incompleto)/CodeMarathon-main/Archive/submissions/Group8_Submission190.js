const { count } = require('console');
const readline = require('readline');
function fetch_input() {
    const rl = readline.createInterface({
        input: process.stdin,
        terminal: false
    });

    
    rl.on("line", (input) => {
        main(input)
        process.exit(0);
    });
}

let inputs = [];
let input_len;
function fetch_inputMultiline() {
    const rl = readline.createInterface({
        input: process.stdin,
        terminal: false
    });

    


    rl.on("line", (input) => {
        
        if(!input_len) {
            input_len = parseInt(input) + 1;
            return;
        }

        if(input_len != inputs.length){
            inputs.push(input);
        }

        if (input_len - 1 != inputs.length) {
            return;
        }
        
        main(inputs);
        process.exit(0);
    });

}


function main(input) {
    let c = 0
    let sum = 0
    for (let i = 1; i <= input; i++){
        let v = i.toString()
        
        for (let val of v) {
            if (val == "0" || val == "1") {
                sum += 1
            }
        }
    }
    console.log(sum)
    
}



//fetch_inputMultiline()
fetch_input()
