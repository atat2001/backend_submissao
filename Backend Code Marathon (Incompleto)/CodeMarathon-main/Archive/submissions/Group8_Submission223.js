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
    
    let [n1, n2, n3] = input.split(",")
    n1 = parseInt(n1)
    n2 = parseInt(n2)
    n3 = parseInt(n3)
    let l = new Set()

    for (let i = 1; i <= n1 + 1; i++){
        l.add(n2 * i)
        l.add(n3 * i)
    }

    l = Array.from(l)
    
    l = l.sort((a,b)=>a-b)
    console.log(l[n1 -1])
}



//fetch_inputMultiline()
fetch_input()
