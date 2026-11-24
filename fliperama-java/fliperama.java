/*
 * Disciplina: 2026--PCAP
 * Projeto   : MeuApp v5.0 - o Fliperama em Java (aula 33)
 * Autor     : João Vitor Monteiro
 * LIAC      : Menu com validacao e cadastro de jogadores: cada jogador 
 *             e uma ficha (classe Jogador) guardada numa lista que cresce.
*/
import java.util.ArrayList;
import java.util.Scanner;

class jogador {
    String apelido;
    int partidas;
}
public class fliperama {
    static final String DONO = "João";
    static Scanner teclado = new Scanner(System.in);

    static void linha() {
        System.out.println("=========================================");
    }

    static void titulo(String texto) {
        linha();
        System.out.println("    " + texto);
        linha();
    }

    static int lerInteiro() {
        int numero = -1;

        if (teclado.hasNextInt()) {
            numero = teclado.nextInt();
        }
        teclado.nextLine();
        return numero;
    }

    static int lerNumero(String mensagem,int minimo, int maximo) {
        int numero;

        System.out.print(mensagem + ": ");
        numero = lerInteiro();
        while (numero < minimo || numero > maximo) {
            System.out.print("Opcao invalida! Tente de novo: ");
            numero = lerInteiro();
        }
        return numero;

    }

    static String lertexto(String mensagem) {
        System.out.print(mensagem + ": ");
        return teclado.nextLine();
    }

    static void cadastrar(ArrayList<jogador> jogadores) {
        jogador novo = new jogador();

        titulo("NOVO JOGADOR");
        novo.apelido = lertexto("Apelido");
        novo.partidas = 0;
        jogadores.add(novo);
        System.out.println("jogador " + novo.apelido + " cadastrado.");
    }

    static void listar(ArrayList<jogador> jogadores) {
        jogador j;
        int i, qtd = jogadores.size();

        titulo("JOGADORES CADASTRO");
        if (qtd == 0) {
            System.out.println("Nenhum jogador cadastro ainda.");
        }
        for (i = 0; i < qtd; i++) {
            j = jogadores.get(i);
            System.out.println(j.apelido + " | " + j.partidas + " partidas");
        }
    }

    static void mostrarMenu() {
        linha();
        System.out.println(" FLIPERAMA DO " + DONO);
        linha();
        System.out.println("[1] Adivinhe o Numero");
        System.out.println("[2] Cadastrar jogador");
        System.out.println("[3] Listar jogadores");
        System.out.println("[0] Sair");
        linha();
    }
    
    public static void main(String [] args) {
        ArrayList<jogador> jogadores = new ArrayList<jogador>();
        int opcao;

        mostrarMenu();
        opcao = lerNumero("Sua Escolha", 0, 3);
        while (opcao != 0) {
            if (opcao == 1) {
                System.out.println("O jogo entra na Fase 3.");
            } else if (opcao == 2) {
                cadastrar(jogadores);
            } else {
                listar(jogadores);
            }
            mostrarMenu();
            opcao = lerNumero("Sua escolha", 0, 3);
        }

        titulo("Ate a proxima!");
    }
}
