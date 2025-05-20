# Arquitetura do Exfiltrator

## Componentes Principais

O Exfiltrator é composto por três componentes principais:

1. **Core Engine** - Responsável pela orquestração de todas as operações
2. **Módulos de Coleta** - Implementações específicas para coleta de diferentes tipos de dados
3. **Sistema de Comunicação** - Gerencia a comunicação segura com o servidor C2

```mermaid
graph TD
    A[Core Engine] --> B[Módulos de Coleta]
    A --> C[Sistema de Comunicação]
    B --> B1[Coletor de Documentos]
    B --> B2[Extrator de Dados de Navegador]
    C --> C1[Comunicação HTTPS]
    C --> C2[Fallback DNS Tunneling]
    A --> D[Mecanismos de Persistência]
    A --> E[Módulo de Criptografia]
    A --> F[Utilidades de Evasão]
