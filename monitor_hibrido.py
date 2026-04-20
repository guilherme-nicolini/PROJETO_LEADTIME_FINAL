import pandas as pd
from sqlalchemy import create_engine
import pywhatkit as kit
import time
import asyncio
from telegram import Bot
from datetime import datetime
import pyautogui

# ==========================================================
# 1. CONFIGURAÇÕES
# ==========================================================
# Lista de WhatsApp (Seus 3 contatos)
contatos_whatsapp = ["+5511997156466"]  # Adicione o 3º aqui

# Configurações do Telegram
TOKEN_TELEGRAM = "8374729132:AAFsFzXHQDFL5q7ajDyQf6OQqSoTRQ7QWaQ"
# Se for mandar para várias pessoas, use uma lista de IDs
lista_ids_telegram = ["6669336647"]

# Banco de Dados
URI = f"mssql+pyodbc://./DB_Olist?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"


# ==========================================================
# 2. FUNÇÃO TELEGRAM (ENVIO RÁPIDO)
# ==========================================================
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


# ==========================================================
# 3. FUNÇÃO WHATSAPP (COM ENTER FORÇADO)
# ==========================================================
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


# ==========================================================
# 4. MOTOR DO AGENTE (DISPARO ÚNICO)
# ==========================================================
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
