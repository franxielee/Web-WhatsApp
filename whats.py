import pywhatkit

phone_number = "+xxxxxxxxx"
message = "Teste de mensagem py"

pywhatkit.sendwhatmsg_instantly(
    phone_number,
    message,
    wait_time=15,
    tab_close=True,
    close_time=3
)
