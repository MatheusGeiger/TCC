Projeto de Tcc


Arduino up ->
    AT+SAPBR=3,1,"Contype","GPRS"
    AT+SAPBR=3,1,"APN","www"
    AT+SAPBR=1,1
    AT+SAPBR=2,1
    AT+CIPGSMLOC=1,1
    AT+HTTPINIT
    AT+HTTPSSL=1
    AT+HTTPPARA="CID",1
    AT+HTTPPARA="URL","https://lit-river-31314.herokuapp.com/insere_coordenada/veiculo/-23.515768/-46.543343/0/"
    AT+HTTPACTION=1
