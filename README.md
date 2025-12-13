# 💰 Sistema Bancário

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)


A resolução de um desafio da [dio](https://www.dio.me) onde foi apresentado um problema de um banco que deseja mordenizar das suas operações utilizando-se da linguagem Python.

Para isso, em primeira instância, por enquanto ele precisa de um sistema que comporte **apenas 1 usuário**, onde o mesmo possa ser capaz de **sacar**, **depositar** e **verificar seu extrato bancário**.

## 🔧 Funções presentes no sistema
- **Sacar**: Sacar um limite máximo de até 500 reais, caso não possua o valor requerido na conta devolve uma mensagem informando que não será possível sacar o dinheiro por falta de saldo.
    > **Observação:** O usuário será permitido sacar apenas 3 vezes ao dia.
- **Depósito**: Depositar valores **positivos** na conta do usuário. Todos os depósitos são armazenados em uma variável para serem exibidos em **Extrato** posteriormente.
- **Extrato**: Essa operação deve listar todos os depósitos e saques realizados na conta. No início da listagem deve ser exibido o saldo atual da conta. Se não ouvir nenhuma movimentação na conta deverá ser exibida a mensagem: **Não foram realizadas movimentações na conta.**
