# Portfólio Acadêmico | Engenharia de Software

Repositório de trabalhos, exercícios e documentação desenvolvidos ao longo da graduação em Engenharia de Software no CEUB.

## Objetivo

Organizar os materiais acadêmicos por disciplina, documentar seu conteúdo e demonstrar o uso de Git e GitHub para controle de versão. O repositório também inclui um site estático publicado com GitHub Pages.

## Estrutura do repositório

```text
Projetos Academicos/
├── README.md
├── docs/
│   ├── index.html
│   └── style.css
├── Documentacao Ldp 1Semestre/
│   ├── README.md
│   └── PP1.doc ... PP6.doc
├── Documentacao POO/
│   ├── README.md
│   └── PP1.doc ... PP3.doc
├── Logica de Programacao 1Semestre/
│   ├── README.md
│   └── PP1.py ... PP6.py
└── Programação Orientada a Objetos/
    ├── README.md
    └── PP1.py ... PP3.py
```

## Projetos e disciplinas

| Seção | Conteúdo | Tecnologias / formatos |
|---|---|---|
| [Documentação LDP — 1º semestre](./Documentacao%20Ldp%201Semestre/README.md) | PP1 a PP6 | Microsoft Word (`.doc`) |
| [Documentação POO](./Documentacao%20POO/README.md) | PP1 a PP3 | Microsoft Word (`.doc`) |
| [Lógica de Programação — 1º semestre](./Logica%20de%20Programacao%201Semestre/README.md) | PP1 a PP6 | Python (`.py`) |
| [Programação Orientada a Objetos](./Programa%C3%A7%C3%A3o%20Orientada%20a%20Objetos/README.md) | PP1 a PP3 | Python (`.py`) |

## Site do portfólio

O site está nos arquivos `docs/index.html` e `docs/style.css`. Depois de habilitar o GitHub Pages para a branch `main` e a pasta `/docs`, ele deverá ficar disponível em:

[https://matheus-kenay.github.io/projetos-academicos-/](https://matheus-kenay.github.io/projetos-academicos-/)

## Como executar os exercícios Python

1. Instale o Python 3, caso ainda não esteja instalado.
2. Abra um terminal na pasta raiz do repositório.
3. Execute o arquivo desejado, por exemplo:

   ```powershell
   python "Logica de Programacao 1Semestre/PP1.py"
   ```

   Para um exercício de POO:

   ```powershell
   python "Programação Orientada a Objetos/PP1.py"
   ```

Os exercícios podem solicitar entradas pelo terminal. Use o arquivo correspondente à atividade que deseja testar.

## Controle de versão

As alterações são registradas com commits do Git e enviadas ao GitHub. Comandos comuns:

```powershell
git add .
git commit -m "Descreve a alteração"
git push
```

A tag `v1.0` deverá ser criada quando a primeira versão revisada do site e da documentação estiver pronta. Alterações posteriores serão registradas em novos commits.

## Autor

**Matheus Kenay** — estudante de Engenharia de Software.

## Observação acadêmica

Os materiais deste repositório são organizados para fins de estudo, acompanhamento da evolução acadêmica e apresentação de atividades desenvolvidas durante a graduação.
