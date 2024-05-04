import java.util.Scanner;
import java.util.ArrayList;


class ParqueEstacionamento {
	private ArrayList<Carro> _carros = new ArrayList<>();
	
	
	public int capacidade() {
		int i = 0;
		for(Carro c : _carros) {
			if(c.estado()) {i++;}
		}

		return i;
	}
	
	private boolean estaCheio() {
		return capacidade() == 5;
	}
	
	
	public void aceitarCarro(String matricula) {
		if(!estaCheio()) {
		if(!alterarEstadoCarro(matricula)) {_carros.add(new Carro(matricula));}
		}
	}
	
	
	public boolean alterarEstadoCarro(String matricula) {
		for(Carro c : _carros) {
			if(c.matricula().equals(matricula)) {
				c.alterarEstado();
				return true;
			}
		}

		return false;
	}
	
	
	public ArrayList<String> listaAtual() {
		ArrayList<String> lista = new ArrayList<>();

		for(Carro c : _carros) {
			if(c.estado()) { lista.add(c.matricula());}
		}

		return lista;
	}
}


class Carro {
	private String _matricula;
	private boolean _emUso;

	Carro(String matricula) {
		_matricula = new String(matricula);
		_emUso = true;
	}


	public String matricula() {return new String(_matricula);}
	
	public boolean estado() { return _emUso;}
	
	public void alterarEstado() {
		if(_emUso == false) { _emUso = true;}
		else { _emUso = false;}
	}
}



public class 112 {
	public static void main(String args[]) {
		ParqueEstacionamento parque = new ParqueEstacionamento();
		Scanner input = new Scanner(System.in);

		String line;
		while(input.hasNextLine()) {
			line = input.nextLine();
			if(line.startsWith("aceitarCarro")) { parque.aceitarCarro(line.substring(15));}

			if(line.startsWith("sairCarro")) { parque.alterarEstadoCarro(line.substring(12));}
		}

		System.out.println(parque.capacidade());
		ArrayList<String> lista = parque.listaAtual();
		for(String s : lista) { System.out.println(s);}
	}
}
