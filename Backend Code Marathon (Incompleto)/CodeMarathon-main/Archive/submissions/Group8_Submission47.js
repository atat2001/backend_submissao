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

class Park{
    constructor() {
        this.park = {}
    }

    add(mat) {
        this.park[mat] = true
    }

    exit(mat) {
        this.park[mat] = false
    }


    echo() {
        let entries = Object.entries(this.park).filter(entry=>entry[1]).sort()
        console.log(entries.length)
        for (let entry of entries) {
            console.log(entry[0])
        }
    }
}

class Car{
    constructor(mat) {
        this.mat = mat;
        this.inUse = true
    }

    
}

function main(input) {
    input = input.slice(1)
    let park = new Park()

    
    for (line of input) {
        let [op, mat] = line.split(" - ", 2)
        if (op == "aceitarCarro") {
            park.add(mat)    
        } else if (op == "sairCarro") {
            park.exit(mat)
        }
        
    }

    park.echo()
    let output = null;

    
}



fetch_inputMultiline()
//fetch_input()