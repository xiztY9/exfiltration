"""
Módulo de coleta de documentos (SIMULAÇÃO EDUCACIONAL)
Este arquivo não contém código malicioso real - só exemplos para o laboratório
"""

import os
import json

class DocumentCollector:
    """Classe que simula a coleta de documentos de um sistema"""
    
    def __init__(self, config=None):
        """Inicializa o coletor de documentos"""
        self.config = config or {
            "file_extensions": [".doc", ".docx", ".xls", ".xlsx", ".pdf", ".txt"],
            "search_paths": [
                "%USERPROFILE%\\Documents",
                "%USERPROFILE%\\Desktop",
                "%USERPROFILE%\\Downloads"
            ],
            "max_file_size_mb": 10,
            "max_files_per_session": 50
        }
        
        self.collected_files = []
    
    def find_documents(self):
        """Encontra documentos com base nas configurações"""
        print("[SIMULAÇÃO] Procurando documentos")
        
        # Simulação de documentos encontrados
        simulated_docs = [
            {"path": "C:\\Users\\adminuser\\Documents\\Financeiro_2025.xlsx", "size": 2.4, "type": "xlsx"},
            {"path": "C:\\Users\\adminuser\\Documents\\Planejamento_Estrategico.docx", "size": 1.7, "type": "docx"},
            {"path": "C:\\Users\\adminuser\\Documents\\Contratos\\NDA_Fornecedor.pdf", "size": 0.8, "type": "pdf"},
            {"path": "C:\\Users\\adminuser\\Desktop\\Relatorio_Seguranca.docx", "size": 3.2, "type": "docx"},
            {"path": "C:\\Users\\adminuser\\Documents\\Senhas.txt", "size": 0.1, "type": "txt"}
        ]
        
        print(f"[SIMULAÇÃO] Encontrados {len(simulated_docs)} documentos")
        return simulated_docs
    
    def collect_document(self, doc_info):
        """Simula a coleta de um único documento"""
        print(f"[SIMULAÇÃO] Coletando: {doc_info['path']}")
        
        # Em um cenário real, aqui seria feita a leitura do arquivo
        # e seu processamento para exfiltração
        
        self.collected_files.append(doc_info)
        return True
    
    def process_documents(self):
        """Processa documentos encontrados"""
        docs = self.find_documents()
        
        for doc in docs:
            if doc["size"] <= self.config["max_file_size_mb"]:
                self.collect_document(doc)
            else:
                print(f"[SIMULAÇÃO] Ignorando {doc['path']} - tamanho excede limite")
        
        print(f"[SIMULAÇÃO] Processados {len(self.collected_files)} de {len(docs)} documentos")
        
        # Gerar um relatório simulado
        report = {
            "timestamp": "2025-05-20T07:05:12",
            "documents_found": len(docs),
            "documents_collected": len(self.collected_files),
            "total_size_mb": sum(d["size"] for d in self.collected_files),
            "file_types": {
                "docx": len([d for d in self.collected_files if d["type"] == "docx"]),
                "xlsx": len([d for d in self.collected_files if d["type"] == "xlsx"]),
                "pdf": len([d for d in self.collected_files if d["type"] == "pdf"]),
                "txt": len([d for d in self.collected_files if d["type"] == "txt"])
            }
        }
        
        print(f"[SIMULAÇÃO] Relatório: {json.dumps(report, indent=2)}")
        return report


if __name__ == "__main__":
    print("AVISO: Este é um código de SIMULAÇÃO para fins educacionais")
    print("Não contém funcionalidades maliciosas reais")
    
    # Demonstração simulada
    collector = DocumentCollector()
    collector.process_documents()