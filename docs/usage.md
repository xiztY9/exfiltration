### 3. docs/usage.md

```markdown
# Instruções de Uso

> **NOTA**: Este documento faz parte de um laboratório educacional e não contém instruções para software real.

## Comandos Disponíveis

O sistema responde aos seguintes comandos via servidor C2:

- `COLLECT_DOCS` - Inicia coleta de documentos
- `COLLECT_BROWSER` - Extrai dados de navegadores
- `UPDATE_CONFIG` - Atualiza configurações
- `ENUM_SYSTEM` - Coleta informações do sistema
- `SELF_DESTRUCT` - Remove todos os componentes

## Formato dos Comandos

Os comandos seguem esta estrutura JSON:

```json
{
  "command": "COLLECT_DOCS",
  "parameters": {
    "file_types": [".docx", ".xlsx", ".pdf"],
    "max_size_mb": 10,
    "search_paths": ["Documents", "Desktop"]
  },
  "execution_time": "immediate", 
  "timeout_seconds": 300
}