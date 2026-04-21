import pandas as pd
from sqlalchemy import create_engine
import pywhatkit as kit
import time
import asyncio
from telegram import Bot
from datetime import datetime
import pyautogui


# 1. CONFIGURAÇÕES

# Lista de WhatsApp 
contatos_whatsapp = ["+551199999999"]  # Adicione Aqui



# Configurações do Telegram
TOKEN_TELEGRAM = "Seu_Token_Aqui"
# Se for mandar para várias pessoas, use uma lista de IDs
lista_ids_telegram = ["Seu_ID"]

# Banco de Dados
URI = f"mssql+pyodbc://./DB_Olist?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"



# 2. FUNÇÃO TELEGRAM 

async def enviar_telegram(mensagem):
    try:
        bot = Bot(token=TOKEN_TELEGRAM)
        for chat_id in lista_ids_telegram:
            await bot.send_message(
                chat_id=chat_id, text=mensagem, parse_mode="Markdown"
            )
            print(f"✅ [TELEGRAM] Enviado para ID: {chat_id}")
    except Exception as e:
        print(f"❌ [ERRO TELEGRAM] {e}")



# 3. FUNÇÃO WHATSAPP 

def enviar_whatsapp_triplo(mensagem):
    for numero in contatos_whatsapp:
        try:
            ahora = datetime.now().strftime("%H:%M:%S")
            print(f"🚀 [{ahora}] Tentando WhatsApp para {numero}...")

            # Abre, digita e espera
            kit.sendwhatmsg_instantly(
                numero, mensagem, wait_time=35, tab_close=True, close_time=10
            )

            # Força o envio físico
            time.sleep(2)
            pyautogui.press("enter")

            print(f"✅ [WHATSAPP] Enviado para {numero}!")
            time.sleep(5)
        except Exception as e:
            print(f"❌ [ERRO WHATSAPP] {e}")



# Agent

def executar_agente():
    try:
        engine = create_engine(URI)
        print(
            f"\n🔍 [{datetime.now().strftime('%H:%M:%S')}] Agente Vigilante Iniciado..."
        )

        query = "SELECT Estado, Ticket_Medio, Frete_Medio FROM tSimulacao_IA"
        df = pd.read_sql(query, engine)

        if df.empty:
            print("⚠️ Tabela vazia. Nada a monitorar.")
            return

        for index, row in df.iterrows():
            estado, ticket, frete = (
                row["Estado"],
                row["Ticket_Medio"],
                row["Frete_Medio"],
            )
            alerta = False
            msg = f"*🚨 ALERTA DE SISTEMA [{estado}]*\n"

            if ticket < 100:
                msg += f"📉 Ticket Médio Baixo: R$ {ticket:.2f}\n"
                alerta = True

            if frete > 4500:
                msg += f"🚚 Frete Crítico: R$ {frete:.2f}\n"
                alerta = True

            if alerta:
                # Dispara no Telegram (Garante o recebimento)
                asyncio.run(enviar_telegram(msg))
                # Dispara no WhatsApp (Gera o impacto visual)
                enviar_whatsapp_triplo(msg)

    except Exception as e:
        print(f"❌ [ERRO NO MOTOR]: {e}")


if __name__ == "__main__":
    executar_agente()
    print("\n🏁 TAREFA CONCLUÍDA. O Agente encerrou o monitoramento.")
