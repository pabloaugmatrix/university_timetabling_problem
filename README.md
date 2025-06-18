# 🎓 University Timetabling Problem (UTP)

O **University Timetabling Problem (UTP)** é um desafio clássico de agendamento de horários em instituições de ensino. Este projeto implementa uma solução utilizando o algoritmo **Forward Checking** para alocar disciplinas, professores e salas de forma otimizada.

## 🛠️ Como Executar

No terminal do linux, vá até o diretório raiz do projeto.

### ▶️ Executar uma única instância
```bash
python3 -m src.main "<arquivo_de_entrada>" [seed]
```

### Parâmetros:

***arquivo_de_entrada:*** Nome do arquivo de entrada (dentro da pasta data/input)

***seed (opcional):*** Valor para reprodução de experimentos

### Exemplo:
```bash
python3 -m src.main "Cenário 5 - 1º Semestre.pdf" 262016
```

### 📊 Executar Benchmark (Conjunto de Instâncias)

```bash
python3 benchmark.py
```

## 📂 Estrutura de Arquivos

```plaintext
.
├── data/
│   ├── input/       # Arquivos de entrada das instâncias
│   └── output/      # Resultados e relatórios gerados
│
├── src/
│   ├── solver/      # Implementação do Forward Checking
│   ├── model/       # Visualização do grafo de conflitos
│   ├── aula.py      # Classe para representar aulas/disciplinas
│   └── data/
│       ├── criar_pdf.py  # Geração de PDF com a solução
│       └── read_data.py  # Leitura e processamento dos dados
│
├── benchmark.py     # Script para experimentos em lote
└── requirements.txt # Lista de dependências do projeto
```

## 🧩 Componentes Principais
***🔍 Solver (Forward Checking)***
* Algoritmo de busca com backtracking

* Tratamento eficiente de restrições

* Heurísticas para otimização de alocações

***📊 Visualização***
* Geração automática de grafos de conflitos

* Representação visual das alocações em formato de grade

***📄 Geração de Relatórios***
* Saída em PDF com horários organizados

* Saída em CSV com métricas do benchmark