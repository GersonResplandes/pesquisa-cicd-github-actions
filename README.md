# Pesquisa de CI/CD com GitHub Actions

Relatório parcial de pesquisa em Engenharia de Software: automação de pipelines e escalabilidade operacional. Curso de Análise e Desenvolvimento de Sistemas, UNIBALSAS, 2026.2.

## Relatório

[Baixar o relatório parcial em PDF](relatorio/Pesquisa_Parcial_CICD_Gerson_UNIBALSAS.pdf). O documento contém os resultados locais e remotos, e o Apêndice E reúne os links para conferir as provas. O arquivo SHA256.txt permite verificar a integridade do PDF.

## Provas verificáveis

- [Código e histórico de commits](https://github.com/GersonResplandes/pesquisa-cicd-github-actions/commits/main/).
- [Execuções reais do GitHub Actions](https://github.com/GersonResplandes/pesquisa-cicd-github-actions/actions/workflows/ci.yml).
- [Evidências do ensaio local](https://github.com/GersonResplandes/pesquisa-cicd-github-actions/tree/main/evidencias/locais).
- [Resultados e logs remotos preservados](evidencias/github/), além dos artefatos das execuções.
- [Índice de provas e instruções de conferência](evidencias/PROVAS.md).

Os registros locais correspondem ao ensaio exploratório realizado em Windows. As execuções hospedadas no GitHub Actions possuem IDs, URLs e commits próprios. Consulte o [índice de provas](evidencias/PROVAS.md) para conferir os resultados e sua origem.

## Executar localmente

Requisitos: Python 3.11 ou superior com pip e Git no PATH. O ensaio original usou Python 3.12.14 em Windows.

```bash
git clone https://github.com/GersonResplandes/pesquisa-cicd-github-actions.git
cd pesquisa-cicd-github-actions
python pipeline.py minha-execucao-01
```

Use um identificador novo em cada execução. O pipeline executa preparação, seis testes unitários, build determinístico de `app.zip`, deploy simulado para diretório novo e smoke test. Não há dependências externas nem entrega produtiva.

## Cenários locais originais

| Cenário | Commit | Resultado |
| --- | --- | --- |
| A01, A02, A03 | `38abe9757919617b399da11f22e88357bdf6b932` | Seis testes aprovados; pacote idêntico |
| F01 | `4a920385aa5477665aaa81b0272c7dec60fb6a40` | Três testes falhos; etapas posteriores bloqueadas |
| R01, M01 | `f404c8cd35042ae132ac8e6115119543462dda2a` | Correção validada e entrega simulada concluída |

Os commits da tabela identificam o histórico local original, anterior à publicação; não são commits deste novo repositório. As três versões de app.py estão preservadas em `evidencias/locais/fontes/`. Para reproduzir um cenário local, copie a versão correspondente para app.py e execute `python pipeline.py ID_novo`. O histórico original também está no pacote suplementar do relatório.

## Workflow e segurança

O arquivo `.github/workflows/ci.yml` usa runner Ubuntu, Python 3.11, permissões de leitura, actions fixadas por SHA e retenção de artefatos de 14 dias. Os registros copiados para `evidencias/github/` ficam preservados no histórico do repositório após expiração dos artefatos.

Uma falha deliberada é um controle experimental, não uma falha inesperada da pesquisa. Este caso não mede carga de usuários, produtividade humana, disponibilidade ou segurança total de um sistema.

## Integridade dos registros

Os caminhos pessoais do computador foram removidos dos logs públicos. Os códigos de saída, resultados dos testes, commits e hashes foram conservados. A autoria acadêmica e a responsabilidade pelo trabalho pertencem ao pesquisador; as evidências técnicas são verificáveis pelas execuções e arquivos publicados.
