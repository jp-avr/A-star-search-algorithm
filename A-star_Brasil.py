import heapq


class fila:
    def __init__(self):
        self.capitais = []

    def push(self, cidade, custo):
        heapq.heappush(self.capitais, (custo, cidade))

    def pop(self):
        return heapq.heappop(self.capitais)[1]

    def vazio(self):
        if (self.capitais == []):
            return True
        else:
            return False

    def check(self):
        print(self.capitais)


class cidadeNo:
    def __init__(self, cidade, distancia):
        self.cidade = str(cidade)
        self.distancia = str(distancia)


brasil = {}


def brdici():
    file = open("brasil.txt", 'r')
    for string in file:
        linha = string.split(',')
        cd1 = linha[0]
        cd2 = linha[1]
        dist = int(linha[2])
        brasil.setdefault(cd1, []).append(cidadeNo(cd2, dist))
        brasil.setdefault(cd2, []).append(cidadeNo(cd1, dist))


def disteuristica():
    h = {}
    with open("brasil_sld.txt", 'r') as file:
        for linha in file:
            linha = linha.strip().split(",")
            no = linha[0].strip()
            sld = int(linha[1].strip())
            h[no] = sld
    return h


def euristica(no, values):
    return values[no]


def astar(start, end):
    caminho = {}
    distancia = {}
    q = fila()
    h = disteuristica()
    q.push(start, 0)
    distancia[start] = 0
    caminho[start] = None
    listaExpandida = []
    while (q.vazio() == False):
        atual = q.pop()
        listaExpandida.append(atual)
        if (atual == end):
            break
        for nova in brasil[atual]:
            g_custo = distancia[atual] + int(nova.distancia)
            # print(nova.cidade, nova.distancia, "now : " + str(distancia[atual]), g_custo)
            if (nova.cidade not in distancia or g_custo < distancia[nova.cidade]):
                distancia[nova.cidade] = g_custo
                f_custo = g_custo + euristica(nova.cidade, h)
                # print(f_custo)
                q.push(nova.cidade, f_custo)
                caminho[nova.cidade] = atual
    printoutput(start, end, caminho, distancia, listaExpandida)


def printoutput(start, end, caminho, distancia, listaExpandida):
    finalcaminho = []
    i = end
    while (caminho.get(i) != None):
        finalcaminho.append(i)
        i = caminho[i]
    finalcaminho.append(start)
    finalcaminho.reverse()
    print("Algoritmo A* para o mapa do Brasil")
    print("\tCampo Grande (CG) => São Luís (SL)")
    print("=======================================================")
    print("Lista das Capitais Expandidas : " + str(listaExpandida))
    print("Número total de Capitais Expandidas : " + str(len(listaExpandida)))
    print("=======================================================")
    print("Capitais no caminho final : " + str(finalcaminho))
    print("Número total de Capitais no caminho final : " + str(len(finalcaminho)))
    print("Custo total : " + str(distancia[end]))


def main():
    inicio = "CG"  # só é necessário mudar o inicio e a saída para resultados diferentes
    destin = "SL"
    brdici()
    astar(inicio, destin)


if __name__ == "__main__":
    main()
