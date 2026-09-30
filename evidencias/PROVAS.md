# Índice de provas verificáveis

Repositório público: [GersonResplandes/pesquisa-cicd-github-actions](https://github.com/GersonResplandes/pesquisa-cicd-github-actions).

## Execuções hospedadas

| Cenário | Resultado | Testes aprovados | Prova |
| --- | --- | --- | --- |
| GH-A01 | success | 6/6 | [Execução 36754769925](https://github.com/GersonResplandes/pesquisa-cicd-github-actions/actions/runs/36754769925) |
| GH-F01 | failure | 3/6 | [Execução 36754802008](https://github.com/GersonResplandes/pesquisa-cicd-github-actions/actions/runs/36754802008) |
| GH-R01 | success | 6/6 | [Execução 36754815479](https://github.com/GersonResplandes/pesquisa-cicd-github-actions/actions/runs/36754815479) |

GH-F01 é a falha deliberada: multiplicação foi substituída por adição. O objetivo é comprovar que os testes impedem build e deploy simulado. GH-R01 restaura o cálculo e comprova a retomada.

## Como conferir

1. Abra a execução e confirme seu commit e a conclusão.
2. Consulte o job validar e o step de testes, empacotamento e entrega.
3. Confira os arquivos result.json e testes.log nos diretórios GH-A01, GH-F01 e GH-R01.
4. Confira o mesmo hash do pacote nas execuções válidas.
5. Em GH-F01, confira status failed, três testes falhos, etapas posteriores skipped e deployment_exists false.

Os artefatos das execuções têm retenção de 14 dias. As cópias destes registros foram preservadas no repositório para consulta posterior. Os dados locais em evidencias/locais têm origem distinta.

SHA-256 remoto do pacote válido: `678c87cff32f2ba792910809fca7ed5c55622d443dc2af98e3679b221dc97075`.

O SHA-256 remoto pode diferir do pacote local por normalização de finais de linha do arquivo app.py no checkout Git. Compare os dois ensaios como ambientes distintos; não se presume identidade binária entre Windows e Linux.

Não houve deploy produtivo, ensaio de carga ou observação de trabalho humano. Os resultados descrevem os cenários técnicos efetivamente registrados.
