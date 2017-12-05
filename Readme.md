Projeto de Tcc


<h4>Arduino up</h4>

    AT+SAPBR=3,1,"Contype","GPRS" <br />
    AT+SAPBR=3,1,"APN","www" <br />
    AT+SAPBR=1,1 <br />
    AT+SAPBR=2,1 <br />
    AT+CIPGSMLOC=1,1 <br />
    AT+HTTPINIT <br />
    AT+HTTPSSL=1 <br />
    AT+HTTPPARA="CID",1 <br />
    AT+HTTPPARA="URL","https://lit-river-31314.herokuapp.com/insere_coordenada/veiculo/-23.515768/-46.543343/0/" <br />
    AT+HTTPACTION=1
