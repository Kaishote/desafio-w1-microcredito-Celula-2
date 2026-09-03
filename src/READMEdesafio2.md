# Arquitetura de Dados - Regras de Negocio da Frota

Arquivo: src/config_negocio.py

## sobre o arquivo

Esse arquivo guarda as regras de negocio da frota (densidade da carga
e os limites de compliance ambiental) dentro de um dicionario Python
chamado REGRAS_NEGOCIO, e tem uma funcao que calcula quanto a empresa
perde quando um caminhao volta de viagem com menos de 30% da carga.

## por que usei um dicionario

Podia ter deixado os numeros direto espalhados no meio do codigo, tipo
"if carga < 30" com o 30 escrito na mao ali mesmo, mas isso fica ruim
de manter depois. Se um dia a empresa quiser mudar esse limite de 30%
pra 25%, por exemplo, teria que procurar em varios lugares do sistema
pra achar onde esse numero foi usado. Colocando tudo dentro de um
dicionario so, fica so um lugar pra mexer.

Outra coisa que eu pensei foi separar as regras (que sao decisao da
empresa, tipo o limite de emissao ou o percentual minimo de carga) da
parte que calcula (a funcao calcular_custo_ociosidade). A funcao nao
tem nenhum numero fixo dentro dela, ela sempre vai buscar os valores
la no dicionario. Acho que isso ajuda bastante se for pensar numa
arquitetura de dados, porque separa bem o que é regra do que é
processamento.

## sobre compliance ambiental / green it

Essa parte de compliance eu tentei ligar com a questao de
sustentabilidade da frota, que era um dos pontos pedidos no desafio.

O limite de emissao de CO2 e a meta de reducao anual ficam guardados
de forma bem visivel dentro do dicionario, junto com as outras regras.
Acho que isso ajuda bastante numa possivel auditoria ambiental, porque
da pra mostrar facil quais eram os parametros que a empresa tava
seguindo em determinado momento, sem precisar ficar catando numero
espalhado pelo codigo todo.

A regra dos 30% de carga minima no retorno tambem tem a ver com isso.
Um caminhao voltando quase vazio gasta praticamente o mesmo
combustivel (e solta praticamente a mesma quantidade de CO2) que um
caminhao voltando cheio, so que sem aproveitar direito essa viagem. Ou
seja, alem de dar prejuizo financeiro pra empresa, é um desperdicio
ambiental tambem. Calculando esse custo de ociosidade, a empresa
consegue enxergar melhor quais rotas estao rodando "no vazio" e talvez
pensar em juntar cargas de retorno, por exemplo, pra nao rodar tanto
caminhao sem necessidade.

Por ultimo, deixei tudo guardado como dado (dicionario) em vez de so
um texto explicando as regras porque isso facilita se um dia quiserem
usar esses mesmos numeros em outra parte do sistema, tipo um painel
que soma quanto de CO2 a frota emitiu no mes, ou um alerta quando
algum caminhao passa do limite. Acho que é meio esse o objetivo de
pensar em arquitetura de dados, deixar organizado hoje pra facilitar
coisa que vai ser construida depois.

## rodando

python3 src/config_negocio.py

Isso mostra as regras carregadas e um exemplo de calculo (caminhao
voltando com 10% de carga numa viagem de 200 km).