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
    let ns = input.split(",")
    let s = []
    for (let v of ns) {
        s.push(parseInt(v))
    }
    
    let last = null
    let currentBlock = []
    let blocks = []
    for (let pointer in s) {
        if (last && s[pointer] == s[last]) {
            blocks[blocks.length -1].push(pointer)
        } else {
            currentBlock = [pointer]
            last = pointer
            blocks.push(currentBlock);
        }
    }
    
    s = (blocks.map(block => s[block[0]]))

    for (let i = 1; i < s.length; i++) {
        let nv = s[i]
        if (s[i - 1] < s[i]) {
            s[i] = Math.min(s[i - 1] + 1, s[i])
        }

        if (s[i + 1] < s[i]) {
            s[i] = Math.max(s[i + 1] + 1, s[i])
        }
        
    }
    
    console.log(s.reduce((a,b)=>a+b))
    



    
}



//fetch_inputMultiline()
fetch_input()