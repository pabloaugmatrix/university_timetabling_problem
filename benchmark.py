import subprocess
import time
import csv
import os

# Caminho do arquivo de entrada
arquivos = ["Cenário 5 - 1º Semestre.pdf", "Cenário 5 - 2º Semestre.pdf"]

for arquivo in arquivos:
    output_path = f"data/output/benchmark_{arquivo}.csv"

    # Criar diretório de saída, se necessário
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Parâmetros
    num_seeds = 30
    repeticoes = 100
    seeds = [i for i in range(num_seeds)]

    # Abrir CSV para escrita
    with open(output_path, mode="w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["execucao", "seed", "tempo_segundos"])

        tempos = []

        for seed in seeds:
            execucao = 1
            for i in range(repeticoes):
                print(f"[Execução {execucao}] Seed: {seed}")
                inicio = time.perf_counter()

                subprocess.run([
                    "python3", "-m", "src.main", arquivo, str(seed)
                ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)  # silencioso

                fim = time.perf_counter()
                duracao = fim - inicio

                writer.writerow([execucao, seed, f"{duracao:.4f}"])
                tempos.append(duracao)
                execucao += 1

        # Escreve a média ao final
        media = sum(tempos) / len(tempos)
        writer.writerow(["MÉDIA", "", f"{media:.4f}"])

    print(f"\nBenchmark completo. Resultados salvos em: {output_path}")
