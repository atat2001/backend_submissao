//
//  main.c
//  p1
//
//  Created by Edson da Veiga on 3/12/22.
//

#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <fcntl.h>
#include <stdbool.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <pthread.h>
#include <signal.h>


typedef struct {
    
    char matricula[10];
    bool EmUso;
} Carro;

int numTodosC = 0;

Carro todosC[9999];

typedef struct {
    int vagasOcupadas;
    Carro *Carros[5];
} ParqueEstacionamento;

ParqueEstacionamento parqueArtur;



void aceitarCarro(char ma[10] ) {
    
    int a = -1;
    
    for (int i = 0; i< numTodosC; i++) {
        if (strcmp(ma, todosC[i].matricula) == 0) {
            a = i;
            break;
        }
    }
    
    if (a == -1) {
        strcpy(todosC[numTodosC].matricula,ma);
        todosC[numTodosC].EmUso = true;
        a = numTodosC;
        numTodosC++;
    }
    
    for (int j = 0; j < 5; j++) {
        if(parqueArtur.Carros[j] == NULL || !parqueArtur.Carros[j]->EmUso) {
            parqueArtur.Carros[j] = &todosC[a];
            todosC[a].EmUso = true;
            parqueArtur.vagasOcupadas++;
            break;
        }
    }

}

void rejeitarCarro(char ma[10] ) {

}

void alterarEstadoCarro (char ma[10]) {
    
    for (int i = 0; i< 5; i++) {
        if (strcmp(ma, parqueArtur.Carros[i]->matricula) == 0 && parqueArtur.Carros[i]->EmUso) {
            parqueArtur.Carros[i]->EmUso = false;
            numTodosC--;
            return;
        }
    }
    
    aceitarCarro(ma);
    
    

}



int main(int argc, const char * argv[]) {
    
    int q = 0 ;
    
        
    char fun[11];
    char ma[10];
    
    parqueArtur.vagasOcupadas = 0;
    
    for (int i =0; i<5; i++) {
        parqueArtur.Carros[i] = NULL;
    }
    
    scanf("%d", &q);
    
    for (int i = 0; i < q; i++) {
        
        scanf("%s - %s", fun, ma);

        if (strcmp(fun, "aceitarCarro") == 0) {
            if(parqueArtur.vagasOcupadas != 5)
                aceitarCarro(ma);
            else
                rejeitarCarro(ma);
        }

        if (strcmp(fun, "sairCarro") == 0) {
            alterarEstadoCarro(ma);
        }
        
    }
    
    printf("%d\n", parqueArtur.vagasOcupadas);
    
    for (int i = 0; i < 5; i++) {
        if (parqueArtur.Carros[i]->EmUso)
            printf("%s\n", parqueArtur.Carros[i]->matricula);
    }
    
    return 0;
}
