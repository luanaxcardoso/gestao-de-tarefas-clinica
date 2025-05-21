# Projeto Integrado - UNIFEOB

**Disciplinas:** Computação em Nuvem e Qualidade de Software  
**Alunas:**  
- Juliana Gomes da Silva – RA: 1012023200178  
- Luana Aparecida Cardoso – RA: 1012023100720  

---

## Aplicação Web para Gestão de Tarefas de uma Clínica Estética

Aplicação desenvolvida com **FastAPI** para agendamento de atendimentos em uma clínica estética. A interface web permite visualizar, adicionar e excluir compromissos de diferentes profissionais.

---

## 📦 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/luanaxcardoso/gestao-de-tarefas-clinica.git
   
   cd gestao-de-tarefas-clinica
    ```
2. Crie um ambiente virtual:
 ```bash
   python -m venv venv
   ```
3. Ative o ambiente virtual:
   - No Windows:
     ```bash
     venv\Scripts\activate
     ```
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

5. Execute o servidor:
   ```bash
   uvicorn main:app --reload
   ```

## Technologias Utilizadas
- **Backend:** FastAPI
- **JSON:** Armazenamento dos dados
- **Frontend:** HTML, CSS, Bootstrap
- **Nuvem:** Microsoft Azure (deploy e hospedagem da aplicação) 

## O projeto é uma PAS funcional, com lógica implementada e interface construída.

| Interface com formulários e tabelas       | ✅       | IAS           |
| Funcionalidades de adicionar/excluir dados| ✅       | PAS           |