# 📊 Desafios de Análise de Dados - RID #185234

Repositório com as soluções dos desafios propostos no programa de formação em análise de dados. Cada desafio aborda competências diferentes, como SQL, visualização de dados no Power BI e criação de dashboards interativos.

---

## 🧩 Desafio 1 – Template Power BI

Este desafio consistiu na criação de um **template (`.pbit`) reutilizável** no Power BI, com modelagem pré-definida e estrutura visual customizada.

📂 Arquivo: [DESAFIO1.pbit](./DESAFIO1.pbit)

---

## 🔍 Desafio 2 – Plano de Ação com SQL + Dashboard

Neste desafio, foram utilizadas **queries SQL** para análise de dados e elaboração de dashboards no PowerPoint.

📂 Arquivo: [RID_ #185234 - Desafio 2 (1).pptx](./RID_%20%23185234%20-%20Desafio%202%20%281%29.pptx)

### Queries utilizadas:
- **Gênero (Pizza)**  
  `SELECT gender, COUNT(*) FROM leads_basic_details GROUP BY gender`
- **Média de Idade (Cartão)**  
  `SELECT AVG(age) AS 'Média da Idade' FROM leads_basic_details`
- **Escolaridade (Barras)**  
  `SELECT current_education, COUNT(*) FROM leads_basic_details GROUP BY current_education ORDER BY Quantidade ASC`
- **Porcentagem assistida por idioma (Tabela)**  
  `SELECT language, AVG(watched_percentage) FROM leads_demo_watched_details WHERE watched_percentage > 0.5 GROUP BY language`
- **Interações bem-sucedidas (Linhas)**  
  `SELECT call_done_date AS 'Data', lead_gen_source, COUNT(call_status) FROM leads_interaction_details JOIN leads_basic_details ON leads_interaction_details.lead_id = leads_basic_details.lead_id WHERE call_status = 'successful' GROUP BY lead_gen_source, Data ORDER BY Data ASC`

---

## 📈 Desafio 3 – Dashboard Interativo no Power BI

Criação de um **dashboard completo** no Power BI, com foco em **KPIs, visualização eficiente e navegação intuitiva**.

📂 Arquivo: [#185234_Desafio_3.pbix](./%23185234_Desafio_3.pbix)

### Habilidades demonstradas:
- Modelagem em estrela
- Criação de medidas com DAX
- Layout visual com boa usabilidade
- Construção de filtros e drill-through

#📘 Projetos em Python – Agenda de Contatos e Gerenciador de Tarefas
Este repositório contém dois projetos em Python desenvolvidos como parte do meu processo de aprendizado. Ambos os sistemas foram construídos de forma incremental, com foco em lógica de programação, estruturas de dados e manipulação de arquivos .json.

##📁 Projeto 1 – Agenda de Contatos
Sistema de agenda de contatos simples, feito a partir de uma videoaula prática. Durante o processo, foram implementadas melhorias como:

Estruturação com funções;

Menu interativo com opções para adicionar, editar, exibir e remover contatos;

Validação básica de dados para:

Nome (não vazio),

Telefone (número inteiro),

Email (deve conter @ e .);

Armazenamento persistente usando um arquivo agenda.json.

###🛠 Funcionalidades:

Adicionar contatos com validação de entrada;

Editar contatos com opções específicas (telefone, email, nome ou ambos);

Remover e listar contatos;

Salvar e carregar dados automaticamente com JSON.

##📁 Projeto 2 – Gerenciador de Tarefas
Aplicativo de lista de tarefas desenvolvido de forma progressiva, começando com comandos básicos de print e input, e evoluindo para a estrutura de dados com listas de dicionários e uso de JSON.

#🛠 Funcionalidades:

Adição de tarefas com prioridade;

Listagem de todas as tarefas;

Remoção por nome;

Salvamento e carregamento automático das tarefas no arquivo tarefas.json.

##💡 Aprendizados colocados em prática
Uso de funções para modularização do código;

Manipulação de listas de dicionários (tarefas, agenda);

Leitura e escrita de arquivos com a biblioteca json;

Laços de repetição (while, for) e condicionais;

Validação básica de dados com try-except e checagens simples.

## 📬 Contato

Desenvolvido por **Guilherme Maciel Queiroz**  
📧 [gmq2000@gmail.com]  
🔗 [LinkedIn]([https://www.linkedin.com/in/seu-perfil](https://www.linkedin.com/in/guilherme-maciel-queiroz-b7b370200/) | 




