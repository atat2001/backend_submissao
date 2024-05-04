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
    blocks = []
    let word = ""
    for (let i = 0; i < input.length; i++){
        if (input[i] in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) {
            blocks.push([word, input[i]])
            word = ""
        } else {
            word += input[i]
        }
    
    }

    
    console.log(blocks.sort((a,b)=>a[1]-b[1]).map(word=>word[0]).join(" "))
}



//fetch_inputMultiline()
fetch_input()
