# Hack The Box [ID Exposed](https://app.hackthebox.eu/challenges/131)
### References
* 
## Description
> We are looking for Sara Medson Cruz's last location, where she left a message. We need to find out what this message is! We only have her email: saramedsoncruz@gmail.com
## Challenge
1. By using Google Hangouts and the browser's developer tools, saramedsoncruz@gmail.com's Google ID was found to be `117395327982835488254`.
2. With that ID, you can use google maps https://www.google.com/maps/contrib/117395327982835488254 to find the last reviews Sara left there:

> A famosa Catedral da Sé é de longe uma das mais faraônicas estruturas arquitetônicas presentes na capital. Estar ao seu lado é sentir de forma intensa o quanto somos pequenos. É um delírio para apreciadores de construções religiosas. Por fora ela é incrível, por dentro é ainda mais majestosa! Lustres enormes, pilares gigantescos e um clima levemente fúnebre. É um ponto turístico indispensável para todos os públicos, sejam religiosos ou ateus.
>
> E claro, é até irônico ver que diante de tamanha riqueza existam centenas de pessoas mendigando o pão. A praça da Sé, onde fica a igreja, é repleta de pessoas em situação de vulnerabilidade social, não se espante se for abordado ou abordada por uma horda de pessoas lhe pedindo trocados, mas cuidado, nem sempre se trata apenas de "pedir", infelizmente há criminosos que adoram se aproveitar daquele turista distraído fazendo fotos ou mesmo daquela pessoa bondosa que vai abrir sua carteira para doar um trocado.
>
> HTB{i_W4S_D_I_S_c_O_v_3_R_3_D}

**Flag**: `HTB{i_W4S_D_I_S_c_O_v_3_R_3_D}`