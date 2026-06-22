Objetivo: Evoluir o projeto de um sistema de cadastro e classificação para um Sistema Municipal de Gestão Habitacional, contemplando todo o ciclo de vida do beneficiário, desde a inscrição até a entrega da unidade habitacional e gestão contratual.


# TODO - Sistema Municipal de Gestão Habitacional

## 1. Área Pública

### Cadastro e Consulta

* Melhorar o layout do formulário de cadastro.
* Aplicar máscaras para CPF, CEP, telefone e NIS.
* Implementar consulta automática de endereço via ViaCEP.
* Validar CPF (dígitos verificadores).
* Validar NIS.
* Permitir recuperação do cadastro por outros mecanismos (caso o cidadão esqueça o NIS).

### Cadastro do Beneficiário

* Expandir o modelo `Beneficiario` com todos os atributos previstos no cadastro habitacional.
* Incluir demais campos informativos que não influenciam na pontuação.
* Revisar organização do formulário em blocos (Dados Pessoais, Endereço, Família, Renda, Habitação etc.).

### Usabilidade

* Melhorar mensagens de sucesso e erro.
* Adicionar indicadores de progresso no cadastro.
* Melhorar a responsividade para dispositivos móveis.

---

## 2. Área Administrativa

### Interface

* Criar `base_admin.html`.
* Criar navbar exclusiva da área administrativa.
* Destacar o menu ativo.
* Exibir identificação do usuário logado.
* Adicionar botão "Voltar ao Painel".
* Adicionar botão "Encerrar sessão".
* Padronizar todas as telas administrativas utilizando `base_admin.html`.

### Dashboard

* Adicionar indicadores estatísticos.
* Adicionar gráficos.
* Exibir data/hora da última atualização.
* Exibir quantidade de empreendimentos ativos.
* Exibir últimas atividades do sistema.

### Beneficiários

* Separar `BeneficiarioUpdateView` pública e administrativa.
* Implementar exclusão lógica.
* Permitir reativação de beneficiários.
* Implementar ordenação dinâmica na listagem.
* Permitir configurar quantidade de registros por página.
* Permitir visualizar beneficiários inativos.
* Implementar histórico completo do cadastro.

---

## 3. Empreendimentos

* Cadastro de empreendimentos habitacionais.
* Situação do empreendimento.
* Quantidade de unidades.
* Data de abertura e encerramento.
* Vinculação de beneficiários ao empreendimento.
* Associação do beneficiário contemplado à unidade habitacional.
* Histórico de seleções por empreendimento.

---

## 4. Seleção Habitacional

* Processo seletivo.
* Classificação automática.
* Lista de suplentes.
* Congelamento da classificação após homologação.
* Histórico das seleções realizadas.
* Convocação dos contemplados.
* Controle de suplentes.
* Homologação da seleção.

---

## 5. Pontuação

* Histórico/versionamento dos critérios por empreendimento.
* Reprocessamento da pontuação por empreendimento.
* Reprocessamento geral.
* Auditoria das alterações de pontuação.
* Registro do motivo do recálculo.
* Preservar a classificação utilizada em seleções já homologadas.

---

## 6. Contratos

* Cadastro de modelos de contrato.
* Geração automática de contratos a partir de templates.
* Preenchimento automático dos dados do beneficiário.
* Preenchimento automático dos dados do empreendimento.
* Preenchimento automático da unidade habitacional.
* Exportação do contrato em PDF.
* Controle de assinatura.
* Histórico de contratos emitidos.
* Emissão de segunda via do contrato.

---

## 7. Exportação

* Refatorar exportação CSV para utilizar dinamicamente todos os campos do modelo.
* Exportação para Excel (.xlsx).
* Seleção de colunas para exportação.
* Exportação em PDF.
* Exportação por empreendimento.
* Exportação conforme layout exigido pela Caixa Econômica Federal.

---

## 8. Relatórios

* Relatório de classificação.
* Relatório de contemplados.
* Relatório de indeferidos.
* Estatísticas cadastrais.
* Indicadores gerenciais.
* Gráficos.
* Relatórios em PDF.
* Relatórios por empreendimento.

---

## 9. Auditoria

* Histórico completo das alterações cadastrais.
* Registro do usuário responsável por cada alteração.
* Registro de login e logout.
* Registro de reprocessamentos.
* Registro de exportações realizadas.
* Registro de geração de contratos.

---

## 10. Segurança

* Perfis de acesso.
* Permissões por funcionalidade.
* Recuperação de senha.
* Bloqueio após tentativas consecutivas de login.
* Logs de acesso.

---

## 11. Integrações

* ViaCEP.
* Receita Federal (validação de CPF, se disponível).
* CadÚnico.
* Caixa Econômica Federal (layout de exportação).
* Gov.br (estudo de viabilidade).

---

## 12. Melhorias Técnicas

* Criar serviços reutilizáveis para regras de negócio.
* Melhorar cobertura de testes.
* Criar documentação técnica do sistema.
* Dockerizar o projeto.
* Padronizar os formulários administrativos.
* Revisar a arquitetura das CBVs e dos serviços.

---

## 13. Evolução do Sistema

* Cadastro de usuários e perfis administrativos.
* Notificações automáticas aos beneficiários.
* Integração com e-mail e WhatsApp.
* Assinatura eletrônica de contratos.
* Portal do beneficiário com acompanhamento do processo.
* API para integração com outros sistemas municipais.
