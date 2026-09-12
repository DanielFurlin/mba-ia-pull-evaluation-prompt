"""
Script para fazer pull de prompts do LangSmith Prompt Hub.

Este script:
1. Conecta ao LangSmith usando credenciais do .env
2. Faz pull dos prompts do Hub
3. Salva localmente em prompts/bug_to_user_story_v1.yml

SIMPLIFICADO: Usa serialização nativa do LangChain para extrair prompts.
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from langchain import hub
from utils import save_yaml, check_env_vars, print_section_header, load_yaml

load_dotenv()


def pull_prompts_from_langsmith():
    return hub.pull("leonanluppi/bug_to_user_story_v1")

def format_prompt(prompt):
    """Formata o prompt para o padrão esperado"""
    return {
        prompt.metadata["lc_hub_repo"]: { 
            "description": None,
            "system_prompt": prompt.messages[0].prompt.template,
            "user_prompt": prompt.messages[1].prompt.template,
            "version": None,
            "created_at": None,
            "tags": [],
        }
    }
    
def main():
    """Função principal"""
    ...
    save_yaml(format_prompt(pull_prompts_from_langsmith()),"prompts/bug_to_user_story_v1.yml")


if __name__ == "__main__":
    sys.exit(main())
